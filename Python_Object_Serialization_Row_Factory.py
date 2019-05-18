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
# row_factory 
# You can change this attribute to a callable that accepts the cursor and the original row as a tuple and 
# will return the real result row. This way, you can implement more advanced ways of returning results, 
# such as returning an object that can also access columns by name.
 
import sqlite3

def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d

con = sqlite3.connect(":memory:")
con.row_factory = dict_factory

cur = con.cursor()
cur.execute("select 1 as a")

print(cur.fetchone()["a"])
