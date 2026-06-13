############### Relational Database with Python ############
import sqlite3  
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')            
conn.commit()
conn.close()    

############## Defination of Realtional Database ? ############
# A relational database is a type of database that organizes data into tables with rows and columns. Each table represents a specific entity or concept, and the relationships between tables are established through keys. Relational databases use Structured Query Language (SQL) for managing and querying data. They are widely used in various applications, including web development, data analysis, and business applications, due to their ability to handle large volumes of data and maintain data integrity through relationships. Examples of relational database management systems include MySQL, PostgreSQL, and SQLite.