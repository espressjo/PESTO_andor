import subprocess
from os.path import join
def flf(path):
    '''
    **Description**:
        Utilize ls and head command to find the last fits file in a given folder. The unix command is ls -t *.fits | head -n1
    **Return**:
        return the name of the file. If none, the function will return -1
    '''
    ls = subprocess.Popen(["stat -c '%X %n' *.fits | sort -k1n | tail -1"],shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,cwd=path)
    out,err = ls.communicate()
    o = out.decode().split(' ')
    
    if len(o)!=2:
        return -1
    return join(path,o[1].strip('\n'))
def flfgz(path):
    '''
    **Description**:
        Utilize ls and head command to find the last fits.gz file in a given folder. The unix command is ls -t *.fits | head -n1
    **Return**:
        return the name of the file. If none, the function will return -1
    '''
    ls = subprocess.Popen(["stat -c '%X %n' *.fits.gz | sort -k1n | tail -1"],shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,cwd=path)
    out,err = ls.communicate()
    o = out.decode().split(' ')
    
    if len(o)!=2:
        return -1
    return join(path,o[1].strip('\n'))



