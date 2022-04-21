import unittest

class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0


    def __getitem__(self, index):
        current = self.__head
        if index < 0:
            index = self.__len + index
        for _ in range(index):
            if current is None or current.has_next() is False:
                raise IndexError
            current = current.get_next()
        return current.value





    def __len__(self):
        return self.__len


    def add(self, value, index=None):
        new_item = LinkedListItem(value)
        if index is None:

            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item

        if index is not None:
            if (index < 0):
                print("enter correct index")
            elif (index == 0):
                if not self.__head:
                    self.__head = new_item
                    self.__tail = new_item
                else:
                    new_item.set_next(self.__head)
                    self.__head = new_item


            else:
                if self.__head is not None:
                    pointer = self.__head
                    for i in range(0, index - 1):
                        if pointer is not None:
                            pointer = pointer.get_next()
                    if pointer is not None:
                        new_item.set_next(pointer.get_next())
                        pointer.set_next(new_item)
                        if index == self.__len:
                            self.__tail = new_item
                    else:
                        print("Not enough items to insert the new item at this index")

                else:
                    print("Empty class. You can only insert your item with the 0 index")

        self.__len += 1

    def add_all(self, values, index=None):
            if index is None:
                index = self.__len
            if (index < 0):
                print("enter correct index")

            for value in values:
                new_item = LinkedListItem(value)

                if (index == 0):
                    if not self.__head:
                        self.__head = new_item
                        self.__tail = new_item
                    else:
                        new_item.set_next(self.__head)
                        self.__head = new_item


                else:
                    if self.__head is not None:
                        pointer = self.__head
                        for i in range(0, index - 1):
                            if pointer is not None:
                                pointer = pointer.get_next()
                        if pointer is not None:
                            new_item.set_next(pointer.get_next())
                            pointer.set_next(new_item)
                            if index == self.__len:
                                self.__tail = new_item
                        else:
                            print("Not enough items to insert the new item at this index")

                    else:
                        print("Empty class. You can only insert your item with the 0 index")

                self.__len += 1
                index += 1



    def pop(self, index=None):
        if index is None:
            index = self.__len-1
        if index is not None:
            if (index < 0):
                print("enter correct index")
            elif index == 0:
                if self.__head is not None:
                    pointer = self.__head
                    pointer_next = pointer.get_next()
                    if pointer_next is not None:
                        self.__head = pointer_next
                        self.__len = self.__len - 1

                    else:
                        self.__head = None
                        self.__tail = None
                        self.__len = 0
                    return pointer.value

            elif index > 0:
                if self.__head is not None:
                    pointer = self.__head
                    for i in range(0, index - 1):
                        if pointer is not None:
                            pointer = pointer.get_next()
                    if pointer is not None:
                        pointer_to_remove = pointer.get_next()
                        if pointer_to_remove is not None:
                            pointer_next = pointer_to_remove.get_next()
                            if pointer_next is not None:
                                pointer.set_next(pointer_next)
                            else:
                                pointer.set_next(None)
                                self.__tail = pointer
                            return pointer_to_remove.value
            self.__len -= 1

    def remove_last_occurence(self, element):
        if element not in self:
            print("No such element")
        else:
            last = None
            for i, k in enumerate(self):
                if element == k:
                    last = i
            self.pop(last)



    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value

class TestLinkedList(unittest.TestCase):

    def test_add(self):
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add(12)
        items.add(13)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[3], 13)

    def test_add_all(self):
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add_all([1,2,3],1)
        self.assertEqual(items[1], 1)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[4], 11)

    def test_pop(self):
        items = LinkedList()
        items.add(1)
        items.add(2)
        items.add(3)
        items.add(4)
        self.assertEqual(items.pop(1), 2)
        self.assertEqual(items.pop(), 4)

    def test_remove_last_occurence(self):
        items = LinkedList()
        items.add(1)
        items.add(2)
        items.add(3)
        items.remove_last_occurence(1)
        self.assertEqual(items[0], 2)

if __name__ == "__main__":
    unittest.main()

