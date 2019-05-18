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
# enable_load_extension(enabled). 
# This routine allows/disallows the SQLite engine to load SQLite extensions from shared libraries. 
# SQLite extensions can define new functions, aggregates or whole new virtual table implementations. 
# One well-known extension is the fulltext-search extension distributed with SQLite.
# Loadable extensions are disabled by default.
 
import sqlite3

con = sqlite3.connect(":memory:")

# enable extension loading

con.enable_load_extension(True)

# Load the fulltext search extension

con.execute("select load_extension('./fts3.so')")

# alternatively you can load the extension using an API call:
# con.load_extension("./fts3.so")

# disable extension loading again

con.enable_load_extension(False)

# example from SQLite wiki

con.execute("create virtual table recipe using fts3(name, ingredients)")

con.executescript("""
    insert into recipe (name, ingredients) values ('broccoli stew', 'broccoli peppers cheese tomatoes');
    insert into recipe (name, ingredients) values ('pumpkin stew', 'pumpkin onions garlic celery');
    insert into recipe (name, ingredients) values ('broccoli pie', 'broccoli cheese onions flour');
    insert into recipe (name, ingredients) values ('pumpkin pie', 'pumpkin sugar flour butter');
    """)

for row in con.execute("select rowid, name, ingredients from recipe where name match 'pie'"):

    print(row)
