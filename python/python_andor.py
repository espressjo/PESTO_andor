from pexpect import spawn,EOF
from time import sleep
from racine import racine
from last_fits import flf
from subprocess import Popen
from header_parser import parse_telmeteo,parse_telinfo
from get_inc import get_inc
class command:
    def __init__(self):
        '''
        **Description**:
            Initialization of the class.\n
            **child**: child handle process of the main tclsh consol.\n
            **child_video**: child process handle for the video feed python script\n
            **cwd**: working directory\n
            **path_data_linux**: root path on the linux computer\n
            **type_acq**: type of acquisirtion (Target,video,flat,dark)\n
            **d**: dictionary fro the type of acquisition\n
            **obj_name**: Name of the object\n
            **working_path_win**: path on the window machine. Will varie in function of the type of acq, dates and object name
            
        '''
        self.cwd = '/home/pesto/data_andor/tcl/'
        self.child = 0
        self.filter_dict = {'H':0,'g':1,'r':2,'i':3,'z':4,'Ha':5,'HA':5,'ha':5,'open':0,'h':0}
        self.filter_arr = ["open","g'","r'","i'","z'","Ha'"]
        self.child_video = 0
        self.initialize()
        self.path_data_linux = "/home/pesto/data_andor/"
        self.type_acq = 'video'
        self.stop=0
        self.filter = "NA"
        self.working_path_win = ""
        self.obj_name = 'default'
        self.d = {'Target' : 0, 'video': 1, 'dark' : 2, 'flat' : 3}
         
    def initialize(self):
        '''
        **Description**:
            Initialization sequences. This function will open a tclsh (version 8.5) console, then upload source client.tcl. Afterward a series of command will be sent to the window computer. Mostly, tcl source files will be uploaded.
        **Return**:
            void
        '''
        print "initializing..."
        self.child = spawn('/usr/local/bin/tclsh8.5',timeout=20,cwd=self.cwd)
        self.child.send('source client.tcl\n')
        self.child.expect('%')
        self.child.send('send { source acquisition.tcl }\n')
        self.child.expect('%')
        self.child.send('send { source head.tcl }\n')
        self.child.expect('%')
        self.child.send('send { source mode.tcl }\n')
        self.child.expect('%')
        self.child.send('send { set_conv 1 }\n')
        self.child.expect('%')
    def set_path(self):
        '''
        **Description**:
            This function will set the window working path. E.g., /190521/Target/test-omm/.
        **Note**:
            This function is useless if the class is used interactively
        **Return**:
            This function will return 0 if succesffull or -1 if it failed.
        '''
        if 'Target' in self.type_acq:
            self.working_path_win = "/"+racine()+"/"+self.type_acq+"/"+self.obj_name+"/"
            return 0
        elif 'video' in self.type_acq:
            self.working_path_win = "/"+racine()+"/"+self.type_acq+"/"
            return 0
        elif 'flat' in self.type_acq:
            self.working_path_win = "/"+racine()+"/"+self.type_acq+"/"
            return 0
        elif 'dark' in self.type_acq:
            self.working_path_win = "/"+racine()+"/"+self.type_acq+"/"
            return 0
        else:
            return -1
    def watch_dog(self,expT):
        '''
        **Description**:
            This function starts the watch dog. Essentially, it launch an infinite loop that follows every image creation in the working path directory.
        **Note**:
            This function can be used interactivaly, but will block the main thread. Either use this function with the acq function or open another console the execute the stop_acq function when you want the acquisition to stop.
        **Return**:
            void
        '''
        path = self.path_data_linux[:-1]+self.working_path_win
        print "watch dog woofing in %s"%(path)
        last_file = "default"
        i = 0
        fivemin = int(60*5./expT)
        
        while(1):
            sleep(expT+2)
            i+=1
            name = flf(path)
            print name
            if name==-1:
                print "name"
                continue
            if name == last_file:
                break
            if i>fivemin:
                i=0
                print "woofing: %s is the last file"%name
            if self.stop==1:
                break
            last_file = name
                
        print "::::::::::::::: Exposure Done!! :::::::::::::::::::"
        self.stop = 0  
    def __check_digit(self,a):
        '''
        **Description**:
            This function check if the string is a positive float or int.
        **Return**:
            int,float or -1 if unsuccessfull
        '''
        if '.' in a:
            for check in a.split('.'):
                if not check.isdigit():
                    return -1
            return float(a)
        else:
            if a.isdigit():
                return int(a)
            else:
                return -1
    def set_header(self):
        '''
        **Desceription**:
            This function will set the header of the futur images. BonOMM must be open otherwise the function will fail.
        **Return**:
            This function returns 0 if successfull or -1 if unsuccessfull
        '''
        self.child.send('send { init_header 1 }\n')
        self.child.expect('%')
        telmeteo = parse_telmeteo()
        if telmeteo==-1: return -1
        self.child.send('send { set_temp %f %f %f %f %f %f }\n'%(telmeteo['Hin'],telmeteo['Hout'],telmeteo['Tin'],telmeteo['Tout'],telmeteo['Tstruct'],telmeteo['Tmir']))
        self.child.expect('%')
        telinfo = parse_telinfo()
        if telinfo==-1: return -1
        self.child.send('send { set_telinfo %1.6f %1.6f %d %1.6f %1.6f %d %1.6f %1.6f}\n'%(telinfo['RA'],telinfo['DEC'],telinfo['EPOCH'],telinfo['HA'],telinfo['AIRMASS'],telinfo['TFOCUS'],telinfo['IROTATOR'],telinfo['DOME']))
        self.child.expect('%')
        
        self.child.send('send { set_pesto %s 999 999 }\n'%self.filter)
        self.child.expect('%')
        return 0
        
    def __inc(self):
        '''
        This function returns the last increment of the fits file in path_working_win
        '''
        inc = get_inc(self.path_data_linux)
        if inc==-1:return 1
        else: return inc
    def acq(self,nbExp,expTime,**kwargs):
        '''
        **Description**:
            This function triggeres an acquisition sequence 
        **nbExp**: 
            number of exposure
        **expTime**: 
            exposure time in seconds
        **Options**:
            --nowoof--: [True/False] Do not start the watch dog (does not block the main thread)
        **Return**:
            return void once the nb. of exposure is acquired
        '''
        self.set_path()
        self.child.send('send { acqui %d %d %1.2f %s %s }\n'%(nbExp,self.__inc()+1,expTime,self.working_path_win,self.obj_name))
        self.child.expect('%')
        if not 'nowoof' in kwargs and not kwargs.get('nowoof'):
            self.watch_dog(expTime)  
    def acq_mode(self,mode):
        '''
        **Description**:
            This function sets the acquisition mode. Choices are : Target, video,flat,dark
        **Return**:
            return -1 if fails, void if successfull
        '''
        if 'Target' in mode: self.type_acq = 'Target'
        elif 'video' in mode : self.type_acq = 'video'
        elif 'flat' in mode : self.type_acq = 'flat'
        elif 'dark' in mode : self.type_acq = 'dark'
        else:
            return -1
    def video_flux(self):
        '''
        **Description**:
            This function starts the video flux
        **Note**:
            Normally this function is not used interactivelly
        '''
        print "starting video."
        path = self.path_data_linux[:-1]+self.working_path_win
        self.child_video = spawn('/usr/bin/python %s/python/video.py %s'%(self.path_data_linux,path),timeout=2)
    def script(self,**kwargs):
        '''
        **Description**:
            This function will execute a script. The user will be prompt the enter the target name, exposure time and object name. The header, acquisition mode and the path will be automatically updated.
        **Options**:
            --video--: Not used interactivally. Will trigger the video function. Use the video function
            --no_header: Used to not querry telinfo and telmeteo. If the script function fails the first time because of the telmeteo or telinfo, you can manually use the set_header function and then use script(no_header=True).
        **Note**:
            i) Use the stop_acq() function to stop the acquisition of th script. 
            ii) the video flux will be automatically launched after exposuretime+2 secondes
        '''
        if 'video' in kwargs and kwargs.get('video'):
            self.acq_mode('video')
        else:
            while (1):
                out = raw_input('acq mode: [Target, video, dark, flat]: ')
                if out in self.d:
                    self.acq_mode(out)
                    break
        if 'video' in kwargs and kwargs.get('video'):  
            self.obj_name = 'video'
        else:
            self.obj_name = raw_input('Name of the object: ')
        while(1):
            expT = raw_input("exposure time? (in seconds): ")
            if self.__check_digit(expT)!=-1:
                break
        print "updating the header"
        if not 'no_header' in kwargs and not kwargs.get('no_header'):
            if self.set_header()==-1:
                print "Unable to set the header. You can manually update the header using the set_header() function than use the no_header=True argument in script() function."
        
        self.acq(65000,float(expT),nowoof=True)
        sleep(float(expT)+2)
        self.video_flux()
#    def __check(self,child):
#        while(1):
#            child.send("status 1\n")
#            child.readline()
#            out = child.readline().strip('\r').strip('\r').strip('\n')
#            print out
#            #child.expect('%')
#            if int(out)==0:
#                break
#            print "waiting for the end of the exposure"
#            sleep(3)
#        return
    def stop_acq(self):
        '''
        **Description**:
            This function will stop a image acquisition
        '''
        child_stop = spawn('/usr/local/bin/tclsh8.5',timeout=10000,cwd=self.cwd)
        child_stop.expect('%')
        child_stop.send('source startstop2.tcl\n')
        child_stop.expect('%')
        child_stop.send('stop 1 \n')
        
        child_stop.expect('%')
        #self.__check(child_stop)        
        child_stop.terminate()
        self.child_video.terminate()
    def send(self,cmd):
        '''
        **Description**:
            This function directly sends command to the window tclsh console. Do not use this function while another function is running
        '''
        self.child.send('send { %s }\n'%cmd)
        self.child.expect('%')
    def video(self,**kwargs):
        '''
        **Description**:
            This function will start the video flux. The user will be ask to enter the exposure time
        **Note**:
            i) use the stop_acq() function to stop the video feed
        '''
        self.script(video=True)
    def fw(self,filtre):
        '''
        **Description**:
            This function set the filter. 
        **Note**:
            If this function fails it will return -1 and write NA in the header
        '''
        if "'" in filtre:
            filtre = filtre.strip("'")
        if not filtre in self.filter_dict:
            print "Wrong filter choice"            
            return -1
        pos = self.filter_dict[filtre]
         
        chld = spawn("fwandor %d"%(pos),cwd=self.cwd)
        out = chld.expect(EOF)
        if out==0:
            print "filter set successfully to %s"%self.filter_arr[pos]
            self.filter = self.filter_arr[pos]
        else:
            self.filter = "NA"
        
        
        
        
    
    
        
        