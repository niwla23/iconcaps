# 91 Icon Keycaps mostly based on fontawesome + generator script

https://www.printables.com/model/395815-91-icon-keycaps

Switch Type: Cherry MX

Sources:

- all brand icons are taken from the website of the respective website (example OBS, firefox) OR from fontawesome free brand font.
- Most icons are from Fontawesome free: https://fontawesome.com/ License: https://creativecommons.org/licenses/by/4.0/
- Self-designed: light caps (modified from FA), RGB, Circle, Triangle, Play, extrude)
 

Blank keycap source: https://www.thingiverse.com/thing:738769 (V2 keycap has been completly remodelled but has the same style as the linked one.)

The files have been created by a python script and are based on a better model for the keycap I made.
Every icon is **centered and scaled automatically**. Please tell me if you find any broken icons or would like to see another icon as a keycap.

## Script Usage
- Install poetry: https://python-poetry.org/docs/#installation
- Create a poetry env with python 3.10: `poetry env use 3.10` (bpy was refusing to install with other versions I think)
- Install dependencies: `poetry install`
- Put your files in the `svgs` folder
- Run the script: `python3.10 main.py`
- your keycaps will be in the `target` folder
