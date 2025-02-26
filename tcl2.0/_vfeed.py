from time import sleep
from ims import ims 
from sys import argv 
import os
def find_latest_fits(root_dir: str) -> str:
    """Find the most recently written FITS file in a directory and its subdirectories."""
    latest_file = None
    latest_mtime = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".fits"):
                filepath = os.path.join(dirpath, filename)
                try:
                    mtime = os.stat(filepath).st_mtime  # Get modification time
                    if mtime > latest_mtime:
                        latest_mtime = mtime
                        latest_file = filepath
                except OSError:
                    continue  # Skip files that cause errors

    return latest_file

if '__main__' in __name__:
    path = argv[1] 
    lfits_old = ""
    ims = ims()
    while True:
        sleep(0.5)
        lfits = find_latest_fits(path)
        if lfits == None:
            sleep(0.5)
        if lfits!=None and lfits!=lfits_old and lfits!="":
            sleep(0.08)
            ims.sendImageSimple(lfits)
            lfits_old = lfits

