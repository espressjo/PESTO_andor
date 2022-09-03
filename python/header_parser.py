from subprocess import Popen,PIPE

#child = Popen(['telinfo'],stderr=PIPE,stdout=PIPE)
#out,err = child.communicate()
def __convRA(ra):
    #hour + minute/60 + second/3600
    h,m,s = ra.split(':')
    return float(h)+float(m)/60.0 + float(s)/3600.0
def parse_telinfo():
    d = {}
    child = Popen(['telinfo'],stderr=PIPE,stdout=PIPE)
    output,err = child.communicate()
    if not output: return -1
    output = output.decode()
    if not 'HA' in output: return -1
    for line in output.split("\n"):
        if 'RA' in line and len(line.split(':'))>3: d['RA'] = __convRA(line.split('RA:')[1])    
        if 'DEC' in line and len(line.split(':'))>3: d['DEC'] = __convRA(line.split('DEC:')[1])
        if 'AIRMASS' in line: d['AIRMASS'] = float(line.split('AIRMASS:')[1])
        if 'FOCUS' in line: d['TFOCUS'] = int(line.split('FOCUS:')[1])
        if 'HA' in line and len(line.split(':'))>3: d['HA'] = __convRA(line.split('HA:')[1])
        if 'EPOCH' in line: d['EPOCH'] = int(line.split('EPOCH:')[1])
        if 'DOME' in line: d['DOME'] = float(line.split('DOME:')[1])
        if 'ROTATOR' in line: d['IROTATOR'] = float(line.split('ROTATOR:')[1])
    if len(d)==8:
        return d
    else:
        print("header not parsed properly")
        return -1
def parse_telmeteo():
    d = {}
    child = Popen(['telmeteo'],stderr=PIPE,stdout=PIPE)
    output,err = child.communicate()
    if not output: return -1
    output = output.decode()
    if not 'Hin' in output: return -1
    for line in output.split('\n'):
        if 'Hin' in line: d['Hin'] = float(line.strip('Hin:').strip('%'))
        if 'Hout' in line: d['Hout'] = float(line.strip('Hout:').strip('%'))
        if 'Tin' in line: d['Tin'] = float(line.strip('Tin:').strip('\xe2\x84\x83'))
        if 'Tmir' in line: d['Tmir'] = float(line.strip('Tmiror:').strip('\xe2\x84\x83'))
        if 'Tout' in line: d['Tout'] = float(line.strip('Tout:').strip('\xe2\x84\x83'))
        if 'Tstruct' in line: d['Tstruct'] = float(line.strip('Tstruct:').strip('\xe2\x84\x83'))
    if len(d)!=6:
        print("problem parsing telmeteo")
        return -1
    else:
        return d