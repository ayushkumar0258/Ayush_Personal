import sqlite3
conn =sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()
cur.execute('drop table if exists counts')
cur.execute('create table counts (email varchar(128) , count int)')
fname=input("Enter File name : ")
if(len(fname)<1):
    fname='mbox-short.txt'
cur.execute('select * from counts')
#cur.execute('drop table counts')
