import sqlite3
def sql(code):
    conn = sqlite3.connect('sas/data.db')
    c = conn.cursor()
    c.execute(code)
    conn.commit()
    f=c.fetchall()
    conn.close()
    return f
def create():
    conn = sqlite3.connect('sas/data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS files(name text,fname text,pw text,data text,enc text)')
    conn.close()
    
