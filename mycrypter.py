def enc(text,key):
    t=text.split('.')
    while '' in t:
        t.remove('')
    d=''''''
    for i in t:
        d+=str((int(i)+int(key)))+'.'
    return d

def dec(text,key):
    t=text.split('.')
    while '' in t:
        t.remove('')
    d=''''''
    for i in t:
        d+=str((int(i)-int(key)))+'.'
    return d
