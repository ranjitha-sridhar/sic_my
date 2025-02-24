class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_lists:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def display(self):
        current=self.head
        if current is None:
            print("Empty LIST")
        while current:
            print(current.data,end=" ")
            current=current.next
    def add_pos(self,data,pos):
        new_node=Node(data)
        if pos<=0:
            print("Invalid POsition")
        if pos==-1:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        index=1
        while current and index<current-1:
            current=current.next
            index+=1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next=current.next
        current.next=new_node
    def del_pos(self,pos):
        if self.head is None:
            print("The list is empty")
            return
        if pos<=0:
            print("Invalid Position")
            return
        if pos==1:
            del_data=self.head.data
            self.head=self.head.next
            print(f"Deleted data is {del_data}")
            return
        current=self.head
        index=1
        while current and index<pos-1:
            current=current.next
            index+=1
        if current is None or current.next is None:
            print("position out of bounds")
            return
        del_data=current.next.data
        current.next=current.next.next
        print(f"Deleted node is {del_data}")
    def display_rev(self):
        def rev_display_node(node):
            if node is None:
                return
            rev_display_node(node.next)
            print(node.data,end=" ")
        if not self.head:
            print("The linked list is empty")
            return
        print("The reversed list is")
        rev_display_node(self.head)
if __name__=="__main__":
    llist=linked_lists()
    llist.append(40)
    llist.append(20)
    llist.append(80)
    print("Original list ")
    llist.display()
    print("Reversed list is")
    llist.display_rev()