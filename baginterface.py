"""
Author: YOUR NAME GOES HERE
File: baginterface.py

Speficitactions of the methods for all bag classes.  Running this code will
not produce any results, but it shows the headers and docstrings of the methods
that MUST be included or supported in any bag class.
"""

class BagInterface(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        return len(self) == 0
            
    
    def __len__(self):
        
        return len(self) 

    def __str__(self):
        """Returns the string representation of self."""
        return str(self)

    def __iter__(self):
        """Supports iteration over a view of self."""
        for i in (self):
            return self[i]

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        newBag = self + other
        return newBag

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if len(self) is not len(other):
            return False
        for i in self:
            if self[i] is not other[i]:
                return False
            
        return True

    # Mutator methods
    def clear(self):
        self = {}
        

    def add(self, item):
        
        return self + item

    def remove(self, item):
        try: 
            item in self
        except KeyError:
            print ("Item not in self")


        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        pass
