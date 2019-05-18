# Python object serialization
# The 'pickle' module implements binary protocols for serializing and de-serializing 
# a Python object structure. 
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
# and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like 
# object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”; 
# however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
# copyreg — Register pickle support functions
# The copyreg module offers a way to define functions used while pickling specific objects. 
# The pickle and copy modules use those functions when pickling/copying those objects. 
# The module provides configuration information about object constructors which are not classes. 
# Such constructors may be factory functions or class instances.
# This example shows how to register a pickle function and how it will be used:
 
import copyreg, copy, pickle

class C(object):

       def __init__(self, a):
            self.a = a

      def pickle_c(c):

        print("pickling a C instance...")

        return C, (c.a,)

    copyreg.pickle(C, pickle_c)

    c = C(1)
    d = copy.copy(c)  # doctest: +SKIP

# Displays 'pickling a C instance...'

    p = pickle.dumps(c)  # doctest: +SKIP

# Displays 'pickling a C instance...'
