from os import popen
from os.path import join 
from pytcl import pytcl
from get_inc import get_inc
from racine import racine 
IP = "132.204.61.46"
port_main = 5002
port_abort = 5003

class andor(pytcl):
    def __init__(self,IP,port=port_main,alternateP=port_abort):
        pytcl.__init__(self,IP,port_main,port_abort)
        self.expTime = 1
        self.nbImage = 1 
        self.type = 'Video'
        self.mode = 'conventional'
        self.basePath = "video"
        self.type_list = {'Target','Video','Flat','Dark','Bias'}
        self.objName = "test"
        self.basename = self.objName
        self.local_path = "/home/pesto/data_andor"
    def __str__(self):
        txt="Andor Camera Parameters\n"
        txt+="----------------------\n"
        txt+=f"Type: {self.type}\n"
        txt+=f"Image requested: {self.nbImage}\n"
        txt+=f"Integration (s): {self.expTime}\n"
        txt+=f"Obj. Name: {self.objName}\n"
        txt+=f"Mode: {self.mode}\n"
        return txt
    def make_folder(self):
        _p = join(racine(),self.type)
        if 'Target' in self.type:
            _p = join(_p,self.objName) 
        return _p
    def setExpTime(self,exp):
        self.expTime = exp
    def set_nb_images(self,nb):
        self.nbImage = nb 
    def target(self,type):
        if type not in self.type_list:
            raise ValueError("Invalid type")
        self.type = type
    def testAudeLa(self,txt):
        return self.rcmd('console::affiche_resultat "%s"'%txt)
    def initialisation(self):
        return self.rcmd("cam1 electronic 1 0 1 2 0 1") 
    def acquisition(self):
        #acquisition $nbimages $increment $expt $path $basename
        path = self.make_folder()
        #make sure TCL is happy
        if path[0] !='/':
            path = "/"+path 
        if path[-1]!='/':
            path = path +"/" 
        #:::::::::::::::::::::::
        i = get_inc(join(self.local_path,racine()))
        if i < 0 :
            i=1

        self.rcmd(f"acquisition {self.nbImage} {i} {self.expTime} {path} {self.basename}")
    def abort(self):
        #open a server connection for the abort thread
        return self.rcmd("set_abort_flag",True)

if '__main__' in __name__:
    with andor(IP) as _andor:
        print("testing script running...")
        _andor.initialisation()
        print(_andor)
        _andor.acquisition()
        print("sleeping 2 seconds")
        sleep(10)
        