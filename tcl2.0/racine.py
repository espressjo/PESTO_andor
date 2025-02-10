from datetime import datetime ,timedelta
from numpy import asarray

def __now():
    now = datetime.now()
    return asarray(now.strftime("%Y-%m-%d-%H-%M-%S").split('-'),dtype=int)
     
def racine():
    '''
    Description
    ------------
    
        This function return a string of the format YYMMDD between 
        12:00:00 and 23:59:59 and YYMMDD-1 between 00:00:00 and 11:59:59.
    
    RETURN STR
    -------
        yymmdd
    '''
    now = datetime.now()
    if now.hour>=12 and now.hour<=23:
        return now.strftime("%y%m%d")
    else :
        shift = timedelta(days=1)
        return (now-shift).strftime("%y%m%d")
    




