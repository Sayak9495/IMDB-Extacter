import os

fname = os.listdir('.')

for fn in fname:
    
    if fn[1]=='.' or fn[2]=='%':
        print fn
        os.rename(fn,fn[4:])
    elif fn[3]=='%':
        print fn
        os.rename(fn,fn[5:])
    else:
        pass
