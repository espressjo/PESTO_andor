from os import popen
from os.path import join 
from pytcl import pytcl
from get_inc import get_inc
from racine import racine
from videofeed import andorfeed
IP = "132.204.61.46"
port_main = 5002
port_abort = 5003
LOCALPATH = "/home/andor"

class andor(pytcl,andorfeed):
    def __init__(self,IP,port=port_main,alternateP=port_abort):
        pytcl.__init__(self,IP,port_main,port_abort)
        andorfeed.__init__(self)
        self.expTime = 1
        self.nbImage = 1 
        self.type = 'Video'
        self.mode = 'conventional'
        self.basePath = "video"
        self.type_list = {'Target','Video','Flat','Dark','Bias'}
        self.feed = andorfeed()
        self.basename = "test"
        self.local_path = LOCALPATH
        self.head_dict = {}
        self.relaunchfeed()
    def relaunchfeed(self):
        if self.running:
            self.kill()

        P = join(self.local_path,racine())
        self.launch(P)

    def increment_verification(self):
        _night = racine()
        print("[debug] ",_night)
        tcl_night = self.rcmd("get_night")
        print("[debug] ",tcl_night)
        if _night not in tcl_night:
            print("TCL night not difined")
            print(self.rcmd(f'set_night "{_night}"'))
            i = get_inc(join(self.local_path,_night))
            print("[debug] ",i)
            print(self.rcmd(f'set_increment {i}'))
 
    def __str__(self):
        txt="Andor Camera Parameters\n"
        txt+="----------------------\n"
        txt+=f"Type: {self.type}\n"
        txt+=f"Image requested: {self.nbImage}\n"
        txt+=f"Integration (s): {self.expTime}\n"
        txt+=f"Obj. Name: {self.basename}\n"
        txt+=f"Mode: {self.mode}\n"
        return txt
    def value_type(self,value):
        if isinstance(value,int):
            return "int"
        elif isinstance(value,float):
            return "float"
        else :
            return "string"
    def u_header(self,keywd,value):
        if keywd not in self.head_dict:
            raise ValueError("Invalid keyword")
            return 
        self.rcmd(f'addHeader {keywd} {value} {self.value_type(value)} "{self.head_dict[keywd]}"')

    def header(self,keywd,value,comments):
        
        self.head_dict[keywd] = comments
        return self.rcmd(f'addHeader {keywd} {value} {self.value_type(value)} "{comments}"')
    def make_folder(self):
        _p = join(racine(),self.type)
        if 'Target' in self.type:
            _p = join(_p,self.basename) 
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
        self.increment_verification()
        self.rcmd(f"acquisition {self.nbImage} {self.expTime} {path} {self.basename}")
    def abort(self):
        #open a server connection for the abort thread
        return self.rcmd("set_abort_flag",True)

if '__main__' in __name__:
    with andor(IP) as _andor:
        print("testing script running...")
        _andor.setExpTime(4)
        _andor.initialisation()
        print(_andor)
        

        print("setting test header")
        _andor.header("test1", "10","Mon commentaire")
        _andor.header("test2", 10,"Mon commentaire")
        _andor.header("test3", 10.1,"Mon commentaire")
        from time import sleep
        _andor.acquisition()
        sleep(10)
        print("done")
        
        
