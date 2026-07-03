import sqlite3
conn =sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()
cur.execute('drop table if exists counts')
cur.execute('create table counts (email varchar(128) , count int)')
fname=input("Enter File name : ")
if(len(fname)<1):
    fname='mbox.txt'
fh=open(fname)
data=list()
for lines in fh:
    if lines.startswith('From: '):
        data=lines.split()
        email=data[1]
        sql1=cur.execute('select count(1) from counts where email=?', (email,))
        row=cur.fetchone()
        if row[0] == 0:
            cur.execute('insert into counts (email,count) values (?,1)',(email,))
        else:
            cur.execute('update counts set count=count+1 where email=?',(email,))
        conn.commit()

for i in cur.execute('select email,count from counts order by count desc limit 10'):
    print(str(i[0]), i[1])
cur.close()

