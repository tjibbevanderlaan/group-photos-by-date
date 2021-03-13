import exiftool
from os import listdir
from os.path import isfile, join
from datetime import datetime
from pathlib import Path
import shutil

sourcedirname = "files"
destdirname = "by-date"


files = [f for f in listdir() if isfile(f)]
files.remove('group-by-date.py')

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)
for d in metadata:
	date_str = d["EXIF:DateTimeOriginal"]
	date = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
	dirname = date.strftime("%Y-%m-%d")
	destdir = Path(destdirname, dirname)

	# create dirstructure
	Path(destdir).mkdir(parents=True, exist_ok=True)
	# move file
	sourcepath = d["SourceFile"]
	destpath = Path(destdir, d["SourceFile"])
	shutil.move(sourcepath, destpath)
