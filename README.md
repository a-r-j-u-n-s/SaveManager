# SaveGame
_A save manager for PC games_

## _About_
This CLI allows you to manage your save folders for PC games. It is written entirely in Python.

Primary features:
- _Create multiple labeled backups of your savegame with custom names/descriptions for reference_
- _Create/restore from a temporary unlabeled backup save_
- _Add/delete your custom saves easily_

## _Usage_

1. `git clone` or download this repository
2. (Optional but recommended) Create a [virtual environment](https://docs.python.org/3/library/venv.html) in the directory 
3. Install dependencies
   ```
   python -m setup install
   ```
4. Script is ready for use!
   1. Verify by seeing if `savegame-manager` appears when you run `pip list`

#### Optional flags

`-l`: display all your current saves

`-c`: indicate that you want to script to use your custom savegame location (i.e. not its default installed location)

**There are _three_ primary modes for this script to run in:**

### load
```
savegame [-l] [-c] load [-b] [savename]
```

- For when you want to replace the current save file with one of your saved backups

_Optional_:

`-b, --backup`  : restore your temporary backup save

`savename`: the name of the save you want to restore. Leave blank to be prompted after seeing the current list of saves

### save
```
savegame [-l] [-c] save [-b] [savename]
```

- For when you want to save your current savegame in a new backup

_Optional_:

`-b, --backup`  : store your current savegame as a temporary backup that you can easily restore from

`savename`: the name of your custom save. Leave blank to be prompted after seeing the current list of saves

### remove
```
savegame [-l] [-c] remove [savenames...]
```

- For when you want to delete one or more of your backups

_Optional_:

`savenames`: a list of your custom saves to delete. Leave blank to choose which save to delete after seeing the list

## Dependencies

* **This program is is only supported for Windows 10**

[Python 3.8](https://www.python.org/downloads/release/python-380/)

[psutil 5.7.0](https://pypi.org/project/psutil/)

[setuptools 57.0.0](https://pypi.org/project/setuptools/)

## _Current Tasks_
Version: 1.0
- Configure script to work with multiple games!
- Publish on [PyPi](https://pypi.org/)


### Disclaimer
Although this CLI does create automatic backups of your save file before performing any actions, you should still
back up your original save folder just once before using the script
