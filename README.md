# Group photos by date
Copy photos of the same day in a folder


## Getting started
1. Make sure to install [ExifTool](https://exiftool.org/)
2. Create virtual environment
```bash
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip3 install requirements.txt
```

## Run script
1. Move your media files to the directory `files`
2. Open the virtual environment
```bash
source venv/bin/activate
```
3. Run the script
```bash
python3 files/group-by-date.py
```
4. Your media files have been moved from `files` to `files/by-date/2020-01-23` for example.


## License
All files are licensed under the BSD license. See the LICENSE file for details.
Copyright 2020		Tjibbe van der Laan