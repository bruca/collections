class Vector:
    """Vector is a growable array of objects like an array
    """
    def __init__(self):
        self.__arr__ = []

    def add(self, e):
        """Append an element
        """
        self.__arr__.append(e)

    def clear(self):
        """Clear array
        """
        self.__arr__.clear()

    def is_empty(self):
        return len(self.__arr__) == 0

    def remove(self, index):
        """Remove element at given index
        """
        self.__arr__.pop(index)
