from os.path import join,getctime
from os import walk

def __find_between_r( s):
    if s and 'fits' in s:
        return int(s.split('/')[-1].split('_')[-1].strip('.fits'))
    else:
        return -1
def get_inc(path)  :   
    files = [join(root,f) for root,_,the_files in walk(path) for f in the_files if f.lower().endswith(".fits")]
    if len(files)!=0:
        List = sorted(files,key=getctime)
        most_recent_file = __find_between_r(str(List[-1]))
    else:
        most_recent_file = -1
        
    return most_recent_file

