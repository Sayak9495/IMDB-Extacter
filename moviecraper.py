import os
import urllib
import json
import re

def scrape(mov,oldname,sort,what):
    mov=mov[:-1]
    serviceurl="http://www.omdbapi.com/?" 
    url = serviceurl + urllib.urlencode({'t':mov})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    data=str(data)
    imdb,rotten='',''

    try:
        imdb = data[data.index('imdbRating')+13:data.index('imdbRating')+16] 
        print imdb,
        rotten = data[data.index('Rotten Tomatoes')+26:data.index('Rotten Tomatoes')+29]       
        print rotten

    except:
        pass

    if sort==0:
        if imdb=='' and len(mov.split())>1: 
            
            try:
                mov1=mov.split()
                mov1=mov1[:len(mov1)-1]
                mov=''
                print mov1
                for io in mov1:
                    mov=mov+io+' '
                scrape(mov,oldname,sort,what)
            except:
                pass
        else:
            if imdb != '':
                try:
                    final = str(imdb)+' '+i
                    if  what == 0:
                        os.rename(oldname,final)
                    fo.write(oldname+"---------"+imdb+" "+rotten)
                    fo.write("\n")
                except:
                    print "ERROR RENAMING THE FILE"
                    pass
    elif sort == 1:
        if rotten=='' and len(mov.split())>1: 
            
            try:
                mov1=mov.split()
                mov1=mov1[:len(mov1)-1]
                mov=''
                print mov1
                for io in mov1:
                    mov=mov+io+' '
                scrape(mov,oldname,sort,what)
            except:
                pass
        else:
            if rotten != '':
                try:
                    if rotten[2]=='0':
                        final = str(rotten)+'%'+' '+i
                    else:
                        final = str(rotten)+' '+i
                    if  what == 0:
                        os.rename(oldname,final)
                    fo.write(oldname+"---------"+imdb+" "+rotten)
                    fo.write("\n")
                except:
                    print "ERROR RENAMING THE FILE"
                    pass
    return imdb,rotten

    
sp=['[',']','(',')']
fo = open("info.txt", "w")
lol = os.listdir('.')
what = int(raw_input("Do you want to rename the files and save them as TXT file(0) or only save them as TXT(1) \nEnter 0 or 1\n"))
if what == 0 :
    sort=int(raw_input("Imdb(0) or Rotten(1) \nEnter 0 or 1?\n"))
else:
    sort=0
for i in lol:
    if i[1]=='.' or i[2]=='%':
        print i
        pass
    else:
        mov=''
        oldname=i
        i = i.replace("_"," ")
        lst=re.findall(r"[\w]+",i)
        
        try:
            counter=0        
            for words in lst:
                
                for chars in words:
                    if chars in sp:
                    #if chars in sp or chars.isdigit():
                        counter = 1
                if counter == 0:
                    mov+=words+' '
            if counter == 1:
                pass
        except:
            
            try:
                lst=i.split('')
                mov=lst[0]+' '+lst[1]
            except:
                mov=lst[0]
        
        print "MOVIE NAME =",mov
        scrape(mov,oldname,sort,what)

fo.close()