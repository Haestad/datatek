""" This module is a unit test for containers module. """

import unittest
from containers import Container, Stack, Queue


class TestContainer(unittest.TestCase):
    """ This class is a unit test for the Container class in the containers module.
    Tests the methods that are shared between subclasses. """

    def setUp(self):
        self.container = Container()
        self.container.push("item 1")
        self.container.push("item 2")
        self.container.push("item 3")

    def test_not_empty(self):
        """ Tests that is_empty() returns false. """
        self.assertFalse(self.container.is_empty())

    def test_container_size(self):
        """ Tests that size() returns the amount of elements in the container. """
        self.assertEqual(3, self.container.size())

    def test_push_element(self):
        """ Tests that you can push an element to the container,
         and that the size updates itself.
         """
        self.container.push("item 4")
        self.assertEqual(4, self.container.size())

    def test_pop_peek_not_implemented(self):
        """ Tests that peek() and pop() raises NotImplementedError. """
        with self.assertRaises(NotImplementedError):
            self.container.peek()
        with self.assertRaises(NotImplementedError):
            self.container.pop()


class TestStack(unittest.TestCase):
    """ This class is a unit test for the Stack class in the containers module.
     Tests subclass specific methods.
     """

    def setUp(self):
        self.stack = Stack()
        self.stack.push("item 1")
        self.stack.push("item 2")
        self.stack.push("item 3")

    def test_peek_element(self):
        """ Tests that peek() returns the last element of the stack,
         and that the stack size stays the same.
         """
        self.assertEqual("item 3", self.stack.peek())
        self.assertEqual(3, self.stack.size())

    def test_pop_element(self):
        """ Tests that pop() returns the last element of the stack,
        and that the stack size is reduced by one.
        """
        self.assertEqual("item 3", self.stack.pop())
        self.assertEqual(2, self.stack.size())

    def test_pop_all(self):
        """ Tests that pop() returns the last element until the stack is empty,
        and that the stack size decreases by one for each pop() call. """
        last_item = 3
        while not self.stack.is_empty():
            self.assertEqual(f'item {last_item}', self.stack.pop())
            last_item -= 1
            self.assertEqual(last_item, self.stack.size())
        self.assertTrue(self.stack.is_empty())

    def test_empty_stack(self):
        """ Tests that both peek() and pop() raises AssertionError when stack is empty. """
        while not self.stack.is_empty():
            self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        with self.assertRaises(AssertionError):
            self.stack.peek()
        with self.assertRaises(AssertionError):
            self.stack.pop()


class TestQueue(unittest.TestCase):
    """ This class is a unit test for the Queue class in the containers module.
     Tests subclass specific methods."""

    def setUp(self):
        self.queue = Queue()
        self.queue.push("item 1")
        self.queue.push("item 2")
        self.queue.push("item 3")

    def test_peek_element(self):
        """ Tests that peek() returns the first element of the queue,
         and that the queue size stays the same.
         """
        self.assertEqual("item 1", self.queue.peek())
        self.assertEqual(3, self.queue.size())

    def test_pop_element(self):
        """ Tests that pop() returns the last element of the queue,
        and that the queue size is reduced by one.
        """
        self.assertEqual("item 1", self.queue.pop())
        self.assertEqual(2, self.queue.size())

    def test_pop_all(self):
        """ Tests that pop() returns the first element until the queue is empty,
        and that the queue size decreases by one for each pop() call. """
        first_item = 1
        while not self.queue.is_empty():
            self.assertEqual(f'item {first_item}', self.queue.pop())
            first_item += 1
            # Need to use 4, since first_item starts at 2.
            self.assertEqual(4 - first_item, self.queue.size())
        self.assertTrue(self.queue.is_empty())

    def test_peek_after_adding_element(self):
        """ Tests that the first element of the queue stays the same
         after adding an element to the queue.
         """
        current_first = self.queue.peek()
        self.queue.push("item 4")
        self.assertEqual(current_first, self.queue.peek())

    def test_empty_queue(self):
        """ Tests that both peek() and pop() raises AssertionError when queue is empty. """
        while not self.queue.is_empty():
            self.queue.pop()
        self.assertTrue(self.queue.is_empty())
        with self.assertRaises(AssertionError):
            self.queue.peek()
        with self.assertRaises(AssertionError):
            self.queue.pop()
