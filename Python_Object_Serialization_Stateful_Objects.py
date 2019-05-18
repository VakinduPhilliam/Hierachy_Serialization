# Python object serialization
# The 'pickle' module implements binary protocols for serializing and de-serializing 
# a Python object structure. 
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
# and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like 
# object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”; 
# however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
# Handling Stateful Objects.
# This example shows how to modify pickling behavior for a class. The TextReader class opens a text file, 
# and returns the line number and line contents each time its readline() method is called. 
# If a TextReader instance is pickled, all attributes except the file object member are saved. 
# When the instance is unpickled, the file is reopened, and reading resumes from the last location. 
# The __setstate__() and __getstate__() methods are used to implement this behavior.
 
class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):

        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):

        self.lineno += 1
        line = self.file.readline()

        if not line:
            return None

        if line.endswith('\n'):
            line = line[:-1]

        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):

        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.

        state = self.__dict__.copy()

        # Remove the unpicklable entries.

        del state['file']

        return state

    def __setstate__(self, state):

        # Restore instance attributes (i.e., filename and lineno).

        self.__dict__.update(state)

        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.

        file = open(self.filename)

        for _ in range(self.lineno):
            file.readline()

        # Finally, save the file.

        self.file = file
