import os
import urllib
import json
import re

def scrape(mov,oldname):
    mov=mov[:-1]
    serviceurl="http://www.omdbapi.com/?"
    #url = serviceurl + urllib.urlencode({'t':mov,'yr':year}) 
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

    if imdb=='' and len(mov.split())>1: 
        
        try:
            mov1=mov.split()
            mov1=mov1[:len(mov1)-1]
            mov=''
            print mov1
            for io in mov1:
                mov=mov+io+' '
            scrape(mov,oldname)
        except:
            pass
    else:
        if imdb != '':
            try:
                print "I'm at Line 41"
                final = str(imdb)+' '+i
                print "I'm at Line 43",i
                os.rename(oldname,final)
            except:
                print "ERROR RENAMING THE FILE"
                pass
    
    return imdb,rotten

    
sp=['[',']','(',')']
fo = open("info.txt", "w")
lol = os.listdir('.')

for i in lol:
    if i[1]=='.':
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
        p=list(scrape(mov,oldname))
        imdb,rotten=p[0],p[1]
        fo.write(i+"---------"+imdb+" "+rotten)
        fo.write("\n")

fo.close()