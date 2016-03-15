from distutils.core import setup
# noinspection PyUnresolvedReferences
import py2exe
import pytz
import os
import zipfile

setup(console=["nightshift_cmd.py", "nightshift_setup.py"], windows=["nightshift.py"],
      requires=['py2exe', "pytz", "pillow", "astral", "tzlocal"])

zipfile_path = os.path.join("dist", "library.zip")
z = zipfile.ZipFile(zipfile_path, 'a')
zoneinfo_dir = os.path.join(os.path.dirname(pytz.__file__), "zoneinfo")
disk_basedir = os.path.dirname(os.path.dirname(pytz.__file__))
for absdir, directories, filenames in os.walk(zoneinfo_dir):
    assert absdir.startswith(disk_basedir), (absdir, disk_basedir)
    zip_dir = absdir[len(disk_basedir):]
    for f in filenames:
        z.write(os.path.join(absdir, f), os.path.join(zip_dir, f))

z.close()
