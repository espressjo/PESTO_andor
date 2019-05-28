import datetime 
from numpy import asarray

def __now():
    now = datetime.datetime.now()
    return asarray(now.strftime("%Y-%m-%d-%H-%M-%S").split('-'),dtype=int)
     
def racine():
    '''
    **Description**:
        This function return a string of the format YYMMDD between 12:00:00 and 23:59:59 and YYMMDD-1 between 00:00:00 and 11:59:59.
    '''
    now = __now()
    if now[3]>=12 and now[3]<=23:
        return "%2.2d%2.2d%2.2d"%(now[0]%100,now[1],now[2])
    elif now[3]<12 and now[3]>=0:
        return "%2.2d%2.2d%2.2d"%(now[0]%100,now[1],now[2]-1)
    




