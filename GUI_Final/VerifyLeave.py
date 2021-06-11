#IMPORTANT:READLINES FUNCTION SHIFTS POINER AFTER EXECUTION
import datetime

def leaverec(fname):
    file=fname+'.txt'
    f=open(file,"r")
    t=str(datetime.datetime.now())[:10]
    l=f.readlines()
    s=[i.strip('\n') for i in l]

    if t in s:
        return False

    else:
        return True
       
    



    
