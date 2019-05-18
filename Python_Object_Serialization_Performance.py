# Python object serialization
# The 'pickle' module implements binary protocols for serializing and de-serializing 
# a Python object structure. 
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
# and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like 
# object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”; 
# however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
# Performance
# Recent versions of the pickle protocol (from protocol 2 and upwards) feature efficient binary encodings 
# for several common features and built-in types. 
# Also, the pickle module has a transparent optimizer written in C.
# For the simplest code, use the dump() and load() functions.
 
import pickle

# An arbitrary collection of objects supported by pickle.

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:

    # Pickle the 'data' dictionary using the highest protocol available.

    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
