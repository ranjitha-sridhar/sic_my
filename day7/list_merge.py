class node:
    def __init__(self, data):
        self.data = data
        self.link = None

class linked_list:
    def __init__(self, num):
        self.head = None
        print(f'List-{num} is created')

    def create_node(self, data):
        node_instance = node(data)
        return node_instance

    def add_node_at_front(self, data):
        if self.head is None:
            self.head = self.create_node(data)
        new_node = self.create_node(data)
        new_node.link = self.head
        self.head = new_node

def create_list(num):
    list_instance = linked_list(num)
    print(f'Creating List-{num}')
    while True:
        data = input('Enter data of the new node: ')
        list_instance.add_node_at_front(data)
        choice = input('Enter 1 to add node, other number to stop: ')
        if choice == '1':
            continue
        break
    return list_instance

def check_if_converges(list1, list2):
    if list1.head is None or list2.head is None:
        print('Lists do not converge')
        return
    temp1 = list1.head
    temp2 = list2.head
    count = 0
    while temp1 is not None and temp2 is not None:
        if temp1.link == temp2.link:
            return count
        temp1 = temp1.link
        temp2 = temp2.link
        count += 1
    return -1

list1 = create_list(1)
list2 = create_list(2)
position = check_if_converges(list1, list2)
if position == -1:
    print('The lists do not converge')
else:
    print(f'The lists converge at position-{position}')
