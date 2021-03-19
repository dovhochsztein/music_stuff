import os
from typing import NamedTuple
import platform


class PathwaySettings(NamedTuple):
    TEMP_DIR: str


SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = SETTINGS_DIR

WINDOWS_SETTINGS = PathwaySettings(
    TEMP_DIR=os.path.join(SETTINGS_DIR, 'temp')
)
MAC_SETTINGS = PathwaySettings(
    TEMP_DIR=os.path.join(SETTINGS_DIR, 'temp')
)
LINUX_SETTINGS = PathwaySettings(
    TEMP_DIR=os.path.join(SETTINGS_DIR, 'temp')
)


if platform.system() == 'Windows':
    SETTINGS = WINDOWS_SETTINGS
elif platform.system() == 'Darwin':
    SETTINGS = MAC_SETTINGS
else:
    SETTINGS = LINUX_SETTINGS

if os.name == 'nt':
    for folder in SETTINGS:
        if not os.path.exists(folder):
            os.makedirs(folder)







if os.name == 'nt':
    for folder in SETTINGS:
        if not os.path.exists(folder):
            os.makedirs(folder)
