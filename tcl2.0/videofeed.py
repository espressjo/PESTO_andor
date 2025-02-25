import os
from time import sleep 

import subprocess
environment = os.environ.copy()
if "PYTHONPATH" in environment:
    environment["PYTHONPATH"]+=":/opt/ims/python"
else:
    environment["PYTHONPATH"] = "/opt/ims/python"
class andorfeed:
    def __init__(self):
        self.process = None 
    
    @property
    def running(self):
        if self.process == None:
            return False
        return True if self.process.poll() == None else False 
    def launch(self,path):
        if not os.path.isdir(path):
            raise Exception("path does not exist")
            return False
        if self.running:
            raise Exception("video feed is already started")
            return False
        self.process = subprocess.Popen(["python","_vfeed.py",path],env=environment)
        return True
    def kill(self):
        if self.process != None:
            self.process.kill()
        self.process = None

