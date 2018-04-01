class List:
    """List is an array of objects
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
