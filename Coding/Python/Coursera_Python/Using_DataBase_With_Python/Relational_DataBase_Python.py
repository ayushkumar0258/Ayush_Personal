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

########## tuples in Relational Database ############
# In a relational database, a tuple is a single row of data in a table. It represents a specific instance of an entity or concept defined by the table. Each tuple consists of a set of attributes (columns) that describe the properties of the entity. For example, in a table called "users" with columns "id", "name", and "age", a tuple might look like this: (1, 'Alice', 30). This tuple represents a user with an id of 1, a name of 'Alice', and an age of 30. Tuples are used