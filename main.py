from itertools import zip_longest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pop(self):
        if not self.head:
            return None
        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.data
        current.next = None
        return value

    def display(self):
        print("Head -> ", end="")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        head = self.head
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def __str__(self):
        return self.display()

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


first_list = list(map(int, input("Enter the first list: ").split()))
second_list = list(map(int, input("Enter the second list: ").split()))

first_linked_list = LinkedList()
second_linked_list = LinkedList()

for item1, item2 in zip_longest(first_list, second_list, fillvalue=0):
    first_linked_list.append(item1)
    second_linked_list.append(item2)

result = LinkedList()
carry = 0
for item1, item2 in zip(first_linked_list, second_linked_list):
    sum_of_digits = item1 + item2 + carry
    carry = sum_of_digits // 10
    result.append(sum_of_digits % 10)

result.reverse()
result.display()
