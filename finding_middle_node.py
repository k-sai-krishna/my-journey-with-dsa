def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
#logic here is:
#slow, moves 1 node for a loop
#fast, moves 2 node for a loop
