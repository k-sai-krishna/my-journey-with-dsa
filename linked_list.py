class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        print("Linked List is :")
        if temp == None:
            print("List is empty")
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def ins_prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        # return self.head
    def ins_append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        # return self.head
    def ins_before(self,value,key):
        if self.head is None:
            print("List is empty,this action is not possible.")
            return
        if self.head.value is key:
            self.ins_prepend(value)
            return
        temp = self.head
        while temp.next.value is not key:
            temp = temp.next
            if temp.next is None:
                print("Enter a valid key")
                return
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
    def ins_after(self,value,key):
        if self.head is None:
            print("List is empty,this action is not possible.")
            return
        if self.tail.value is key:
            self.ins_append(value)
            return
        temp = self.head
        while temp.value is not key:
            temp = temp.next
            if temp == None:
                print("Enter a valid key")
                return
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
    def del_pop_first(self):
        if self.head is None:
            print("Deletion is not possible")
            return None
        del_key = self.head.value
        if self.head.next is None:
            self.head = self.tail = None
            return del_key
        self.head = self.head.next
        return del_key
    def del_pop_last(self):
        if self.head is None:
            print("Deletion is not possible")
            return None
        del_key = self.tail.value
        temp = self.head
        if temp is self.tail:
            self.del_pop_first()
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        return del_key
    def del_given(self,key):
        if self.search(key) is None:
            print("Enter a valid key")
            return
        del_key = key
        # if self.head is None:
        #     print("Deletion is not possible")
        #     return
        if self.head.value == key:
            self.del_pop_first()
            return del_key
        if self.tail.value == key:
            self.del_pop_last()
            return del_key
        temp = self.head
        while temp.next.value is not key:
            temp = temp.next
        temp.next = temp.next.next
        return del_key
    def search(self,key):
        if self.head == None:
            return -1
        temp = self.head
        while temp.value is not key:
            temp = temp.next
            if temp is None:
                return None
        return temp
    def del_before(self,key):
        if self.search(key) is None:
            print("Enter a valid key")
            return
        if self.head.value == key:
            print("Deletion is not possible")
            return 
        if self.head.next.value == key:
            del_key = self.del_pop_first()
            return del_key
        temp = self.head
        while temp.next.next.value is not key:
            temp = temp.next
            # if temp.next.next is None:
            #     print("Key is not found")
            #     return
        del_key = temp.next.value
        temp.next = temp.next.next
        return del_key
    def del_after(self,key):
        temp = self.search(key)
        if temp is None:
            print("Enter a valid key")
            return
        if self.tail == temp:
            print("Deletion is not possible")
            return
        if temp.next is self.tail:
            del_key = self.del_pop_last()
            return del_key
        del_key = temp.next.value
        temp.next = temp.next.next
        return del_key
    def reverse(self):
        temp = self.head
        prev = None
        next = None
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
        return True
            
def driver():
    n = input("Do you want to create a linked list?(yes/no) :")
    if n.lower().strip() == 'yes':
        try:
            f = int(input("Enter first element :"))
        except (TypeError,ValueError):
            print("Provide integer data only!!")
            exit()
        list1 = LinkedList(f)
    else:
        #creating a linked list with four nodes
        # list1 = LinkedList(1)
        # list1.ins_append(2)
        # list1.ins_append(3)
        # list1.ins_append(4)
        # list1.print_list()
        print("\nWhy don't you create a linked list and play with it!?\nCompile me again if you want to..!!")
        exit()
    while True:
        try:
            n = int(input("\n\n1.Print\n2.Insertion\n3.Deletion\n4.Search\n5.Reverse the LL\n0.Exit\nEnter your choice :"))
        except (ValueError , TypeError):
            print("\nEnter a valid number")
        if n == 1:
            list1.print_list()
        elif n == 2:
            try:
                val = int(input("Enter the value :"))
            except (ValueError, TypeError):
                print("\nEnter a valid number")
            try:
                m = int(input("\n\nInsertion\n1.Prepend\n2.Append\n3.Before given key\n4.After given key\nOther.Back\nEnter your choice :"))
            except (ValueError,TypeError):
                print("\nEnter a valid number")
            if m == 1:
                list1.ins_prepend(val)
            elif m == 2:
                list1.ins_append(val)
            elif m == 3:
                try:
                    key = int(input("Enter the key :"))
                except(ValueError, TypeError):
                    print("\nEnter a valid number")
                list1.ins_before(val,key)
            elif m == 4:
                try:
                    key = int(input("Enter the key :"))
                except(ValueError, TypeError):
                    print("\nEnter a valid number")
                list1.ins_after(val,key)
            else:
                print("\nYou have entered the main menu")
                continue
        elif n == 3:
            try:
                m = int(input("\n\nDeletion\n1.Pop first\n2.Pop Last\n3.Before given key\n4.After given key\n5.Given key\nOther.Back\nEnter your choice :"))
            except(ValueError,TypeError):
                print("\nEnter a valid number")
            if m == 1:
                del_key = list1.del_pop_first()
                if del_key is not None:
                    print(f"Deleted key is {del_key}.")
            elif m == 2:
                del_key = list1.del_pop_last()
                if del_key is not None:
                    print(f"Deleted key is {del_key}.")
            elif m == 3:
                #before given key
                try:
                    key = int(input("Enter the key value:"))
                except(ValueError, TypeError):
                    print("\nEnter a valid number")
                del_key = list1.del_before(key)
                if del_key:
                    print(f"Deleted key is {del_key}.")
            elif m == 4:
                try:
                    key = int(input("Enter the key value:"))
                except(ValueError, TypeError):
                    print("\nEnter a valid number")
                del_key = list1.del_after(key)
                if del_key:
                    print(f"Deleted key is {del_key}.")
            elif m == 5:
                try:
                    key = int(input("Enter the key value:"))
                except(ValueError, TypeError):
                    print("\nEnter a valid number")
                del_key = list1.del_given(key)
                if del_key:
                    print(f"Deleted key is {del_key}")
            else:
                print("\nYou have entered the main menu")
                continue
        elif n == 4:
            try:
                key = int(input("Enter the key to search :"))
            except(ValueError, TypeError):
                print("\nEnter a valid number")
            ad = list1.search(key)
            if ad == -1:
                print("Linked list is empty")
            elif ad is None:
                print(f"Your key:{key} is not found")
            else:
                print(f"Your key: {key} is found at {ad}")
        elif n == 5:
            #reverse the ll
            status = list1.reverse()
            if status is True:
                print("Your Linked list has been reversed!!")
        elif n == 0:
            break
        else:
            print("\nEnter a VAlid number")
if __name__== '__main__':
    driver()
