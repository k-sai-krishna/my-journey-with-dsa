def del_middle(self):
        slow = None
        fast = self.head
        while fast is not None and fast.next is not None:
            if slow is None:
                slow = self.head
            else:
                slow = slow.next
            fast = fast.next.next
        if slow == None:
            self.head = None
            return 
        slow.next = slow.next.next
#logic
#same logic as finding middle node but here we find its preceding and swap the addresses
#achieved by start slow from None
