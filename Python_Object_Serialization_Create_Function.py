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
# The 'create_function(name, num_params, func)' creates a user-defined function that you can later use 
# from within SQL statements under the function name name. num_params is the number of parameters the 
# function accepts (if num_params is -1, the function may take any number of arguments), and func is a 
# Python callable that is called as the SQL function.
# The function can return any of the types supported by SQLite: bytes, str, int, float and None.

import sqlite3
import hashlib

def md5sum(t):
    return hashlib.md5(t).hexdigest()

con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)

cur = con.cursor()
cur.execute("select md5(?)", (b"foo",))

print(cur.fetchone()[0])
