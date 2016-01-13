import os.path
basedir = r'd:/'
DIRNUM = 0;
FILENUM = 0;
def listdirfile(dir,flag=''):
    global DIRNUM
    global FILENUM
    for fileordir in os.listdir(dir):
        if os.path.isdir(os.path.join(dir,fileordir)):
            print(flag+'['+fileordir+']')
            DIRNUM = DIRNUM+1
            #print('-',end='')
            try:
                listdirfile(os.path.join(dir,fileordir),flag+'-')
            except IOError:
                print('ioerror')
        else:
            print(flag+fileordir)
            FILENUM = FILENUM+1
    
        
listdirfile(basedir)
print('目录的个数是%d'%DIRNUM)
print('文件的个数是%d'%FILENUM)
    
    
