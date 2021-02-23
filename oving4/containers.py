""" This module contains different containers for storing data when operating the calculator. """


class Container:
    """ This class is a superclass for all the containers, contains all relevant methods. """
    def __init__(self):
        self.items = []

    def size(self):
        """ Returns the number of items in self.items. """
        return len(self.items)

    def is_empty(self):
        """ Returns True if self.items is empty, or else returns False. """
        if not self.items:
            return True
        return False

    def push(self, item):
        """ Adds item to the end of self.items. """
        self.items.append(item)

    def pop(self):
        """ Pops off the correct element of self.items, and returns it.
        The method differs between the subclasses, hence is not implemented.
        """
        raise NotImplementedError

    def peek(self):
        """ Peeks at the correct element of self.items, and returns it
        The method differs between the subclasses, hence is not implemented.
        """
        raise NotImplementedError


class Stack(Container):
    """ This class is a Stack container, following the FIFO(First-In, First-Out) method. """
    def peek(self):
        """ Peeks at the last element of the list, and returns it. """
        assert not self.is_empty()
        return self.items[-1]

    def pop(self):
        """ Pops off the last element of the list, and returns it. """
        assert not self.is_empty()
        return self.items.pop()


class Queue(Container):
    """ This class is a Queue container, following the LIFO(Last-in, First-Out) method. """
    def peek(self):
        """ Peeks at the first element of the list, and returns it. """
        assert not self.is_empty()
        return self.items[0]

    def pop(self):
        """ Pops off the first element of the list, and returns it. """
        assert not self.is_empty()
        return self.items.pop(0)
