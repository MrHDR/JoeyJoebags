import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as messagebox
import usb.core
import usb.util
import time
root = tkinter.Tk()
imgbuffer = ''
Exposure = 16384
DMatrix = [
 140, 152, 172, 149, 167, 219, 142, 155, 183, 151, 170, 231,
 146, 162, 203, 143, 157, 187, 148, 165, 215, 145, 160, 199,
 141, 154, 179, 150, 169, 227, 140, 153, 175, 149, 168, 223,
 147, 164, 211, 144, 159, 195, 146, 163, 207, 143, 158, 191]
Matrix = [
 140, 152, 172, 140, 152, 172, 140, 152, 172, 140, 152, 172,
 140, 152, 172, 140, 152, 172, 140, 152, 172, 140, 152, 172,
 140, 152, 172, 140, 152, 172, 140, 152, 172, 140, 152, 172,
 140, 152, 172, 140, 152, 172, 140, 152, 172, 140, 152, 172]
LCmatrix = [
 128, 148, 220, 143, 202, 246, 131, 161, 226, 146, 215, 252,
 138, 184, 237, 133, 166, 228, 141, 197, 244, 136, 179, 235,
 130, 157, 224, 145, 211, 250, 129, 152, 222, 144, 206, 248,
 140, 193, 241, 135, 175, 233, 139, 188, 239, 134, 170, 230]

def UpdatePic(image, buff):
    hexcode = '#00FF00'
    cols = ['#E0E0E0', '#A0A0A0', '#808080', '#101010']
    tmp = '{'
    t1 = 0
    for y in range(0, 112):
        for x in range(0, 128):
            if x != 127:
                tmp += tmp.join([cols[buff[t1]]]) + ' '
            if x == 127:
                tmp += tmp.join([cols[buff[t1]]])
            t1 += 1

        if y != 111:
            tmp += '} {'
        if y == 111:
            tmp += '}'
            continue

    image.put(tmp)


def ShowImg():
    global imgbuffer
    TileX = 0
    TileY = 0
    pixX = 0
    pixY = 0
    print('Converting Tiles to Bitmap')
    for Tiles in range(0, 224):
        ReadAdd = Tiles * 16
        PixAdd = TileX * 8 + TileY * 128 * 8
        for lines in range(0, 16, 2):
            TileLine = Two2One(imgbuffer[ReadAdd + lines], imgbuffer[ReadAdd + lines + 1])
            buff[PixAdd + pixY * 128:PixAdd + pixY * 128 + 8] = TileLine
            pixY += 1

        pixY = 0
        TileX += 1
        if TileX == 16:
            TileX = 0
            TileY += 1
            continue

    print('Updating Canvas with Bitmap')
    UpdatePic(photo, buff)
    print('Done!')


def Two2One(Byte1, Byte2):
    base3 = [
     0, 0, 0, 0, 0, 0, 0, 0]
    shnu = 7
    for bits in range(0, 8):
        bi1 = Byte1 >> bits & 1
        bi2 = Byte2 >> bits & 1
        base3[shnu] = 1 * bi1 + 2 * bi2
        shnu -= 1

    return base3


def GetCamImgBuffer():
    global imgbuffer
    print('Downloading')
    imgbuffer = b''
    RAMaddress = 41216
    main_RAMBankSwitch(0)
    for packetNumber in range(0, 56):
        AddHi = RAMaddress >> 8
        AddLo = RAMaddress & 255
        dev.write(1, [17, 0, 0, AddHi, AddLo])
        USBbuffer = dev.read(129, 64)
        RAMaddress += 64
        imgbuffer = b''.join([imgbuffer, USBbuffer])

    print('Done')
    ShowImg()


def main_RAMBankSwitch(bankNumber):
    blo = bankNumber & 255
    dev.write(1, [10, 0, 1, 64, 0, blo])
    USBbuffer = dev.read(129, 64)


def UpdateRegisters(Exposure):
    main_RAMBankSwitch(16)
    Hi = Exposure >> 8
    Lo = Exposure & 255
    dev.write(1, [65, 160, 1, 0])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 2, Hi])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 3, Lo])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 4, 4])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 5, 128])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 5, 191])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 5, 48])
    USBbuffer = dev.read(129, 64)
    for dither in range(0, 48):
        dev.write(1, [65, 160, 6 + dither, DMatrix[dither]])
        USBbuffer = dev.read(129, 64)


def TriggerCamera():
    main_RAMBankSwitch(16)
    dev.write(1, [65, 160, 0, 3])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [64, 0, 16, 0, 0])


def CheckIfDone():
    main_RAMBankSwitch(16)
    dev.write(1, [17, 0, 0, 160, 0])
    return dev.read(129, 64)[0] & 1


def Snap():
    TriggerCamera()
    time.sleep(0.05)
    GetCamImgBuffer()


def UpdateExposure(Exposure):
    main_RAMBankSwitch(16)
    Hi = Exposure >> 8
    Lo = Exposure & 255
    dev.write(1, [65, 160, 2, Hi])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [65, 160, 3, Lo])
    USBbuffer = dev.read(129, 64)
    Snap()


def Inc():
    global Exposure
    Exposure += 2048
    UpdateExposure(Exposure)


def Dec():
    global Exposure
    Exposure -= 2048
    UpdateExposure(Exposure)


def Save():
    buffconv = b''
    print(len(buff))
    for conv in range(0, len(buff)):
        num = buff[conv]
        if num == 0:
            buffconv = b''.join([buffconv, b'\xff'])
        if num == 1:
            buffconv = b''.join([buffconv, b'\x7f'])
        if num == 2:
            buffconv = b''.join([buffconv, b'\xa4'])
        if num == 3:
            buffconv = b''.join([buffconv, b'\x00'])
            continue

    ROMfile = open('bmp.hed', 'rb')
    BMPheader = ROMfile.read()
    ROMfile.close()
    result = BMPheader + buffconv
    ROMfile = open('mix.bmp', 'wb')
    ROMfile.write(result)
    ROMfile.close()


dev = usb.core.find(idVendor=1133, idProduct=4660)
if dev is None:
    messagebox.showinfo('USB Error', 'I Cant find your hardware! Check the device is plugged in and the USB driver is installed')
    exit()
if dev is not None:
    dev.set_configuration()
root.geometry('128x220')
photo = tkinter.PhotoImage(width=128, height=112)
buff = [3 for j in range(0, 14336)]
UpdatePic(photo, buff)
label = tkinter.Label(root, image=photo)
label.grid()
but = tkinter.Button(root, text='Snap!', command=Snap)
but.grid()
but = tkinter.Button(root, text='Increase Exposure', command=Inc)
but.grid()
but = tkinter.Button(root, text='Decrease Exposure', command=Dec)
but.grid()
but = tkinter.Button(root, text='Save', command=Save)
but.grid()
UpdateRegisters(18432)
root.mainloop()