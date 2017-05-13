import os

fname = os.listdir('.')

for fn in fname:
    
    if fn[1]=='.':
        print fn
        os.rename(fn,fn[4:])
    else:
        pass
