# -*- coding: utf-8 -*-
import sqlite3,sql,md5,time,os,mycrypter,hashe,getpass,auth,sys,pickle
def crypt(files,pw,pwn,enc):
    sql.create()
    if pw!=pwn:
        print "Passwords didn't match!"
    elif enc!='y' and enc!='n':
        print "Please Select valid encryption method!"
    else:
        try:
                
            c=open(files,'rb+')
            d=c.read()
            go=True
            for i in sql.sql('select name from files'):
                if files in i:
                    print ('A file with same name exist.Please rename your file')
                    go=False
            if go:
                print ''
                if enc=='n':
                    print 'Locking file.Please wait.Thise may take few minuites to complete depending on your file size'
                elif enc=='y':
                    print 'Encrypting file.Please wait.Thise may take few minuites to complete depending on your file size'
                print ''
                try:
                    pw=md5.md5(pw).hexdigest()
                    e=[]
                    ccc=''''''
                    mm={}
                    mm2={}

                    for i in d:
                        try:
                            mycryptekljkr.encrypt(i)
                        except:
                            if i not in e:
                                e.append(i)
                    e2=[str(i+int(pw[-5],16)) for i in range(len(e))][::-1]
                    for i in range(len(e)):
                        mm[e[i]]=e2[i]

                    for i in d:
                        ccc+=mm[i]+'.'
                    ft=files[1]+str(time.time())+files[0]
                    if enc=='y':
                        try:
                            ccc= mycrypter.enc(ccc,int(hashe.key(pw)))
                        except Exception as i:
                            print i
                    elif enc=='n':
                        
                        with open(ft, 'wb') as handle:
                          pickle.dump(ccc, handle)
                        ccc=' '
                    ft=files[1]+str(time.time())+files[0]
                    ss="insert into files (name,fname,pw,data,enc) values ('%s','%s','%s','%s','%s')"%(files,ft,pw,ccc,enc)
                    sql.sql(ss)
                    c.close()
                    c=open('sas/'+ft+'log.sas','w')
                    c.write(str(e))
                    os.remove(files)
                    print 'file %s locked successfully!' %(files)
                except:
                    raw_input( 'There was something error with locking file %s' %(files))
                    sys.exit()

        except:
            print 'Cant open file %s'%(files)



def decrypt(pw):
    pw=md5.md5(pw).hexdigest()
    fff=sql.sql('select name from files')
    print ''
    print 'Searching for locked files...'
    print ''
    for i in fff:
        print i[0]
    if not fff:
        print 'No Locked files found'
    else:
       if 1:
            print ''
            print 'Found %s files'%(len(fff))
            print ''
            files=raw_input('Enter File name to unlock: ')
            mm2={}
            abc=sql.sql('select data from files where name="%s"'%(files))
            c=open('sas/'+(sql.sql('select fname from files where name="%s"'%(files)))[0][0]+'log.sas','r')
            exx='e='+c.read()            
            
            exec(exx)
            e2=[str(i+int(pw[-5],16)) for i in range(len(e))][::-1]
            c.close()        
            for i in range(len(e)):
                mm2[e2[i]]=e[i]
            ddd=''''''
            ab=abc[0][0]
            en=sql.sql('select enc from files where name="%s"'%(files))
            if en[0][0]=='y':
                try:
                    ab= mycrypter.dec(ab,int(hashe.key(pw)))
                except Exception as i:
                    print i
            elif en[0][0]=='n':
                pass
            else:
                print en[0][0]
            for i in ab.split('.'):
                    if i !='':
                        ddd+=mm2[i]
                        

            
            hh=open(files,'wb+')
            hh.write(ddd)
            print 'file %s unlocked successfully!' %(files)
            hh.close()

def main():
        import sys
        print ""
        print "Welcome to SAS File Encrypter and Locker"
        print ""
        print ""
        print ""
        mainn()

def mainn():
    while 1:
        try:
            if not auth.auth():
                
                try:
                    os.remove('sas/data.db')
                    auth.create()
                except:
                    pass
                p=getpass.getpass('Create Password: ')
                q=getpass.getpass('Re-Enter Password: ')
                if p==q:
                    pw=md5.md5(p).hexdigest()
                    auth.addpw(pw)
                else:
                    print "passwords didn't match"
            else:
                inp=raw_input( " Enter 'L' to login or 'C' to change your password: ")
                if inp=='C':
                    cur=auth.auth()
                    p=getpass.getpass('Enter Current Password: ')

                    if md5.md5(p).hexdigest()!=cur[0]:
                        print 'Wrong password'
                    elif md5.md5(p).hexdigest()==cur[0]:
                        r=getpass.getpass('Create new Password: ')
                        q=getpass.getpass('Re-Enter Password: ')
                        if r==q:
                            npw=md5.md5(r).hexdigest()
                            auth.cpw(npw)
                            print "passwords Changed successfully"
                        else:
                            print "passwords didn't match"
                elif inp=='L':
                    cur=auth.auth()
                    p=getpass.getpass('Enter Password: ')
                    if md5.md5(p).hexdigest()!=cur[0]:
                        print 'Wrong password'
                    elif md5.md5(p).hexdigest()==cur[0]:
                        main2(p)
        except Exception as i:
            print 'Something went wrong..Please restart the program!'
def main2(p):
    while 1:
        inp=raw_input( " Enter 'L' to lock or encrypt files 'U' to unlock files or 'E' to exit: ")
        if inp=='E':
            
            sys.exit()
            break
        elif inp=='U':
            decrypt(p)
        elif inp=='L':
            files=raw_input('Enter path to file (if you want to lock multiple files, add all paths coma seperated): ')
            enc=raw_input("Do you want to encrypt your file(s)? Encrypting helps you to secure your files,but it may slow down locking procces.Enter 'y' to Encrypt and lock or 'n' to lock without encrypting:   : ")
            for i in files.split(','):
                pw=p
                pwn=p
                if enc!='y' and enc!='n':
                    print "Please Select valid encryption method!"
                else:
                    crypt(i,pw,pwn,enc)
            
            
main()    
