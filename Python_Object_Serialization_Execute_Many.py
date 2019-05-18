# Python object serialization
# The 'pickle' module implements binary protocols for serializing and de-serializing 
# a Python object structure. 
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
# and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like 
# object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”; 
# however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
# sqlite3 — DB-API 2.0 interface for SQLite databases
# SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate 
# server process and allows accessing the database using a nonstandard variant of the SQL query language. 
# Some applications can use SQLite for internal data storage. 
# It’s also possible to prototype an application using SQLite and then port the code to a larger database 
# such as PostgreSQL or Oracle.
# executemany(sql, seq_of_parameters) 
# Executes an SQL command against all parameter sequences or mappings found in the sequence seq_of_parameters. 
# The sqlite3 module also allows using an iterator yielding parameters instead of a sequence.
 
import sqlite3

class IterChars:

    def __init__(self):
        self.count = ord('a')

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > ord('z'):
            raise StopIteration
        self.count += 1

        return (chr(self.count - 1),) # this is a 1-tuple

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table characters(c)")

theIter = IterChars()
cur.executemany("insert into characters(c) values (?)", theIter)

cur.execute("select c from characters")

print(cur.fetchall())
