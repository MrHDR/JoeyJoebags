# JoeyJoebags
Custom version of the Joey software.


## Current Additions

- Fixes dumping 32MB repros like the DV15 & PPP08

- Dumping / Flashing completion percentage

- Progress is now shown on a single line

- Removed dotted lines at the top of all menu entries

- A digitally signed driver

# Installing the driver

Unzip the "JoeyJoebags_Signed_Driver.zip" file and right click "Install Driver.bat" and run is as an admin, no reboots or disabling driver signature enforecement needed.

# Compiling/Decompiling Windows Binaries

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