from pexpect import spawn,EOF
import os

class pytcl:
    def __init__(self,ip,port,alternateP=None):
        self.ip = ip
        self.alternate_port = alternateP
        self.port = port
        self.python_path = "/opt/andor/python"
        self.tclsh = "env LD_LIBRARY_PATH=/opt/tclsh8.5/lib /opt/tclsh8.5/bin/tclsh"
        self.child = None
        self.child_alternate = None
    def connect(self):
        print("Connecting to Audela server.")
        self.child = spawn(self.tclsh,timeout=2,cwd="./")
        self.child_alternate = spawn(self.tclsh,timeout=2,cwd="./")
        print("version of DP: ",self.write("package require dp"))
        print("TCP socket: ",self.write(f"set server [dp_MakeRPCClient {self.ip} {self.port} ]"))
        if self.alternate_port:
            print("Connecting to alternate port")
            self.write_alternate("package require dp")
            self.write_alternate(f"set server [dp_MakeRPCClient {self.ip} {self.alternate_port} ]")
        
        return self  # The returned value is assigned to 'm' in 'with MyModule() as m:'
    def __enter__(self):
        return self.connect()  # The returned value is assigned to 'm' in 'with MyModule() as m:'
    def disconnect(self):
        return self.write("close $server\n")
    def rcmd(self,cmd,alternate=False):
        #write a command directly on the Audela console.
        c = f'dp_RPC $server {cmd}\n'
        if alternate:
            return self.write_alternate(c)
        else:
            return self.write(c)
    def write_alternate(self,cmd):
        try:
            self.child_alternate.send(f"{cmd}\r\n")
            self.child_alternate.readline()
            self.child_alternate.expect("%")
            return self.child_alternate.before.decode().strip()
        except:
            return
    def write_blind(self,cmd):
        #same as write but we do not expect anything
        self.child.send(f"{cmd}\r\n")
    def write(self,cmd):
        try:
            self.child.send(f"{cmd}\r\n")
            self.child.readline()
            self.child.expect("%")
            return self.child.before.decode().strip()
        except:
            return 
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        #trying to disconnect from server
        #self.write("close $server\n")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return False
    
if __name__ == "__main__":
    
    with pytcl("localhost",5002) as tcl:
        print(tcl.rcmd('puts "hello world!"'))
        print("ok") 
