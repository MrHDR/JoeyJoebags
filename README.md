# JoeyJoebags
Custom version of the Joey software.
### Firmware Flashing

**Required Software:**
- [JoeyFirmwareTool](https://github.com/HDR/JoeyJoebags/releases)
- [stm32flash](https://sourceforge.net/projects/stm32flash/)

**Required Tools:**
- CP2102 (or any other device that can be used for flashing)

#### Maple Mini

I use a CP2102 for this, but other flashing tools should work.

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



#### STM32F103C8T6

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
