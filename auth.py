import sqlite3,sql
def create():
    conn = sqlite3.connect('sas/data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS auth(pw text)')
    conn.close()

def auth():
    try:
        conn = sqlite3.connect('sas/data.db')
        c = conn.cursor()
        c.execute('select pw from auth')
        vv=c.fetchone()
        conn.close()
        return vv
    except:
        return False


def addpw(paw):
    conn = sqlite3.connect('sas/data.db')
    c = conn.cursor()
    c.execute('insert into auth(pw) values ("%s")'%(paw))
    conn.commit()
    conn.close()

def cpw(pw):
    conn = sqlite3.connect('sas/data.db')
    c = conn.cursor()
    c.execute('update auth set pw="%s"'%(pw))
    conn.close()
