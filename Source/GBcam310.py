import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as messagebox
import usb.core
import usb.util
import time

root =tkinter.Tk()
imgbuffer=""
Exposure=0x4000
#Matrix used for Dithering
DMatrix=    [0x8C,0x98,0xAC,0x95,0xA7,0xDB,0x8E,0x9B,0xB7,0x97,0xAA,0xE7,
            0x92,0xA2,0xCB,0x8F,0x9D,0xBB,0x94,0xA5,0xD7,0x91,0xA0,0xC7,
            0x8D,0x9A,0xB3,0x96,0xA9,0xE3,0x8C,0x99,0xAF,0x95,0xA8,0xDF,
            0x93,0xA4,0xD3,0x90,0x9F,0xC3,0x92,0xA3,0xCF,0x8F,0x9E,0xBF]
#Dithering Disabled
Matrix = [0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,
          0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,
          0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,
          0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC,0x8C,0x98,0xAC]
#Low contrast Dithering
LCmatrix = [0x80,0x94,0xDC,0x8F,0xCA,0xF6,0x83,0xA1,0xE2,0x92,0xD7,0xFC,
            0x8A,0xB8,0xED,0x85,0xA6,0xE4,0x8D,0xC5,0xF4,0x88,0xB3,0xEB,
            0x82,0x9D,0xE0,0x91,0xD3,0xFA,0x81,0x98,0xDE,0x90,0xCE,0xF8,
            0x8C,0xC1,0xF1,0x87,0xAF,0xE9,0x8B,0xBC,0xEF,0x86,0xAA,0xE6]

    
def UpdatePic(image,buff):
    hexcode='#00FF00'
    cols=['#E0E0E0','#A0A0A0','#808080','#101010']
    tmp="{"
    t1=0
    for y in range (0,112):
        for x in range (0,128):
            if x !=127:
                tmp+=tmp.join([cols[buff[t1]]])+" "
            if x==127:
                tmp+=tmp.join([cols[buff[t1]]])
            t1+=1
        if y!=111:
            tmp+="} {"
        if y==111:
            tmp+="}"
    image.put(tmp)

def ShowImg(): #Shows the GB tile image in imgbuffer - Ready to import Real images!!!
        TileX=0 #16 tiles x 16 tiles
        TileY=0
        pixX=0
        pixY=0
        print ("Converting Tiles to Bitmap")
        for Tiles  in range (0,224):
            ReadAdd=(Tiles*16) #16 bytes per tile
            PixAdd=(TileX*8)+(TileY*128*8)
            for lines in range (0,16,2):
                TileLine=Two2One(imgbuffer[ReadAdd+lines],imgbuffer[ReadAdd+lines+1])
                buff[PixAdd+(pixY*128):PixAdd+(pixY*128)+8]=TileLine
                pixY+=1
            pixY=0
            TileX+=1
            if TileX==16:
                TileX=0
                TileY+=1
        print ("Updating Canvas with Bitmap")
        UpdatePic(photo,buff)
        print ("Done!")


def Two2One(Byte1,Byte2):    
    base3=[0,0,0,0,0,0,0,0]
    shnu=7
    for bits in range (0,8):
        bi1=(Byte1 >> bits)& 1
        bi2=(Byte2 >> bits)& 1
        base3[shnu]=(1*bi1)+(2*bi2)
        shnu-=1
    return base3


def GetCamImgBuffer():
    print ("Downloading")
    global imgbuffer
    imgbuffer=b''
    RAMaddress=0xA100
    main_RAMBankSwitch(0)
    for packetNumber in range(0,56):
        AddHi=RAMaddress>>8
        AddLo=RAMaddress&0xFF
        dev.write(0x01,[0x11,0x00,0x00,AddHi,AddLo])
        USBbuffer = dev.read(0x81,64)
        RAMaddress += 64
        imgbuffer=b''.join([imgbuffer,USBbuffer]) #faster way of doing it
    print ("Done")
    ShowImg()

def main_RAMBankSwitch(bankNumber):
    blo=bankNumber&0xFF
    dev.write(0x01,[0x0A,0x00,0x01,0x40,0x00,blo])
    USBbuffer = dev.read(0x81,64)

def UpdateRegisters(Exposure):
    main_RAMBankSwitch(0x10)

    Hi=Exposure>>8
    Lo=Exposure&0xFF

    dev.write(0x01,[0x41,0xA0,0x01,0x00])
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x02,Hi])
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x03,Lo])
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x04,0x04])
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x05,0x80])#Vref
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x05,0xBF])#Vref
    USBbuffer = dev.read(0x81,64)

    dev.write(0x01,[0x41,0xA0,0x05,0x30])#Vref
    USBbuffer = dev.read(0x81,64)

    for dither in range (0,16*3):
        dev.write(0x01,[0x41,0xA0,0x06+dither,DMatrix[dither]])
        USBbuffer = dev.read(0x81,64)
                    
    
    
def TriggerCamera():
    main_RAMBankSwitch(0x10)
    dev.write(0x01,[0x41,0xA0,0x00,0x03])
    USBbuffer = dev.read(0x81,64)
    dev.write(0x01,[0x40,0x00,0x10,0x00,0x00])

def CheckIfDone():
    main_RAMBankSwitch(16)    
    dev.write(0x01,[0x11,0x00,0x00,0xA0,0x00])
    return (dev.read(0x81,64)[0]&1)

def Snap():
        TriggerCamera()
        time.sleep(.05)
        GetCamImgBuffer()

def UpdateExposure(Exposure):
    main_RAMBankSwitch(0x10)
    Hi=Exposure>>8
    Lo=Exposure&0xFF
    dev.write(0x01,[0x41,0xA0,0x02,Hi])
    USBbuffer = dev.read(0x81,64)
    dev.write(0x01,[0x41,0xA0,0x03,Lo])
    USBbuffer = dev.read(0x81,64)
    Snap()

def Inc():
    global Exposure
    Exposure+=0x800
    UpdateExposure(Exposure)
def Dec():
    global Exposure
    Exposure-=0x800
    UpdateExposure(Exposure)

def Save():
    buffconv=b''
    print (len(buff))
    for conv in range (0,len(buff)):
        num=(buff[conv])
        if num==0:
            buffconv=b''.join([buffconv,b'\xFF'])
        if num==1:
            buffconv=b''.join([buffconv,b'\x7F'])
        if num==2:
            buffconv=b''.join([buffconv,b'\xA4'])
        if num==3:
            buffconv=b''.join([buffconv,b'\x00'])
    ROMfile=open("bmp.hed",'rb')
    BMPheader=ROMfile.read()
    ROMfile.close()
    result= BMPheader+buffconv
    
    ROMfile=open("mix.bmp",'wb')
    ROMfile.write(result)
    ROMfile.close()

        
dev = usb.core.find(idVendor=0x046d, idProduct=0x1234)
if dev is None:
    messagebox.showinfo("USB Error","I Cant find your hardware! Check the device is plugged in and the USB driver is installed")
    exit()
if dev is not None:
   # messagebox.showinfo("Welcome","Gen3 is a work in progress, please report any bugs or requests to Bennvenn@hotmail.com")
    dev.set_configuration()
root.geometry("128x220")

photo = tkinter.PhotoImage(width=128,height=112)
#Clear the Buffer
buff = [3 for j in range(0,128*112)]
UpdatePic(photo,buff)

label=tkinter.Label(root,image=photo)
label.grid()
but=tkinter.Button(root,text="Snap!",command=Snap)
but.grid()
but=tkinter.Button(root,text="Increase Exposure",command=Inc)
but.grid()
but=tkinter.Button(root,text="Decrease Exposure",command=Dec)
but.grid()
but=tkinter.Button(root,text="Save",command=Save)
but.grid()

UpdateRegisters(0x4800)

root.mainloop()

