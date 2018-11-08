from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import string
import usb.core
import usb.util
ROMsize = 0
RAMsize = 0
ROMbuffer = ''
RAMbuffer = ''
USBbuffer = ''
FlashBlockSize = 0
for usbfill in range(64):
    USBbuffer = USBbuffer + '\x00'

Command_Get_Version = [
 0]
Command_Get_ROM = [16]
Command_Set_Bank = [8]
Command_Flash_ROM = [32]

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Joey Joebags by BennVenn - V3.30')
        self.pack(fill=BOTH, expand=1)
        self.lowerLeftLabel = StringVar()
        cartSelectionLabel = Label(root, textvariable=self.lowerLeftLabel)
        cartSelectionLabel.place(x=0, y=280)
        self.lowerRightLabel = StringVar()
        hardwareStatusLabel = Label(root, textvariable=self.lowerRightLabel)
        hardwareStatusLabel.place(x=0, y=260)
        self.ROMtitleLabel = StringVar()
        ROMtitleLabel = Label(root, textvariable=self.ROMtitleLabel)
        ROMtitleLabel.place(x=0, y=0)
        self.ROMsizeLabel = StringVar()
        ROMsizeLabel = Label(root, textvariable=self.ROMsizeLabel)
        ROMsizeLabel.place(x=0, y=20)
        self.RAMsizeLabel = StringVar()
        RAMsizeLabel = Label(root, textvariable=self.RAMsizeLabel)
        RAMsizeLabel.place(x=0, y=40)
        self.MAPPERtypeLabel = StringVar()
        MAPPERtypeLabel = Label(root, textvariable=self.MAPPERtypeLabel)
        MAPPERtypeLabel.place(x=0, y=60)
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Exit', command=main_Exit)
        cartTypeMenu = Menu(menu)
        menu.add_cascade(label='Cart Type', menu=cartTypeMenu)
        MBCmenu = Menu(menu)
        cartTypeMenu.add_cascade(label='GB(C) Generic', menu=MBCmenu)
        MBCmenu.add_command(label='Get Save RAM', command=main_MBC_Dump_RAM)
        MBCmenu.add_command(label='Write Save RAM', command=main_MBC_Burn_RAM)
        MBCmenu.add_command(label='Dump ROM', command=main_MBC_Dump_ROM)
        MBC2menu = Menu(menu)
        cartTypeMenu.add_cascade(label='GB MBC2', menu=MBC2menu)
        MBC2menu.add_command(label='Get Save RAM', command=main_MBC2_Dump_RAM)
        MBC2menu.add_command(label='Write Save RAM', command=main_MBC2_Burn_RAM)
        MBC2menu.add_command(label='Dump ROM', command=main_MBC_Dump_ROM)
        GBCammenu = Menu(menu)
        cartTypeMenu.add_cascade(label='GB Camera', menu=GBCammenu)
        GBCammenu.add_command(label='Get Save RAM', command=main_Cam_Dump_RAM)
        GBCammenu.add_command(label='Write Save RAM', command=main_Cam_Burn_RAM)
        EMS32menu = Menu(menu)
        cartTypeMenu.add_cascade(label='EMS32', menu=EMS32menu)
        EMS32menu.add_command(label='Get Save RAM', command=main_MBC_Dump_256RAM)
        EMS32menu.add_command(label='Write Save RAM', command=main_MBC_Burn_RAM)
        EMS32menu.add_command(label='Dump ROM', command=main_MBC_Dump_ROM)
        EMS32menu.add_command(label='Flash ROM', command=main_EMS64_Burn_ROM)
        EMS64menu = Menu(menu)
        cartTypeMenu.add_cascade(label='EMS64', menu=EMS64menu)
        EMS64menu.add_command(label='Get Save RAM', command=main_MBC_Dump_256RAM)
        EMS64menu.add_command(label='Write Save RAM', command=main_MBC_Burn_RAM)
        EMS64menu.add_command(label='Dump ROM', command=main_MBC_Dump_ROM)
        EMS64menu.add_command(label='Flash ROM', command=main_EMS64_Burn_ROM)
        EMS64menu.add_command(label='Set page 2', command=main_EMS64_PageSwap)
        BV64menu = Menu(menu)
        BV64GSR = Menu(menu)
        BV64WSR = Menu(menu)
        cartTypeMenu.add_cascade(label='BennVenn 64M', menu=BV64menu)
        BV64menu.add_cascade(label='Get Save RAM', menu=BV64GSR)
        BV64GSR.add_command(label='128K', command=main_BV64_Dump_128K0)
        BV64GSR.add_command(label='32K (1)', command=main_BV64_Dump_32K1)
        BV64GSR.add_command(label='32K (2)', command=main_BV64_Dump_32K2)
        BV64GSR.add_command(label='32K (3)', command=main_BV64_Dump_32K3)
        BV64GSR.add_command(label='32K (4)', command=main_BV64_Dump_32K4)
        BV64menu.add_cascade(label='Write Save RAM', menu=BV64WSR)
        BV64WSR.add_command(label='128K', command=main_BV_Burn_128k0)
        BV64WSR.add_command(label='32K (1)', command=main_BV_Burn_32K0)
        BV64WSR.add_command(label='32K (2)', command=main_BV_Burn_32K1)
        BV64WSR.add_command(label='32K (3)', command=main_BV_Burn_32K2)
        BV64WSR.add_command(label='32K (4)', command=main_BV_Burn_32K3)
        BV64menu.add_command(label='Dump ROM', command=main_BV64_Dump_ROM0)
        BV64menu.add_command(label='Flash ROM', command=main_BV64_Flash_ROM0)
        BV256menu = Menu(menu)
        BV256B1 = Menu(menu)
        BV256B2 = Menu(menu)
        BV256B3 = Menu(menu)
        BV256B4 = Menu(menu)
        BV1256GSR = Menu(menu)
        BV1256WSR = Menu(menu)
        BV2256GSR = Menu(menu)
        BV2256WSR = Menu(menu)
        BV3256GSR = Menu(menu)
        BV3256WSR = Menu(menu)
        BV4256GSR = Menu(menu)
        BV4256WSR = Menu(menu)
        cartTypeMenu.add_cascade(label='BennVenn 256M', menu=BV256menu)
        BV256menu.add_cascade(label='Block1', menu=BV256B1)
        BV256menu.add_cascade(label='Block2', menu=BV256B2)
        BV256menu.add_cascade(label='Block3', menu=BV256B3)
        BV256menu.add_cascade(label='Block4', menu=BV256B4)
        BV256B1.add_cascade(label='Get Save RAM', menu=BV1256GSR)
        BV1256GSR.add_command(label='128K', command=main_BV64_Dump_128K0)
        BV1256GSR.add_command(label='32K (1)', command=main_BV64_Dump_32K1)
        BV1256GSR.add_command(label='32K (2)', command=main_BV64_Dump_32K1)
        BV1256GSR.add_command(label='32K (3)', command=main_BV64_Dump_32K1)
        BV1256GSR.add_command(label='32K (4)', command=main_BV64_Dump_32K1)
        BV256B1.add_cascade(label='Write Save RAM', menu=BV1256WSR)
        BV1256WSR.add_command(label='128K', command=main_BV_Burn_128k0)
        BV1256WSR.add_command(label='32K (1)', command=main_BV_Burn_32K0)
        BV1256WSR.add_command(label='32K (2)', command=main_BV_Burn_32K1)
        BV1256WSR.add_command(label='32K (3)', command=main_BV_Burn_32K2)
        BV1256WSR.add_command(label='32K (4)', command=main_BV_Burn_32K3)
        BV256B1.add_command(label='Dump ROM', command=main_BV64_Dump_ROM0)
        BV256B1.add_command(label='Flash ROM', command=main_BV64_Flash_ROM0)
        BV256B2.add_cascade(label='Get Save RAM', menu=BV2256GSR)
        BV2256GSR.add_command(label='128K', command=main_BV64_Dump_128K1)
        BV2256GSR.add_command(label='32K (1)', command=main_BV64_Dump_32K21)
        BV2256GSR.add_command(label='32K (2)', command=main_BV64_Dump_32K21)
        BV2256GSR.add_command(label='32K (3)', command=main_BV64_Dump_32K21)
        BV2256GSR.add_command(label='32K (4)', command=main_BV64_Dump_32K21)
        BV256B2.add_cascade(label='Write Save RAM', menu=BV2256WSR)
        BV2256WSR.add_command(label='128K', command=main_BV_Burn_128k1)
        BV2256WSR.add_command(label='32K (1)', command=main_BV_Burn_32K10)
        BV2256WSR.add_command(label='32K (2)', command=main_BV_Burn_32K11)
        BV2256WSR.add_command(label='32K (3)', command=main_BV_Burn_32K12)
        BV2256WSR.add_command(label='32K (4)', command=main_BV_Burn_32K13)
        BV256B2.add_command(label='Dump ROM', command=main_BV64_Dump_ROM1)
        BV256B2.add_command(label='Flash ROM', command=main_BV64_Flash_ROM1)
        BV256B3.add_cascade(label='Get Save RAM', menu=BV3256GSR)
        BV3256GSR.add_command(label='128K', command=main_BV64_Dump_128K2)
        BV3256GSR.add_command(label='32K (1)', command=main_BV64_Dump_32K31)
        BV3256GSR.add_command(label='32K (2)', command=main_BV64_Dump_32K31)
        BV3256GSR.add_command(label='32K (3)', command=main_BV64_Dump_32K31)
        BV3256GSR.add_command(label='32K (4)', command=main_BV64_Dump_32K31)
        BV256B3.add_cascade(label='Write Save RAM', menu=BV3256WSR)
        BV3256WSR.add_command(label='128K', command=main_BV_Burn_128k2)
        BV3256WSR.add_command(label='32K (1)', command=main_BV_Burn_32K20)
        BV3256WSR.add_command(label='32K (2)', command=main_BV_Burn_32K21)
        BV3256WSR.add_command(label='32K (3)', command=main_BV_Burn_32K22)
        BV3256WSR.add_command(label='32K (4)', command=main_BV_Burn_32K23)
        BV256B3.add_command(label='Dump ROM', command=main_BV64_Dump_ROM2)
        BV256B3.add_command(label='Flash ROM', command=main_BV64_Flash_ROM2)
        BV256B4.add_cascade(label='Get Save RAM', menu=BV4256GSR)
        BV4256GSR.add_command(label='128K', command=main_BV64_Dump_128K3)
        BV4256GSR.add_command(label='32K (1)', command=main_BV64_Dump_32K41)
        BV4256GSR.add_command(label='32K (2)', command=main_BV64_Dump_32K41)
        BV4256GSR.add_command(label='32K (3)', command=main_BV64_Dump_32K41)
        BV4256GSR.add_command(label='32K (4)', command=main_BV64_Dump_32K41)
        BV256B4.add_cascade(label='Write Save RAM', menu=BV4256WSR)
        BV4256WSR.add_command(label='128K', command=main_BV_Burn_128k3)
        BV4256WSR.add_command(label='32K (1)', command=main_BV_Burn_32K30)
        BV4256WSR.add_command(label='32K (2)', command=main_BV_Burn_32K31)
        BV4256WSR.add_command(label='32K (3)', command=main_BV_Burn_32K32)
        BV4256WSR.add_command(label='32K (4)', command=main_BV_Burn_32K33)
        BV256B4.add_command(label='Dump ROM', command=main_BV64_Dump_ROM3)
        BV256B4.add_command(label='Flash ROM', command=main_BV64_Flash_ROM3)
        CatMenu = Menu(menu)
        cartTypeMenu.add_cascade(label='Catskull 32k', menu=CatMenu)
        CatMenu.add_command(label='Erase', command=main_Catskull_erase)
        CatMenu.add_command(label='Flash', command=main_Catskull_write)
        Bung32menu = Menu(menu)
        cartTypeMenu.add_cascade(label='Bung 32M', menu=Bung32menu, state=DISABLED)
        Bung32menu.add_command(label='Get Save RAM')
        Bung32menu.add_command(label='Write Save RAM')
        Bung32menu.add_command(label='Dump ROM')
        Bung32menu.add_command(label='Flash ROM')
        Bung64menu = Menu(menu)
        cartTypeMenu.add_cascade(label='Bung 64M', menu=Bung64menu, state=DISABLED)
        Bung64menu.add_command(label='Get Save RAM')
        Bung64menu.add_command(label='Write Save RAM')
        Bung64menu.add_command(label='Dump ROM')
        Bung64menu.add_command(label='Flash ROM')
        JPNmenu = Menu(menu)
        cartTypeMenu.add_cascade(label='DMG-MMSA-JPN', menu=JPNmenu)
        JPNmenu.add_command(label='Get Save RAM', command=main_MBC_Dump_RAM)
        JPNmenu.add_command(label='Write Save RAM', command=main_MBC_Burn_RAM)
        JPNmenu.add_command(label='Dump ROM', command=main_MBC_Dump_ROM)
        JPNmenu.add_command(label='Flash ROM', command=main_JPN_Burn_ROM)
        JPNmenu.add_command(label='Unlock Sector 0', command=main_JPN_Unlock_ROM)
        MXmenu = Menu(menu)
        cartTypeMenu.add_cascade(label='Shark MX', menu=MXmenu)
        MXmenu.add_command(label='Get Save RAM', command=main_MBC_Dump_RAM)
        MXmenu.add_command(label='Write Save RAM', command=main_MBC_Burn_RAM)
        MXmenu.add_command(label='Dump ROM', command=main_MX_Dump_ROM)
        MXmenu.add_command(label='Flash ROM', command=main_MX_Burn_ROM)
        ELmenu = Menu(menu)
        cartTypeMenu.add_cascade(label='El-Cheapo', menu=ELmenu)
        ELmenu.add_command(label='Erase', command=main_ELCheapo_Erase)
        ELmenu.add_command(label='Flash ROM', command=main_ELCheapo_Write)
        cartTypeMenu.add_separator()
        ELmenuSD = Menu(menu)
        cartTypeMenu.add_cascade(label='El-Cheapo SD', menu=ELmenuSD)
        ELmenuSD.add_command(label='Erase', command=main_ELCheapoSD_Erase)
        ELmenuSD.add_command(label='Flash ROM', command=main_ELCheapoSD_Write)
        cartTypeMenu.add_separator()
        BV5menu = Menu(menu)
        cartTypeMenu.add_cascade(label='Chinese BV5 Clone Cart', menu=BV5menu)
        BV5menu.add_command(label='Erase', command=main_BV5_Erase)
        BV5menu.add_command(label='Flash ROM', command=main_BV5_Write)
        cartTypeMenu.add_separator()
        GBA_GenericMenu = Menu(menu)
        GBA_ROM_Size = Menu(menu)
        GBA_ROM_Burn = Menu(menu)
        cartTypeMenu.add_cascade(label='GBA Generic', menu=GBA_GenericMenu)
        GBA_GenericMenu.add_command(label='Read Header', command=main_GBA_ReadHeader)
        GBA_GenericMenu.add_separator()
        GBA_GenericMenu.add_command(label='Dump 4kbit EEPROM', command=main_GBA_EEPROM_4k)
        GBA_GenericMenu.add_command(label='Dump 64kbit EEPROM', command=main_GBA_EEPROM_64k)
        GBA_GenericMenu.add_command(label='Write 4kbit EEPROM', command=main_GBA_Write4kEEPROM)
        GBA_GenericMenu.add_command(label='Write 64kbit EEPROM', command=main_GBA_Write64kEEPROM)
        GBA_GenericMenu.add_separator()
        GBA_GenericMenu.add_command(label='Dump 64kbytes SRAM', command=main_GBA_Dump64kSRAM)
        GBA_GenericMenu.add_command(label='Write 64k to SRAM', command=main_GBA_Write64kSRAM)
        GBA_GenericMenu.add_separator()
        GBA_GenericMenu.add_command(label='Dump 64kbytes FLASH', command=main_GBA_Dump64kFLASH)
        GBA_GenericMenu.add_command(label='Dump 128kbytes FLASH', command=main_GBA_Dump128kFLASH)
        GBA_GenericMenu.add_command(label='Write 64k to FLASH', command=main_GBA_Write64kFLASHRAM)
        GBA_GenericMenu.add_command(label='Write 128k to FLASH', command=main_GBA_Write128kFLASHRAM)
        GBA_GenericMenu.add_separator()
        GBA_GenericMenu.add_cascade(label='Dump ROM', menu=GBA_ROM_Size)
        GBA_ROM_Size.add_command(label='8mbit', command=main_GBA_Dump_8)
        GBA_ROM_Size.add_command(label='16mbit', command=main_GBA_Dump_16)
        GBA_ROM_Size.add_command(label='32mbit', command=main_GBA_Dump_32)
        GBA_ROM_Size.add_command(label='64mbit', command=main_GBA_Dump_64)
        GBA_ROM_Size.add_command(label='128mbit', command=main_GBA_Dump_128)
        GBA_ROM_Size.add_command(label='256mbit', command=main_GBA_Dump_256)
        GBA_BV = Menu(menu)
        cartTypeMenu.add_cascade(label='GBA BennVenn128M', menu=GBA_BV)
        GBA_BV.add_command(label='Flash ROM', command=main_GBA_Flash_ROM)
        GBA_DD = Menu(menu)
        cartTypeMenu.add_cascade(label='GBA 4400 clone cart', menu=GBA_DD)
        GBA_DD.add_command(label='Flash ROM', command=main_GBA_Flash_ROM_DD)
        functionMenu = Menu(menu)
        menu.add_cascade(label='Function', menu=functionMenu)
        functionMenu.add_command(label='Read Cart Header', command=main_readCartHeader)
        functionMenu.add_separator()
        joeyMenu = Menu(menu)
        menu.add_cascade(label='Joey', menu=joeyMenu)
        joeyMenu.add_command(label='Enter Update Key', command=main_SendKey)
        joeyMenu.add_command(label='Update Firmware', command=main_updateFirmware)
        joeyMenu.add_command(label='Update Firmware (Legacy)', command=main_updateFirmwareLegacy)
        joeyMenu.add_separator()
        self.lowerRightLabel.set('Hardware Not Detected')
        self.ROMtitleLabel.set('ROM Title: Unknown')
        self.ROMsizeLabel.set('ROM Size: Unknown')
        self.RAMsizeLabel.set('RAM Size: Unknown')
        self.MAPPERtypeLabel.set('Mapper: Unknown')


def main_Header():
    Header = ''
    dev.write(1, [16, 0, 0, 1, 0])
    dat = dev.read(129, 64)
    Header = dat
    msg = [16, 0, 0, 1, 64]
    dev.write(1, msg)
    dat = dev.read(129, 64)
    Header += dat
    msg = [16, 0, 0, 1, 128]
    dev.write(1, msg)
    dat = dev.read(129, 64)
    Header += dat
    print('ROM Title: ' + str(Header[52:67]))


def main_readCartHeader():
    global ROMsize
    global RAMsize
    main_BV_SetBank(0, 0)
    main_ROMBankSwitch(1)
    RAMtypes = [0, 2048, 8192, 32768, 131072, 65536]
    Header = ''
    dev.write(1, [16, 0, 0, 1, 0])
    dat = dev.read(129, 64)
    Header = dat
    msg = [16, 0, 0, 1, 64]
    dev.write(1, msg)
    dat = dev.read(129, 64)
    Header += dat
    msg = [16, 0, 0, 1, 128]
    dev.write(1, msg)
    dat = dev.read(129, 64)
    Header += dat
    ROMsize = 32768 * 2 ** Header[72]
    app.ROMtitleLabel.set('ROM Title: ' + str(Header[52:67], 'utf-8'))
    app.ROMsizeLabel.set('ROM Size: ' + str(32768 * 2 ** Header[72]))
    RAMsize = RAMtypes[Header[73]]
    app.RAMsizeLabel.set('RAM Size:' + str(RAMsize))


def main_Exit():
    exit()


def main_LoadROM():
    global ROMsize
    global ROMbuffer
    ROMfileName = askopenfilename(filetypes=(('GB ROM File', '*.GB'), ('GBC ROM File', '*.GBC'),
                                             ('GBA ROM File', '*.GBA'), ('All Files', '*.*')))
    if ROMfileName:
        ROMfile = open(ROMfileName, 'rb')
        ROMbuffer = ROMfile.read()
        ROMsize = len(ROMbuffer)
        ROMfile.close()
        return 1
    return 0


def main_SaveROM():
    ROMfileName = asksaveasfilename(defaultextension='.GB', filetypes=(('GB ROM File', '*.GB'),
                                                                       ('GBC ROM File', '*.GBC'),
                                                                       ('GBA ROM File', '*.GBA'),
                                                                       ('All Files', '*.*')))
    if ROMfileName:
        ROMfile = open(ROMfileName, 'wb')
        ROMfile.write(ROMbuffer)
        ROMfile.close()


def main_LoadRAM():
    global RAMbuffer
    global RAMsize
    RAMfileName = askopenfilename(filetypes=(('GB/C/A SRAM File', '*.SAV'), ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'rb')
        RAMbuffer = RAMfile.read()
        RAMsize = len(RAMbuffer)
        RAMfile.close()
        return 1
    return 0


def main_SaveRAM():
    print(len(RAMbuffer))
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GB/C/A SRAM File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        RAMfile.write(RAMbuffer)
        RAMfile.close()


def main_updateFirmware():
    A = Get_Key_State()
    if A == 1:
        FWfileName = askopenfilename(filetypes=(('BennVenn Firmware File', '*.BEN'),
                                                ('All Files', '*.*')))
        if FWfileName:
            FWfile = open(FWfileName, 'rb')
            FWbuffer = FWfile.read()
            FWsize = len(FWbuffer)
            if FWsize == 33280:
                dev.write(1, [3])
                USBbuffer = dev.read(129, 64)
                app.lowerRightLabel.set('File Size Correct')
                for FWpos in range(512, 33279, 64):
                    dev.write(1, FWbuffer[FWpos:FWpos + 64])

            else:
                app.lowerRightLabel.set('File Invalid')
            FWfile.close()
            exit()
    if A == 0:
        messagebox.showinfo('Error', 'Please enter Key before updating firmware')


def main_updateFirmwareLegacy():
    FWfileName = askopenfilename(filetypes=(('BennVenn Firmware File', '*.BEN'), ('All Files', '*.*')))
    if FWfileName:
        FWfile = open(FWfileName, 'rb')
        FWbuffer = FWfile.read()
        FWsize = len(FWbuffer)
        if FWsize == 33280:
            dev.write(1, [3])
            USBbuffer = dev.read(129, 64)
            app.lowerRightLabel.set('File Size Correct')
            for FWpos in range(512, 33279, 64):
                dev.write(1, FWbuffer[FWpos:FWpos + 64])

        else:
            app.lowerRightLabel.set('File Invalid')
        FWfile.close()
        exit()


def main_CheckVersion():
    dev.write(1, Command_Get_Version)
    dat = dev.read(129, 64)
    sdat = ''
    for x in range(5):
        sdat = sdat + chr(dat[x])

    D = SDID_Read()
    app.lowerRightLabel.set('Firmware ' + sdat + ' Device ID: ' + D)


def main_MBC_Dump_ROM():
    global BankSize
    BankSize = 16384
    main_readCartHeader()
    main_dumpROM()


def main_MX_Dump_ROM():
    global BankSize
    BankSize = 16384
    main_readCartHeader()
    main_dumpMXROM()


def main_MBC_Dump_RAM():
    global BankSize
    BankSize = 16384
    main_readCartHeader()
    dev.write(1, [10, 0, 1, 96, 0, 1])
    USBbuffer = dev.read(129, 64)
    main_dumpRAM()
    main_SaveRAM()


def main_MBC_Dump_256RAM():
    global BankSize
    global RAMsize
    BankSize = 16384
    main_readCartHeader()
    RAMsize = 131072
    main_dumpRAM()
    main_SaveRAM()


def main_MBC2_Dump_RAM():
    global BankSize
    global RAMsize
    RAMsize = 512
    BankSize = 512
    main_dumpRAM2()
    main_SaveRAM()


def main_MBC_Burn_RAM():
    global BankSize
    BankSize = 16384
    main_readCartHeader()
    dev.write(1, [10, 0, 1, 96, 0, 1])
    USBbuffer = dev.read(129, 64)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_MBC2_Burn_RAM():
    global BankSize
    global RAMsize
    RAMsize = 512
    BankSize = 512
    if main_LoadRAM() == 1:
        main_BurnRAM2()


def main_BV64_Dump_ROM(ROMBlk):
    global ROMsize
    global BankSize
    BankSize = 16384
    ROMsize = 8388608
    main_BV_SetBank(ROMBlk, 0)
    main_dumpROM()


def main_BV64_Flash_ROM():
    global FlashBlockSize
    global BankSize
    FlashBlockSize = 131072
    BankSize = 16384
    if main_LoadROM() == 1:
        main_BV_lockBank(1)
        main_BV_FlashROM()


def main_BV64_Flash_ROM0():
    main_BV_Flash_ROM(0)


def main_BV64_Flash_ROM1():
    main_BV_Flash_ROM(1)


def main_BV64_Flash_ROM2():
    main_BV_Flash_ROM(2)


def main_BV64_Flash_ROM3():
    main_BV_Flash_ROM(3)


def main_BV64_Dump_ROM0():
    main_BV64_Dump_ROM(0)


def main_BV64_Dump_ROM1():
    main_BV64_Dump_ROM(1)


def main_BV64_Dump_ROM2():
    main_BV64_Dump_ROM(2)


def main_BV64_Dump_ROM3():
    main_BV64_Dump_ROM(3)


def main_BV64_Dump_32K1():
    main_BV64_Dump_32K(0, 0)


def main_BV64_Dump_32K2():
    main_BV64_Dump_32K(0, 1)


def main_BV64_Dump_32K3():
    main_BV64_Dump_32K(0, 2)


def main_BV64_Dump_32K4():
    main_BV64_Dump_32K(0, 3)


def main_BV64_Dump_32K21():
    main_BV64_Dump_32K(1, 0)


def main_BV64_Dump_32K22():
    main_BV64_Dump_32K(1, 1)


def main_BV64_Dump_32K23():
    main_BV64_Dump_32K(1, 2)


def main_BV64_Dump_32K24():
    main_BV64_Dump_32K(1, 3)


def main_BV64_Dump_32K31():
    main_BV64_Dump_32K(2, 0)


def main_BV64_Dump_32K32():
    main_BV64_Dump_32K(2, 1)


def main_BV64_Dump_32K33():
    main_BV64_Dump_32K(2, 2)


def main_BV64_Dump_32K34():
    main_BV64_Dump_32K(2, 3)


def main_BV64_Dump_32K41():
    main_BV64_Dump_32K(3, 0)


def main_BV64_Dump_32K42():
    main_BV64_Dump_32K(3, 1)


def main_BV64_Dump_32K43():
    main_BV64_Dump_32K(3, 2)


def main_BV64_Dump_32K44():
    main_BV64_Dump_32K(3, 3)


def main_BV64_Dump_128K0():
    main_BV64_Dump_128K(0)


def main_BV64_Dump_128K1():
    main_BV64_Dump_128K(1)


def main_BV64_Dump_128K2():
    main_BV64_Dump_128K(2)


def main_BV64_Dump_128K3():
    main_BV64_Dump_128K(3)


def main_Cam_Dump_RAM():
    global BankSize
    global RAMsize
    BankSize = 16384
    RAMsize = 131072
    main_dumpRAM()
    main_SaveRAM()


def main_Cam_Burn_RAM():
    global RAMsize
    if main_LoadRAM() == 1:
        RAMsize = 131072
        main_BurnRAM()


def main_BV_Burn_32K0():
    main_BV_SetBank(0, 0)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K1():
    main_BV_SetBank(0, 1)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K2():
    main_BV_SetBank(0, 2)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K3():
    main_BV_SetBank(0, 3)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K10():
    main_BV_SetBank(1, 0)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K11():
    main_BV_SetBank(1, 1)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K12():
    main_BV_SetBank(1, 2)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K13():
    main_BV_SetBank(1, 3)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K20():
    main_BV_SetBank(2, 0)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K21():
    main_BV_SetBank(2, 1)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K22():
    main_BV_SetBank(2, 2)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K23():
    main_BV_SetBank(2, 3)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K30():
    main_BV_SetBank(3, 0)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K31():
    main_BV_SetBank(3, 1)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K32():
    main_BV_SetBank(3, 2)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_32K33():
    main_BV_SetBank(3, 3)
    if main_LoadRAM() == 1:
        main_BurnRAM()


def main_BV_Burn_128k0():
    main_BV_Burn_128k(0)


def main_BV_Burn_128k1():
    main_BV_Burn_128k(1)


def main_BV_Burn_128k2():
    main_BV_Burn_128k(2)


def main_BV_Burn_128k3():
    main_BV_Burn_128k(3)


def main_BV_Burn_128k(bnum):
    global RAMbuffer
    global RAMsize
    if main_LoadRAM() == 1:
        RAMsize = 32768
        tempRAMbuffer = RAMbuffer
        RAMbuffer = tempRAMbuffer[0:32768]
        main_BV_SetBank(bnum, 0)
        main_BurnRAM()
        RAMbuffer = tempRAMbuffer[32768:65536]
        main_BV_SetBank(bnum, 1)
        main_BurnRAM()
        RAMbuffer = tempRAMbuffer[65536:98304]
        main_BV_SetBank(bnum, 2)
        main_BurnRAM()
        RAMbuffer = tempRAMbuffer[98304:131072]
        main_BV_SetBank(bnum, 3)
        main_BurnRAM()


def main_BV64_Dump_128K(blk):
    global RAMbuffer
    global BankSize
    global RAMsize
    TempRAMbuffer = b''
    BankSize = 16384
    RAMsize = 32768
    main_BV_SetBank(blk, 0)
    main_dumpRAM()
    TempRAMbuffer = RAMbuffer
    main_BV_SetBank(blk, 1)
    main_dumpRAM()
    TempRAMbuffer = TempRAMbuffer + RAMbuffer
    main_BV_SetBank(blk, 2)
    main_dumpRAM()
    TempRAMbuffer = TempRAMbuffer + RAMbuffer
    main_BV_SetBank(blk, 3)
    main_dumpRAM()
    RAMbuffer = TempRAMbuffer + RAMbuffer
    RAMsize = 131072
    main_SaveRAM()


def main_BV64_Dump_32K(blk, sublk):
    global BankSize
    global RAMsize
    BankSize = 16384
    RAMsize = 32768
    main_BV_SetBank(blk, sublk)
    main_dumpRAM()
    main_SaveRAM()


def main_BV_lockBank(bnum):
    bnum = bnum + 144
    print('Flash locked to ', hex(bnum))
    dev.write(1, [10, 0, 3, 112, 0, 0, 112, 1, 0, 112, 2, bnum])
    USBbuffer = dev.read(129, 64)


def main_BV_SetBank(blk, sublk):
    sublk = sublk * 64
    print(hex(blk), hex(sublk))
    dev.write(1, [10, 0, 3, 112, 0, sublk, 112, 1, 224, 112, 2, blk])
    USBbuffer = dev.read(129, 64)


def main_BV_Flash_ROM(block):
    FFtest = ''
    FFtest = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    main_LoadROM()
    FlashBlockSize = 131072
    messagebox.showinfo('Block Change Required', 'Please remove and insert Flash cart, then click OK')
    main_BV_lockBank(block)
    print('from flashrom() ', ROMsize, FlashBlockSize)
    NumOfBlks = int(ROMsize / FlashBlockSize)
    if NumOfBlks == 0:
        NumOfBlks = 1
    print('erasing ', NumOfBlks)
    print('Erasing ROM Area required for flash')
    for blknum in range(0, NumOfBlks):
        main_BV_EraseFlashBlock(blknum)

    print('Writing ROM Data')
    ROMpos = 0
    waitcount = 0
    for BankNumber in range(0, int(ROMsize / 16384)):
        main_ROMBankSwitch(BankNumber)
        print(BankNumber * 16384, ' of ', ROMsize)
        for ROMAddress in range(16384, 32768, 32):
            if BankNumber == 0:
                ROMAddress = ROMAddress - 16384
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data32Bytes = ROMbuffer[ROMpos:ROMpos + 32]
            if Data32Bytes == FFtest:
                pass
            else:
                AddHi = AddHi.to_bytes(1, 'little')
                AddLo = AddLo.to_bytes(1, 'little')
                FlashWriteCommand = b' \x00\x04*\n\xaa\xa9\x05UV' + AddHi + AddLo + b'&' + AddHi + AddLo + b'\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                USBoutputPacket = FlashWriteCommand + Data32Bytes
                dev.write(1, USBoutputPacket)
                while main_IsFlashBusy() == 1:
                    waitcount += 1
                    if waitcount == 10:
                        print('Error: ', USBoutputPacket, BankNumber, AddHi, AddLo, ROMpos)
                        continue

                waitcount = 0
            ROMpos += 32

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Block Unlock Required', 'Writing Complete. Please remove and insert Flash cart, then click OK')


def main_MX_Burn_ROM():
    print('Erasing Flash')
    mx1()
    while main_JPN_Read(0) != 255:
        pass

    print('Chip erase complete')
    main_LoadROM()
    addold = 0
    print('Writing ROM Data')
    for address in range(0, ROMsize, 32):
        AddHi = address >> 16 & 255
        AddMe = address >> 8 & 255
        AddLo = address & 255
        Data32Bytes = ROMbuffer[address:address + 32]
        AddHi = AddHi.to_bytes(1, 'little')
        AddMe = AddMe.to_bytes(1, 'little')
        AddLo = AddLo.to_bytes(1, 'little')
        FlashWriteCommand = b'#' + AddHi + AddMe + AddLo
        Data32Bytes = ROMbuffer[address:address + 32]
        USBoutputPacket = FlashWriteCommand + Data32Bytes
        dev.write(1, USBoutputPacket)
        USBbuffer = dev.read(129, 64)
        print('writing', address, ROMsize)

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')


def mx1():
    dev.write(1, [10, 0, 7, 63, 0, 65, 85, 85, 170, 42, 170, 85, 85, 85, 128, 85, 85, 170, 42, 170, 85, 85, 85, 16])
    print('Erasing Flash')
    while main_JPN_Read(0) != 255:
        pass

    print('Chip erase complete')


def mx2():
    dev.write(1, [35, 0, 0, 32, 1, 2, 3, 4, 5, 6, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85])
    USBbuffer = dev.read(129, 64)


def mx3(address):
    AddHi = address >> 16 & 255
    AddMe = address >> 8 & 255
    AddLo = address & 255
    Data32Bytes = b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
    AddHi = AddHi.to_bytes(1, 'little')
    AddMe = AddMe.to_bytes(1, 'little')
    AddLo = AddLo.to_bytes(1, 'little')
    FlashWriteCommand = b'#' + AddHi + AddMe + AddLo
    USBoutputPacket = FlashWriteCommand + Data32Bytes
    dev.write(1, USBoutputPacket)
    USBbuffer = dev.read(129, 64)


def main_EMS64_PageSwap():
    dev.write(1, [19])
    USBbuffer = dev.read(129, 64)


def main_EMS64_Burn_ROM():
    main_EMS64_Flash_ROM()


def main_EMS64_Flash_ROM():
    FFtest = ''
    for usbfill in range(32):
        FFtest = FFtest + 'ÿ'

    main_LoadROM()
    FlashBlockSize = 131072
    NumOfBlks = int(ROMsize / FlashBlockSize)
    if NumOfBlks == 0:
        NumOfBlks = 1
    print('erasing ', NumOfBlks)
    print('Erasing ROM Area required for flash')
    for blknum in range(0, NumOfBlks):
        main_EMS64_EraseFlashBlock(blknum)

    print('Writing ROM Data')
    ROMpos = 0
    waitcount = 0
    for BankNumber in range(0, int(ROMsize / 16384)):
        main_ROMBankSwitch(BankNumber)
        print(BankNumber * 16384, ' of ', ROMsize)
        for ROMAddress in range(16384, 32768, 32):
            if BankNumber == 0:
                ROMAddress = ROMAddress - 16384
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data32Bytes = ROMbuffer[ROMpos:ROMpos + 32]
            AddHi = AddHi.to_bytes(1, 'little')
            AddLo = AddLo.to_bytes(1, 'little')
            FlashWriteCommand = b'!\x01\x02\xd0' + AddHi + AddLo + b'\xe8' + AddHi + AddLo + b'\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            USBoutputPacket = FlashWriteCommand + Data32Bytes
            dev.write(1, USBoutputPacket)
            while main_IsFlashBusyEMS() == 1:
                waitcount += 1
                if waitcount == 10:
                    print('Error: ', USBoutputPacket, BankNumber, AddHi, AddLo, ROMpos)
                    continue

            waitcount = 0
            ROMpos += 32

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')
    main_ROMBankSwitch(0)
    dev.write(1, [10, 1, 1, 0, 0, 255])
    USBbuffer = dev.read(129, 64)


def main_EMS64_EraseFlashBlock(BlockNum):
    main_ROMBankSwitch(BlockNum * 8)
    print('Erasing Block ' + str(BlockNum))
    dev.write(1, [10, 1, 2, 64, 0, 32, 64, 0, 208])
    USBbuffer = dev.read(129, 64)
    waitcount = 0
    while main_IsFlashBusyEMS() == 1:
        waitcount += 1
        if waitcount == 100000:
            print('Error: ', BlockNum)
            exit()
            continue

    dev.write(1, [10, 1, 1, 64, 0, 255])
    USBbuffer = dev.read(129, 64)
    print('Done')


def main_dumpROM():
    global ROMbuffer
    ROMfileName = asksaveasfilename(defaultextension='.GB', filetypes=(('GB ROM File', '*.GB'),
                                                                       ('GBC ROM File', '*.GBC'),
                                                                       ('GBA ROM File', '*.GBA'),
                                                                       ('All Files', '*.*')))
    if ROMfileName:
        ROMfile = open(ROMfileName, 'wb')
        for bankNumber in range(0, int(ROMsize / BankSize)):
            print('Dumping ROM:', int(bankNumber * BankSize), ' of ', ROMsize)
            if bankNumber == 0:
                ROMaddress = 0
            else:
                ROMaddress = BankSize
            main_ROMBankSwitch(bankNumber)
            for packetNumber in range(0, int(BankSize / 64)):
                AddHi = ROMaddress >> 8
                AddLo = ROMaddress & 255
                dev.write(1, [16, 0, 0, AddHi, AddLo])
                ROMbuffer = dev.read(129, 64)
                ROMfile.write(ROMbuffer)
                ROMaddress += 64

        ROMfile.close()
        print('Done!')


def main_dumpMXROM():
    global ROMbuffer
    ROMfileName = asksaveasfilename(filetypes=(('GB ROM File', '*.GB'), ('GBC ROM File', '*.GBC'),
                                               ('GBA ROM File', '*.GBA'), ('All Files', '*.*')))
    if ROMfileName:
        ROMfile = open(ROMfileName, 'wb')
        for bankNumber in range(0, int(ROMsize / BankSize)):
            print('Dumping ROM:', int(bankNumber * BankSize), ' of ', ROMsize)
            if bankNumber == 0:
                ROMaddress = 0
            else:
                ROMaddress = BankSize
            main_MXROMBankSwitch(bankNumber)
            for packetNumber in range(0, int(BankSize / 64)):
                AddHi = ROMaddress >> 8
                AddLo = ROMaddress & 255
                dev.write(1, [16, 0, 0, AddHi, AddLo])
                ROMbuffer = dev.read(129, 64)
                ROMfile.write(ROMbuffer)
                ROMaddress += 64

        ROMfile.close()
        print('Done!')


def main_dumpRAM():
    global RAMbuffer
    global USBbuffer
    RAMbuffer = b''
    for bankNumber in range(0, int(RAMsize / 8192)):
        RAMaddress = 40960
        main_RAMBankSwitch(bankNumber)
        for packetNumber in range(0, int(128.0)):
            AddHi = RAMaddress >> 8
            AddLo = RAMaddress & 255
            dev.write(1, [17, 0, 0, AddHi, AddLo])
            USBbuffer = dev.read(129, 64)
            RAMaddress += 64
            RAMbuffer = b''.join([RAMbuffer, USBbuffer])


def main_dumpRAM2():
    global RAMbuffer
    global USBbuffer
    RAMbuffer = b''
    RAMaddress = 40960
    for packetNumber in range(0, int(8.0)):
        AddHi = RAMaddress >> 8
        AddLo = RAMaddress & 255
        dev.write(1, [17, 0, 0, AddHi, AddLo])
        USBbuffer = dev.read(129, 64)
        RAMaddress += 64
        RAMbuffer = b''.join([RAMbuffer, USBbuffer])

    print('Done')


def main_BurnRAM():
    global USBbuffer
    RAMaddress = 40960
    Rpos = 0
    for bankNumber in range(0, int(RAMsize / 8192)):
        RAMaddress = 40960
        main_RAMBankSwitch(bankNumber)
        for packetNumber in range(0, int(128)):
            AddHi = RAMaddress >> 8
            AddLo = RAMaddress & 255
            dev.write(1, [18, 0, 0, AddHi, AddLo])
            USBbuffer = dev.read(129, 64)
            dev.write(1, RAMbuffer[Rpos:Rpos + 64])
            USBbuffer = dev.read(129, 64)
            RAMaddress += 64
            Rpos += 64

    print('Done')


def main_BurnRAM2():
    global USBbuffer
    Rpos = 0
    RAMaddress = 40960
    for packetNumber in range(0, int(8)):
        AddHi = RAMaddress >> 8
        AddLo = RAMaddress & 255
        dev.write(1, [18, 0, 0, AddHi, AddLo])
        USBbuffer = dev.read(129, 64)
        dev.write(1, RAMbuffer[Rpos:Rpos + 64])
        USBbuffer = dev.read(129, 64)
        RAMaddress += 64
        Rpos += 64

    print('Done')


def main_IsFlashBusy():
    dev.write(1, [11, 0])
    temp = dev.read(129, 64)
    if temp[0] == 1:
        return 1
    if temp[0] == 0:
        return 0


def main_IsFlashBusyEMS():
    dev.write(1, [12, 0])
    temp = dev.read(129, 64)
    if temp[0] == 1:
        return 1
    if temp[0] == 0:
        return 0


def main_BV_EraseFlashBlock(BlockNum):
    main_ROMBankSwitch(BlockNum * 8)
    print('Erasing Block ' + str(BlockNum))
    dev.write(1, [10, 0, 6, 10, 170, 169, 5, 85, 86, 10, 170, 128, 10, 170, 169, 5, 85, 86, 64, 0, 48])
    USBbuffer = dev.read(129, 64)
    waitcount = 0
    while main_IsFlashBusy() == 1:
        waitcount += 1
        if waitcount == 100000:
            print('Error: ', BlockNum)
            exit()
            continue

    print('Done')


def main_ROMBankSwitch(bankNumber):
    bhi = bankNumber >> 8
    blo = bankNumber & 255
    if bhi > 0:
        dev.write(1, [10, 0, 1, 48, 0, bhi])
        USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 33, 0, blo])
    USBbuffer = dev.read(129, 64)


def main_MXROMBankSwitch(bankNumber):
    blo = bankNumber & 319
    dev.write(1, [10, 0, 1, 63, 0, blo])
    USBbuffer = dev.read(129, 64)


def main_RAMBankSwitch(bankNumber):
    print('Bank:' + str(bankNumber))
    blo = bankNumber & 255
    dev.write(1, [10, 0, 1, 64, 0, blo])
    USBbuffer = dev.read(129, 64)


def main_JPN_test():
    main_JPN_F2()
    main_JPN_F4()
    dev.write(1, [10, 0, 2, 1, 32, 1, 1, 63, 165])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 2, 1, 32, 2, 1, 63, 165])
    USBbuffer = dev.read(129, 64)
    main_JPN_F5(160)
    main_JPN_F5(96)
    main_JPN_F5(224)
    dev.write(1, [10, 0, 2, 1, 32, 2, 1, 63, 165])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 2, 1, 32, 2, 1, 63, 165])
    USBbuffer = dev.read(129, 64)
    for k in range(16):
        dev.write(1, [10, 0, 16, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85])
        USBbuffer = dev.read(129, 64)


def main_JPN_Unlock_ROM():
    main_JPN_F2()
    main_JPN_F4()
    main_JPN_F1(21845, 170)
    main_JPN_F1(10922, 85)
    main_JPN_F1(21845, 96)
    main_JPN_F1(21845, 170)
    main_JPN_F1(10922, 85)
    main_JPN_F1(0, 64)


def main_JPN_Burn_ROM():
    main_JPN_F2()
    main_JPN_F4()
    main_JPN_EraseFlash()
    main_LoadROM()
    addold = 0
    for address in range(0, ROMsize, 32):
        AddHi = address >> 16 & 255
        AddMe = address >> 8 & 255
        AddLo = address & 255
        Data32Bytes = ROMbuffer[address:address + 32]
        AddHi = AddHi.to_bytes(1, 'little')
        AddMe = AddMe.to_bytes(1, 'little')
        AddLo = AddLo.to_bytes(1, 'little')
        FlashWriteCommand = b'"' + AddHi + AddMe + AddLo
        Data32Bytes = ROMbuffer[address:address + 32]
        USBoutputPacket = FlashWriteCommand + Data32Bytes
        dev.write(1, USBoutputPacket)
        USBbuffer = dev.read(129, 64)
        trying = 0
        while main_JPN_Read(0) & 128 != 128:
            trying = trying + 1
            if trying == 100:
                print('Failed writing to sector', address)
                break

        if addold != address >> 13:
            print(address, 'bytes of', ROMsize)
        addold = address >> 13

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')
    main_JPN_F1(0, 240)
    main_JPN_F3()


def main_JPN_EraseFlash():
    main_JPN_F1(21845, 170)
    main_JPN_F1(10922, 85)
    main_JPN_F1(21845, 128)
    main_JPN_F1(21845, 170)
    main_JPN_F1(10922, 85)
    main_JPN_F1(21845, 16)
    while main_JPN_Read(0) != 128:
        pass


def main_JPN_F1(Address, Data):
    AddHi = Address >> 8
    AddLo = Address & 255
    dev.write(1, [10, 0, 5, 1, 32, 15, 1, 37, AddHi, 1, 38, AddLo, 1, 39, Data, 1, 63, 165])
    USBbuffer = dev.read(129, 64)


def main_JPN_F2():
    dev.write(1, [10, 0, 4, 1, 32, 9, 1, 33, 170, 1, 34, 85, 1, 63, 165])
    USBbuffer = dev.read(129, 64)


def main_JPN_F3():
    dev.write(1, [10, 0, 2, 1, 32, 8, 1, 63, 165])
    USBbuffer = dev.read(129, 64)


def main_JPN_F4():
    dev.write(1, [10, 0, 9, 1, 32, 10, 1, 37, 98, 1, 38, 4, 1, 39, 0, 1, 63, 165, 1, 32, 1, 1, 63, 165, 1, 32, 2, 1, 63, 165])
    USBbuffer = dev.read(129, 64)


def main_JPN_F5(inst):
    dev.write(1, [10, 0, 3, 1, 32, 16, 1, 63, 165, 1, 33, 1])
    USBbuffer = dev.read(129, 64)
    main_JPN_F1(21845, 170)
    main_JPN_F1(10922, 85)
    main_JPN_F1(21845, inst)


def main_JPN_F6(data):
    dev.write(1, [10, 0, 2, 1, 32, 192 & data, 1, 63, 165])
    USBbuffer = dev.read(129, 64)


def main_JPN_F7(inst):
    main_JPN_F1(17749, 170)
    main_JPN_F1(17066, 85)
    main_JPN_F1(17749, inst)


def main_JPN_Read(Address):
    AddHi = Address >> 8
    AddLo = Address & 255
    dev.write(1, [16, 0, 0, AddHi, AddLo])
    ROMbuffer = dev.read(129, 64)
    return ROMbuffer[0]


def JPN_Read(Address):
    AddHi = Address >> 8
    AddLo = Address & 255
    dev.write(1, [16, 0, 0, AddHi, AddLo])
    ROMbuffer = dev.read(129, 64)
    return ROMbuffer


def main_GBA_ReadHeader():
    dev.write(1, [48, 0, 0, 0, 64])
    USBbuffer = dev.read(129, 64)
    print(str(USBbuffer[32:44], 'utf-8'))
    app.ROMtitleLabel.set('ROM Title: ' + str(USBbuffer[32:44], 'utf-8'))
    app.MAPPERtypeLabel.set('GBA Cart: No Mapper')
    fsize = 256
    if main_GBA_GetByte(8388608) == (0, 0, 0, 0, 0, 0, 0, 0):
        fsize = 128
    if main_GBA_GetByte(4194304) == (0, 0, 0, 0, 0, 0, 0, 0):
        fsize = 64
    if main_GBA_GetByte(2097152) == (0, 0, 0, 0, 0, 0, 0, 0):
        fsize = 32
    if main_GBA_GetByte(1048576) == (0, 0, 0, 0, 0, 0, 0, 0):
        fsize = 16
    if main_GBA_GetByte(524288) == (0, 0, 0, 0, 0, 0, 0, 0):
        fsize = 8
    app.ROMsizeLabel.set('ROM Size: ' + str(fsize) + ' Mbits')
    print('Size Autodetected as', fsize, 'Mbits (not 100% accurate)')


def main_GBA_Dump_8():
    global ROMsize
    ROMsize = 1048576
    main_GBA_Dump()


def main_GBA_Dump_16():
    global ROMsize
    ROMsize = 2097152
    main_GBA_Dump()


def main_GBA_Dump_32():
    global ROMsize
    ROMsize = 4194304
    main_GBA_Dump()


def main_GBA_Dump_64():
    global ROMsize
    ROMsize = 8388608
    main_GBA_Dump()


def main_GBA_Dump_128():
    global ROMsize
    ROMsize = 16777216
    main_GBA_Dump()


def main_GBA_Dump_256():
    global ROMsize
    ROMsize = 33554432
    main_GBA_Dump()


def main_GBA_GetByte(Address):
    Lo = Address & 255
    Me = (Address & 65280) >> 8
    Hi = (Address & 16711680) >> 16
    dev.write(1, [48, 0, Hi, Me, Lo])
    ROMbuffer = dev.read(129, 64)
    return (
     ROMbuffer[0], ROMbuffer[1], ROMbuffer[2], ROMbuffer[3], ROMbuffer[4], ROMbuffer[5], ROMbuffer[6], ROMbuffer[7])


def main_GBA_GetByte(Address):
    Lo = Address & 255
    Me = (Address & 65280) >> 8
    Hi = (Address & 16711680) >> 16
    dev.write(1, [48, 0, Hi, Me, Lo])
    ROMbuffer = dev.read(129, 64)
    Tbuff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k = 0
    for t in range(1, 64, 2):
        Tbuff[k] = ROMbuffer[t] & 1
        k = k + 1

    return Tbuff


def main_GBA_EEPROM_Read(Address):
    Lo = Address & 255
    Me = (Address & 65280) >> 8
    Hi = (Address & 16711680) >> 16
    dev.write(1, [56, 0, Hi, Me, Lo])
    ROMbuffer = dev.read(129, 64)
    return ROMbuffer[0:8]


def main_GBA_EEPROM_Write(Address):
    Lo = Address & 255
    Me = (Address & 65280) >> 8
    Hi = (Address & 16711680) >> 16
    dev.write(1, [55, 0, Hi, Me, Lo, 0, 0, 0, 0, 0, 0, 0, 0])
    ROMbuffer = dev.read(129, 64)
    print('done')


def main_GBA_EEPROM_WriteFF(Address):
    Lo = Address & 255
    Me = (Address & 65280) >> 8
    Hi = (Address & 16711680) >> 16
    dev.write(1, [55, 0, Hi, Me, Lo, 255, 255, 255, 255, 255, 255, 255, 255])
    ROMbuffer = dev.read(129, 64)
    print('done')


def main_GBA_Dump():
    ROMfileName = asksaveasfilename(defaultextension='.GBA', filetypes=(('GBA ROM File', '*.GBA'),
                                                                        ('All Files', '*.*')))
    Hi2 = 0
    if ROMfileName:
        ROMfile = open(ROMfileName, 'wb')
        Address = 0
        for Address in range(0, int(ROMsize / 2), 32):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [48, 0, Hi, Me, Lo])
            ROMbuffer = dev.read(129, 64)
            ROMfile.write(ROMbuffer)
            if Hi2 != Hi:
                print(str(Address * 2) + ' Bytes of ' + str(ROMsize))
            Hi2 = Hi

        ROMfile.close()
        print('Done!')


def main_GBA_Flash_Erase():
    for sectors in range(0, 255):
        main_GBA_Sector_Erase(sectors)


def main_GBA_Sector_Erase(Sector):
    Shi = Sector >> 1
    Slo = Sector << 7
    Shi = Shi & 255
    Slo = Slo & 255
    dev.write(1, [49, 6, 0, 5, 85, 0, 169, 0, 2, 170, 0, 86, 0, 5, 85, 0, 128, 0, 5, 85, 0, 169, 0, 2, 170, 0, 86, Shi, Slo, 0, 0, 48])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [51])
    IFB = dev.read(129, 64)
    while IFB[0] == 1:
        dev.write(1, [51])
        IFB = dev.read(129, 64)

    print((Sector + 1) * 65536, 'Bytes Erased')


def main_GBA_Flash_ROM():
    if main_GBA_Read_CFI() == 1:
        main_LoadROM()
        Hi2 = 0
        secta = int(ROMsize / 65536) + 1
        for sectors in range(0, secta):
            main_GBA_Sector_Erase(sectors)

        for ROMaddress in range(0, ROMsize, 32):
            Address = int(ROMaddress / 2)
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            Data32Bytes = ROMbuffer[ROMaddress:ROMaddress + 32]
            Hi = Hi.to_bytes(1, 'little')
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            FlashWriteCommand = b'2' + Hi + Me + Lo + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            USBoutputPacket = FlashWriteCommand + Data32Bytes
            dev.write(1, USBoutputPacket)
            response = dev.read(129, 64)
            if Hi2 != Hi:
                print(ROMaddress, ' bytes of ', ROMsize, 'Written...')
                Hi2 = Hi
                continue

        print(ROMsize, ' Written!')
        messagebox.showinfo('Operation Complete', 'Writing Complete.')
        main_GBA_ReadHeader()


def main_GBA_Read_CFI():
    dev.write(1, [49, 1, 0, 0, 85, 0, 152])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [48, 0, 0, 0, 16])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [48, 0, 0, 0, 32])
    buffer = dev.read(129, 64)
    if ROMbuffer[0] == 82 and ROMbuffer[2] == 81 and ROMbuffer[4] == 90:
        print('CFI Present')
        print(2 << int(buffer[14] - 1), 'bytes capacity')
        dev.write(1, [49, 1, 0, 0, 0, 0, 240])
        buffer = dev.read(129, 64)
        return 1
    else:
        return 0


def main_GBA_Testcode():
    dev.write(1, [48, 0, 0, 0, 0])
    ROMbuffer = dev.read(129, 64)
    print(ROMbuffer)
    dev.write(1, [49, 2, 0, 0, 0, 0, 96, 0, 0, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [49, 2, 0, 0, 0, 0, 32, 0, 0, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [49, 2, 0, 0, 0, 2, 64, 0, 0, 0, 2, 0])
    ROMbuffer = dev.read(129, 64)
    dev.write(1, [48, 0, 0, 0, 0])
    ROMbuffer = dev.read(129, 64)
    print(ROMbuffer)


def main_GBA_Dump64kSRAM():
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GBA Save File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        Address = 0
        for Address in range(0, 65536, 64):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [53, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer)

        RAMfile.close()
        print('Done!')


def main_GBA_EEPROM_64k():
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GBA Save File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        Address = 0
        for Address in range(0, 1024):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [56, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer[0:8])

        RAMfile.close()
        print('Done!')


def main_GBA_EEPROM_4k():
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GBA Save File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        Address = 0
        for Address in range(0, 64):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [60, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer[0:8])

        RAMfile.close()
        print('Done!')


def main_GBA_Write64kEEPROM():
    SRAMfileName = askopenfilename(filetypes=(('GBA Save File', '*.SAV'), ('All Files', '*.*')))
    if SRAMfileName:
        SRAMfile = open(SRAMfileName, 'rb')
        SRAMbuffer = SRAMfile.read()
        SRAMsize = len(SRAMbuffer)
        for Address in range(0, 1024):
            Lo2 = Address & 255
            Me2 = (Address & 65280) >> 8
            Data8Bytes = SRAMbuffer[Address * 8:Address * 8 + 8]
            Me = Me2.to_bytes(1, 'little')
            Lo = Lo2.to_bytes(1, 'little')
            WriteCommand = b'7\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data8Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)
            for WriteDelay in range(0, 10):
                dev.write(1, [56, 0, 0, Me2, Lo2])

        SRAMfile.close()
        print('Done!')


def main_GBA_Write4kEEPROM():
    SRAMfileName = askopenfilename(filetypes=(('GBA Save File', '*.SAV'), ('All Files', '*.*')))
    if SRAMfileName:
        SRAMfile = open(SRAMfileName, 'rb')
        SRAMbuffer = SRAMfile.read()
        SRAMsize = len(SRAMbuffer)
        for Address in range(0, 64):
            Lo2 = Address & 255
            Me2 = (Address & 65280) >> 8
            Data8Bytes = SRAMbuffer[Address * 8:Address * 8 + 8]
            Me = Me2.to_bytes(1, 'little')
            Lo = Lo2.to_bytes(1, 'little')
            WriteCommand = b'=\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data8Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)
            for WriteDelay in range(0, 10):
                dev.write(1, [56, 0, 0, Me2, Lo2])

        SRAMfile.close()
        print('Done!')


def main_GBA_Dump64kFLASH():
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GBA Save File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        Address = 0
        dev.write(1, [57, 0, 0, 0, 0, 0])
        RAMbuffer = dev.read(129, 64)
        for Address in range(0, 65536, 64):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [53, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer)

        RAMfile.close()
        print('Done!')


def main_GBA_Dump128kFLASH():
    RAMfileName = asksaveasfilename(defaultextension='.SAV', filetypes=(('GBA Save File', '*.SAV'),
                                                                        ('All Files', '*.*')))
    if RAMfileName:
        RAMfile = open(RAMfileName, 'wb')
        Address = 0
        dev.write(1, [57, 0, 0, 0, 0, 0])
        RAMbuffer = dev.read(129, 64)
        for Address in range(0, 65536, 64):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [53, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer)

        dev.write(1, [57, 0, 0, 0, 0, 1])
        RAMbuffer = dev.read(129, 64)
        for Address in range(0, 65536, 64):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            dev.write(1, [53, 0, Hi, Me, Lo])
            RAMbuffer = dev.read(129, 64)
            RAMfile.write(RAMbuffer)

        RAMfile.close()
        print('Done!')


def main_GBA_FlashSaveErase():
    dev.write(1, [58, 0, 0, 0])
    RAMbuffer = dev.read(129, 64)
    dev.write(1, [53, 0, 0, 0, 0])
    RAMbuffer = dev.read(129, 64)
    while RAMbuffer[0] != 255:
        dev.write(1, [53, 0, 0, 0, 0])
        RAMbuffer = dev.read(129, 64)

    print('FlashSave Erased')


def main_GBA_Write64kSRAM():
    SRAMfileName = askopenfilename(filetypes=(('GBA Save File', '*.SAV'), ('All Files', '*.*')))
    if SRAMfileName:
        SRAMfile = open(SRAMfileName, 'rb')
        SRAMbuffer = SRAMfile.read()
        SRAMsize = len(SRAMbuffer)
        for Address in range(0, SRAMsize, 32):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Data32Bytes = SRAMbuffer[Address:Address + 32]
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            WriteCommand = b'6\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data32Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)

        SRAMfile.close()
        print('Done!')


def main_GBA_Write128kFLASHRAM():
    SRAMfileName = askopenfilename(filetypes=(('GBA Save File', '*.SAV'), ('All Files', '*.*')))
    if SRAMfileName:
        main_GBA_FlashSaveErase()
        SRAMfile = open(SRAMfileName, 'rb')
        SRAMbuffer = SRAMfile.read()
        SRAMsize = len(SRAMbuffer)
        dev.write(1, [57, 0, 0, 0, 0, 0])
        RAMbuffer = dev.read(129, 64)
        for Address in range(0, 65535, 32):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Data32Bytes = SRAMbuffer[Address:Address + 32]
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            WriteCommand = b';\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data32Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)

        dev.write(1, [57, 0, 0, 0, 0, 1])
        RAMbuffer = dev.read(129, 64)
        for Address in range(65536, 131071, 32):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Data32Bytes = SRAMbuffer[Address:Address + 32]
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            WriteCommand = b';\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data32Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)

        SRAMfile.close()
        print('Done!')


def main_GBA_Write64kFLASHRAM():
    SRAMfileName = askopenfilename(filetypes=(('GBA Save File', '*.SAV'), ('All Files', '*.*')))
    if SRAMfileName:
        main_GBA_FlashSaveErase()
        SRAMfile = open(SRAMfileName, 'rb')
        SRAMbuffer = SRAMfile.read()
        SRAMsize = len(SRAMbuffer)
        dev.write(1, [57, 0, 0, 0, 0, 0])
        RAMbuffer = dev.read(129, 64)
        for Address in range(0, SRAMsize, 32):
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Data32Bytes = SRAMbuffer[Address:Address + 32]
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            WriteCommand = b';\x00\x00' + Me + Lo
            Dataout = WriteCommand + Data32Bytes
            dev.write(1, Dataout)
            RAMbuffer = dev.read(129, 64)

        SRAMfile.close()
        print('Done!')


def main_BV5_Erase():
    print('Erasing...')
    dev.write(1, [10, 1, 6, 10, 170, 169, 5, 85, 86, 10, 170, 128, 10, 170, 169, 5, 85, 86, 10, 170, 16])
    RAMbuffer = dev.read(129, 64)
    while main_ELCheapo_Read(0)[0] != 255:
        print(main_ELCheapo_Read(0))

    print('Erased')


def main_BV5_Write():
    main_LoadROM()
    print('Writing ROM Data')
    main_BV5_Erase()
    ROMpos = 0
    waitcount = 0
    for BankNumber in range(0, int(ROMsize / 16384)):
        main_ROMBankSwitch(BankNumber)
        print(BankNumber * 16384, ' of ', ROMsize)
        for ROMAddress in range(16384, 32768, 32):
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data32Bytes = ROMbuffer[ROMpos:ROMpos + 32]
            AddHi = AddHi.to_bytes(1, 'little')
            AddLo = AddLo.to_bytes(1, 'little')
            FlashWriteCommand = b"'\x00" + AddHi + AddLo
            USBoutputPacket = FlashWriteCommand + Data32Bytes
            dev.write(1, USBoutputPacket)
            USBbuffer = dev.read(129, 64)
            ROMpos += 32

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')
    main_ROMBankSwitch(0)


def main_ELCheapo_Erase():
    print('Erasing...')
    dev.write(1, [10, 1, 6, 10, 170, 170, 5, 85, 85, 10, 170, 128, 10, 170, 170, 5, 85, 85, 10, 170, 16])
    RAMbuffer = dev.read(129, 64)
    while main_ELCheapo_Read(0)[0] != 255:
        pass

    print('Erased')


def main_ELCheapo_Read(Address):
    AddHi = Address >> 8
    AddLo = Address & 255
    dev.write(1, [16, 0, 0, AddHi, AddLo])
    ROMbuffer = dev.read(129, 64)
    return ROMbuffer


def main_ELCheapo_Write():
    main_LoadROM()
    print('Writing ROM Data')
    main_ELCheapo_Erase()
    ROMpos = 0
    waitcount = 0
    for BankNumber in range(0, int(ROMsize / 16384)):
        main_ROMBankSwitch(BankNumber)
        print(BankNumber * 16384, ' of ', ROMsize)
        for ROMAddress in range(16384, 32768, 32):
            if BankNumber == 0:
                ROMAddress = ROMAddress - 16384
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data32Bytes = ROMbuffer[ROMpos:ROMpos + 32]
            AddHi = AddHi.to_bytes(1, 'little')
            AddLo = AddLo.to_bytes(1, 'little')
            FlashWriteCommand = b'$\x00' + AddHi + AddLo
            USBoutputPacket = FlashWriteCommand + Data32Bytes
            dev.write(1, USBoutputPacket)
            USBbuffer = dev.read(129, 64)
            ROMpos += 32

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')
    main_ROMBankSwitch(0)


def main_ELCheapoSD_Erase():
    print('Erasing...')
    dev.write(1, [10, 0, 1, 0, 0, 5])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 6, 10, 170, 170, 5, 85, 85, 10, 170, 128, 10, 170, 170, 5, 85, 85, 10, 170, 16])
    RAMbuffer = dev.read(129, 64)
    while main_ELCheapo_Read(0)[0] != 255:
        print(main_ELCheapo_Read(0))

    print('Erased')


def main_ELCheapoSD_Read(Address):
    AddHi = Address >> 8
    AddLo = Address & 255
    dev.write(1, [16, 0, 0, AddHi, AddLo])
    ROMbuffer = dev.read(129, 64)
    return ROMbuffer


def main_ELCheapoSD_Write():
    main_LoadROM()
    print('Writing ROM Data')
    print('Erasing...')
    dev.write(1, [10, 0, 1, 0, 0, 5])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 6, 10, 170, 170, 5, 85, 85, 10, 170, 128, 10, 170, 170, 5, 85, 85, 0, 0, 48])
    RAMbuffer = dev.read(129, 64)
    while main_ELCheapo_Read(0)[0] != 255:
        pass

    print('Erased')
    ROMpos = 0
    waitcount = 0
    for BankNumber in range(0, int(ROMsize / 16384)):
        print(main_ELCheapo_Read(16384))
        main_ROMBankSwitch(BankNumber)
        print(main_ELCheapo_Read(16384))
        print(BankNumber, BankNumber * 16384, ' of ', ROMsize)
        for ROMAddress in range(16384, 32768, 32):
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data32Bytes = ROMbuffer[ROMpos:ROMpos + 32]
            AddHi = AddHi.to_bytes(1, 'little')
            AddLo = AddLo.to_bytes(1, 'little')
            FlashWriteCommand = b'%\x00' + AddHi + AddLo
            USBoutputPacket = FlashWriteCommand + Data32Bytes
            dev.write(1, USBoutputPacket)
            USBbuffer = dev.read(129, 64)
            ROMpos += 32

    app.lowerLeftLabel.set(str(ROMsize) + ' Bytes Written')
    messagebox.showinfo('Operation Complete', 'Writing Complete.')
    main_ROMBankSwitch(0)


def SD_Init():
    dev.write(1, [10, 0, 1, 0, 0, 5])
    USBbuffer = dev.read(129, 64)
    for init in range(0, 10):
        dev.write(1, [10, 0, 1, 48, 0, 255])
        USBbuffer = dev.read(129, 64)
        dev.write(1, [10, 0, 1, 16, 0, 3])
        USBbuffer = dev.read(129, 64)

    dev.write(1, [10, 0, 1, 48, 0, 64])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 48, 0, 0])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 48, 0, 0])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 48, 0, 0])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 48, 0, 0])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 48, 0, 149])
    USBbuffer = dev.read(129, 64)
    dev.write(1, [10, 0, 1, 16, 0, 1])
    USBbuffer = dev.read(129, 64)
    for wait in range(0, 4):
        dev.write(1, [10, 0, 1, 48, 0, 255])
        USBbuffer = dev.read(129, 64)
        dev.write(1, [10, 0, 1, 16, 0, 1])
        USBbuffer = dev.read(129, 64)
        print(main_ELCheapoSD_Read(12288))


def main_GSWrite():
    dev.write(1, [10, 0, 6, 85, 85, 170, 42, 170, 85, 85, 85, 128, 85, 85, 170, 42, 170, 85, 85, 85, 16])
    tmp = dev.read(129, 64)
    main_LoadROM()
    print('Writing ROM Data')
    ROMpos = 0
    waitcount = 0
    dev.write(1, [10, 0, 1, 64, 0, 1])
    tmp = dev.read(129, 64)
    print('Bank set')
    for ROMAddress in range(0, 4096):
        AddHi = ROMAddress >> 8
        AddLo = ROMAddress & 255
        DataByte = ROMbuffer[ROMAddress]
        AddHi = AddHi.to_bytes(1, 'little')
        AddLo = AddLo.to_bytes(1, 'little')
        DataByte = DataByte.to_bytes(1, 'little')
        FlashWriteCommand = b'\n\x00\x04UU\xaa**UUU\xa0' + AddHi + AddLo + DataByte
        USBoutputPacket = FlashWriteCommand
        dev.write(1, USBoutputPacket)
        USBbuffer = dev.read(129, 64)


def main_Catskull_erase():
    print('Erasing...')
    dev.write(1, [10, 1, 6, 85, 85, 170, 42, 170, 85, 85, 85, 128, 85, 85, 170, 42, 170, 85, 85, 85, 16])
    RAMbuffer = dev.read(129, 64)
    while main_ELCheapo_Read(0)[0] != 255:
        pass

    print('Erased')


def main_Catskull_write():
    if main_LoadROM() == 1:
        main_Catskull_erase()
        print('Writing ROM Data')
        ROMpos = 0
        for ROMAddress in range(0, 32768, 1):
            AddHi = ROMAddress >> 8
            AddLo = ROMAddress & 255
            Data1Byte = ROMbuffer[ROMpos:ROMpos + 1]
            dev.write(1, [10, 1, 4, 85, 85, 170, 42, 170, 85, 85, 85, 160, AddHi, AddLo, Data1Byte[0]])
            ROMpos += 1

        messagebox.showinfo('Operation Complete', 'Writing Complete.')


def SDID_Read():
    dev.write(1, [128])
    USBbuffer = dev.read(129, 64)
    A = USBbuffer[0] + (USBbuffer[1] << 8) + (USBbuffer[2] << 16) + (USBbuffer[3] << 24)
    B = USBbuffer[4] + (USBbuffer[5] << 8) + (USBbuffer[6] << 16) + (USBbuffer[7] << 24)
    C = USBbuffer[8] + (USBbuffer[9] << 8) + (USBbuffer[10] << 16) + (USBbuffer[11] << 24)
    D = str(hex(A)) + ',' + str(hex(B)) + ',' + str(hex(C))
    return D


def main_SendKey():
    myText = simpledialog.askstring('Update', 'Enter Device Key:')
    if all((c in string.hexdigits for c in myText)) == False or len(myText) != 8:
        messagebox.showinfo('Error', 'One or more characters are invalid')
    else:
        Key = myText[0:8]
        B1 = int(Key[0:2], 16)
        B2 = int(Key[2:4], 16)
        B3 = int(Key[4:6], 16)
        B4 = int(Key[6:8], 16)
        B1 = B1.to_bytes(1, 'little')
        B2 = B2.to_bytes(1, 'little')
        B3 = B3.to_bytes(1, 'little')
        B4 = B4.to_bytes(1, 'little')
        WriteCommand = b'\x81' + B1 + B2 + B3 + B4
        dev.write(1, WriteCommand)
        USBbuffer = dev.read(129, 64)
        A = Get_Key_State()
        if A == 0:
            messagebox.showinfo('Error', 'Key not a match to Hardware ID')
    if A == 1:
        messagebox.showinfo('Success', 'Firmware Update Enabled')


def Get_Key_State():
    dev.write(1, [132])
    USBbuffer = dev.read(129, 64)
    return USBbuffer[0]


def SDID_Set():
    dev.write(1, [129, 240, 24, 96, 231])
    USBbuffer = dev.read(129, 64)


def SDID_Readback():
    dev.write(1, [130])
    USBbuffer = dev.read(129, 64)
    A = USBbuffer[0] + (USBbuffer[1] << 8) + (USBbuffer[2] << 16) + (USBbuffer[3] << 24)
    print(hex(A))


def GBA_DualDecord_Unlock_All_Blocks():
    dev.write(1, [49, 2, 0, 64, 0, 0, 96, 0, 64, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    dev.write(1, [49, 2, 0, 128, 0, 0, 96, 0, 128, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    dev.write(1, [49, 2, 0, 192, 0, 0, 96, 0, 192, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    for ROMaddress in range(0, 33554431, 131072):
        Address = int(ROMaddress / 2)
        Lo = Address & 255
        Me = (Address & 65280) >> 8
        Hi = (Address & 16711680) >> 16
        Data32Bytes = ROMbuffer[ROMaddress:ROMaddress + 32]
        Hi = Hi.to_bytes(1, 'little')
        Me = Me.to_bytes(1, 'little')
        Lo = Lo.to_bytes(1, 'little')
        FlashWriteCommand = b'1\x02' + Hi + Me + Lo + b'\x00`' + Hi + Me + Lo + b'\x00\xd0'
        dev.write(1, FlashWriteCommand)


def main_GBA_Sector_Erase_DD(Sector):
    Shi = Sector
    Shi = Shi & 255
    dev.write(1, [49, 2, Shi, 0, 0, 0, 32, Shi, 0, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    print((Sector + 1) * 131072, 'Bytes Erased')


def main_GBA_SectorFragment_Erase_DD():
    dev.write(1, [49, 2, 0, 64, 0, 0, 32, 0, 64, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    dev.write(1, [49, 2, 0, 128, 0, 0, 32, 0, 128, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128

    dev.write(1, [49, 2, 0, 192, 0, 0, 32, 0, 192, 0, 0, 208])
    ROMbuffer = dev.read(129, 64)
    A = 0
    while A != 128:
        dev.write(1, [48, 0, 0, 0, 0])
        A = dev.read(129, 64)
        A = A[0]
        A = A & 128


def main_GBA_Flash_ROM_DD():
    global ROMbuffer
    if main_GBA_Read_CFI() == 1:
        main_LoadROM()
        Hi2 = 0
        GBA_DualDecord_Unlock_All_Blocks()
        secta = int(ROMsize / 131072) + 1
        main_GBA_SectorFragment_Erase_DD()
        for sectors in range(0, secta):
            main_GBA_Sector_Erase_DD(sectors)

        for ROMaddress in range(0, ROMsize, 32):
            Address = int(ROMaddress / 2)
            Lo = Address & 255
            Me = (Address & 65280) >> 8
            Hi = (Address & 16711680) >> 16
            Data64Bytes = ROMbuffer[ROMaddress:ROMaddress + 32]
            Hi = Hi.to_bytes(1, 'little')
            Me = Me.to_bytes(1, 'little')
            Lo = Lo.to_bytes(1, 'little')
            FlashWriteCommand = b'>' + Hi + Me + Lo + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            USBoutputPacket = FlashWriteCommand + Data64Bytes
            dev.write(1, USBoutputPacket)
            response = dev.read(129, 64)
            if Hi2 != Hi:
                print(ROMaddress, ' bytes of ', ROMsize, 'Written...')
                Hi2 = Hi
                continue

        print(ROMsize, ' Written!')
        messagebox.showinfo('Operation Complete', 'Writing Complete.')
        dev.write(1, [49, 1, 0, 0, 0, 0, 255])
        ROMbuffer = dev.read(129, 64)
        main_GBA_ReadHeader()


root = Tk()
root.geometry('400x300')
app = Window(root)
dev = usb.core.find(idVendor=1133, idProduct=4660)
if dev is None:
    messagebox.showinfo('USB Error', 'I Cant find your hardware! Check the device is plugged in and the USB driver is installed')
    exit()
if dev is not None:
    dev.set_configuration()
    messagebox.showinfo('Welcome', 'Gen3 is a work in progress, please report any bugs or requests to Bennvenn@hotmail.com')
    main_CheckVersion()
    root.mainloop()