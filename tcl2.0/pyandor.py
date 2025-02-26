import os
from telcible import telcible
from telmeteo import telmeteo 
from tcs2 import tcs
from os import popen
from os.path import join 
from tcs import tcs
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
        self.objet = "test"
        self.local_path = LOCALPATH
        self.head_dict = {}
        self.relaunchfeed()
        self.fwOK = False
    def fw(self,position):
        if not self.fwOK:
            print("initializing filter wheel")
            if 'open' not in os.popen("/opt/pesto/bin/fwandor open").read().strip():
                return -1

            self.fwOK = True
        if position not in os.popen(f"/opt/pesto/bin/fwandor {position} -nocheck").read().strip():
            return -1 
        return 0

    def getfwposition(self):
        return os.popen("/opt/pesto/bin/fwandor -getposition -nocheck").read().strip()
    def relaunchfeed(self):
        if self.running:
            self.kill()
        P = join(self.local_path,racine())
        self.launch(P)
    def setHeader(self):
        #do something
        
        #get some info 
        
        telmeteo = telmeteo()
        telmeteo.telmeteo()
        tcs = tcs()
        tcs.telinfo()
        if self.fwOK:
            f = self.getfwposition()
        else:
            f = "NOK"
        telcible = telcible()
        telcible.telcible()

        self.header("EXPOSURE",self.expTime,"The effective exposure time in ms")
        self.header("HUMIN",telmeteo.HIN,"Interior humidity (%)")
        print(f)
        self.header("FILTRE",f,"Filter used")
        self.header("HUMOUT",telmeteo.HOUT,"Exterior humidity (%)")
        self.header("TEMPIN",telmeteo.TIN,"Interior temperature (C)")
        self.header("TEMPOUT",telmeteo.TOUT,"Exterior temperature (C)")
        self.header("TEMPST",telmeteo.TSTRUCT,"Telescope structure temperature (C)")
        self.header("TEMPM",telmeteo.TMIR,"Mirror temperature (C)")
        self.header("OBJECT",self.objet,"object name")
        #tcs
        self.header("EPOCH",tcs.EPOCH,"Epoch of the coordinate")
        self.header("AIRMASS",tcs.AIRMASS,"Airmass")
        self.header("RA",tcs.RA,"right ascention")
        self.header("HA",tcs.HA,"hour angle")
        self.header("DEC",tcs.DEC,"declinaison")
        self.header("FOCUS",tcs.FOCUS,"Focus of the telescope")
        self.header("ROTATOR",tcs.ROTATOR,"Angle of the instrument rotator")
        self.header("YEAR",tcs.YEAR,"Year")
        self.header("DOME",tcs.DOME,"angle of the dome")
        self.header("ST",tcs.ST,"Sideral time")
        self.header("UT",tcs.UT,"Universal time")
        self.header("PROGRAM",telcible.PROGRAM,"Universal time")
        self.header("SOFTV","2.0","acquisition software version")
        telmeteo.disconnect()
        tcs.disconnect()
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
        txt+=f"Obj. Name: {self.objet}\n"
        txt+=f"Mode: {self.mode}\n"
        c_inc = self.rcmd("get_increment")
        txt+=f"Current increment: {c_inc}\n"
        return txt
    def value_type(self,value):
        if isinstance(value,int):
            return "int"
        elif isinstance(value,float):
            return "float"
        else :
            return "string"
    def header(self,keywd,value,comments=""):
        #update and create a header entry
        if keywd not in self.head_dict:
            self.rcmd(f'addHeader {keywd} {value} {self.value_type(value)} "{comments}"')
        else:
            self.rcmd(f'addHeader {keywd} {value} {self.value_type(value)} "{self.head_dict[keywd]}"')
    def make_folder(self):
        _p = join(racine(),self.type)
        if 'Target' in self.type:
            _p = join(_p,self.objet) 
        return _p
    def setExpTime(self,exp):
        self.expTime = float(exp)
    def set_nb_images(self,nb):
        self.nbImage = int(nb) 
    def setType(self,type):
        if type not in self.type_list:
            raise ValueError("Invalid type")
        self.type = type
    def testAudeLa(self,txt):
        return self.rcmd('console::affiche_resultat "%s"'%txt)
    def initialisation(self):
        return self.rcmd("cam1 electronic 1 0 1 2 0 1") 
    def acquisition(self):
        #acquisition $nbimages $increment $expt $path $basename
        print("setting header...")
        self.setHeader()
        path = self.make_folder()
        #make sure TCL is happy
        if path[0] !='/':
            path = "/"+path 
        if path[-1]!='/':
            path = path +"/" 
        self.increment_verification()
        _basename = racine()
        self.rcmd(f"acquisition {self.nbImage} {self.expTime} {path} {_basename}")
        
    def abort(self):
        #open a server connection for the abort thread
        return self.rcmd("set_abort_flag",True)
    def script(self):
        self.setType("Target")
        #integrtion time
        _expT = input("Integration time (s): ")
        try:
            self.setExpTime(_expT)
        except:
            raise Exception("Invalid integration time")
            return 
        telcible = telcible()
        telcible.telcible()
        if telcible.s_info:
            telcible.OBJET !="0" and telcible.OBJET!="":
            print(f"{telcible.OBJET} found loaded!")
            if "yes" in input("Do you want to use this object? [yes/no]: "):
                self.objet = telcible.OBJET
            else:
                self.objet = input("Name of the object?: ")
        else:
            self.objet = input("Name of the object?: ")
        _nb_image = input("Number of images: ")
        try:
            self.set_nb_images(_nb_image)
        except:
            raise Exception("Invalid number of images")
            return
        print("starting acquisition...")
        self.acquisition()
            
            
if '__main__' in __name__:
    with andor(IP) as _andor:
        print("testing script running...")
        _andor.setExpTime(4)
        _andor.initialisation()
        print(_andor)
        
        #print("setting fw...")        
        #_andor.fw("open")
        print("setting test header")
        #_andor.header("test1", "10","Mon commentaire")
        #_andor.header("test2", 10,"Mon commentaire")
        #_andor.header("test3", 10.1,"Mon commentaire")
        from time import sleep
        _andor.acquisition()
        sleep(10)
        print("done")
        
        
