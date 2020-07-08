# JoeyJoebags
Tools, firmware and software for the JoeyJoebags

**Please note that this section is to help users fix broken devices, no support will be provided beyond this readme**

### Firmware Flashing

#### Software Flashing (Arduino ide)

**Required Software:**
- [Arduino IDE](https://www.arduino.cc/en/main/software)
- [Arduino_STM32](https://github.com/rogerclarkmelbourne/Arduino_STM32/wiki/Installation)

**Flashing the firmware:**
1. Open "JoeyBootloader.ino" in the Arduino IDE
2. Connect the maple mini over usb
3. Under "Tools" select the following options:
```
Board: "Maple Mini"
Bootloader version: "Original (17k RAM, 108k Flash)"
CPU Speed(MHz): "48MHz (Slow - with USB)"
Optimize: "Smallest (default)"
Port: COM# (Maple Mini)" ##Where # is the COM number of your device
```

4. Click Upload and open the serial monitor
5. That's it, you're done

[Video Guide](https://www.youtube.com/watch?v=m3snxbclFE0)

#### Hardware Flashing (If the maple mini does not have the default bootloader)

**Required Software:**
- [JoeyFirmwareTool](https://github.com/HDR/JoeyJoebags/releases)
- [stm32flash](https://sourceforge.net/projects/stm32flash/)

**Required Tools:**
- CP2102 (or any other device that can be used for flashing)

#### Maple Mini

**Pinout:**

| Maple Mini | CP2102 |
|------------|------------|
| GND | GND |
| 25(RX1) | TXD |
| 26(TX1) | RXD |
| VIN | 5V |

| Maple Mini | Maple Mini |
|------------|------------|
| VCC | BUT(boot0) |
| GND | boot1 |

Connect everything according to the above pinout (boot1 and boot0 are not needed if you set the maple mini to flash mode using the buttons) 

**Flashing the firmware:**
1. Drop a .ben file onto "JoeyFirmwareTool.exe", this will produce a file called "JoeyFirmware.bin"
2. Find out what com port your flashing tool is (for this example i will be using COM8)
3. open commandline and navigate to your stm32flash folder
4. run `stm32flash -w JoeyFirmware.bin -v -g 0x0 COM8` and your maple mini will be flashed.
5. That's it, you're done!

#### STM32F103C8T6

**Pinout:**

| STM32F103C8T6 | CP2102 |
|------------|------------|
| Pin 31 | GND |
| Pin 43 | TXD |
| Pin 42 | RXD |
| Pin 32 | 3.3V |
| Pin 61 | 3.3V |
| Pin 28 | GND |

**Flashing the firmware:**
1. Drop a .ben file onto "JoeyFirmwareTool.exe", this will produce a file called "JoeyFirmware.bin"
2. Find out what com port your flashing tool is (for this example i will be using COM8)
3. open commandline and navigate to your stm32flash folder
4. run `stm32flash -w JoeyFirmware.bin -v -g 0x0 COM8` and your STM32F103C8T6 will be flashed.
5. That's it, you're done!

# Custom Signed Driver

Unzip the "JoeyJoebags_Signed_Driver.zip" file and right click "Install Driver.bat" and run is as an admin, no reboots or disabling driver signature enforecement needed.

# Compiling/Decompiling Windows Software Binaries

### Compiling
Run ```python -m py2exe JoeyJoebags.py``` to compile windows binaries

Alternatively you can use this script
```
from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

setup(
        options = {
                    'py2exe': {'bundle_files': 2,
                               'compressed': True
                              }
                  },
        console = [{
                    'script': "JoeyJoebags.py",
					'icon_resources': [(0, 'favicon.ico')]
                  }],
        zipfile = None,
)
```

### Requirements
```
Python 3.4
PyUSB
py2exe
```

### Installing Requirements
1. Download & Install Python 3.4 64bit from https://www.python.org/downloads/windows/
2. open cmd as admin and type ```python -m pip install PyUSB``` & ```python -m pip install py2exe```

### Decompiling
To decompile the binary you will need python_exe_unpack.py from https://github.com/countercept/python-exe-unpacker just follow the instructions in the readme, to decompile the exe use ```python python_exe_unpack.py -i JoeyJoebags.exe```

If you experience any issues with installing PyCrypto for the decompiler, install this https://github.com/axper/python3-pycrypto-windows-installer

### Requirements
```
Python 3.4
pefile
unpy2exe
uncompyle6
xdis
pycrypto
configparser
```

### Installing Requirements
1. Download & Install Python 3.4 64bit from https://www.python.org/downloads/windows/
2. Download https://github.com/countercept/python-exe-unpacker
3. open cmd as admin in the python-exe-unpacker folder and type ```python -m pip install -r requirements.txt```

## Custom Software Additions

- Fixes dumping 32MB repros like the DV15 & PPP08

- Dumping / Flashing completion percentage

- Progress is now shown on a single line

- Removed dotted lines at the top of all menu entries
