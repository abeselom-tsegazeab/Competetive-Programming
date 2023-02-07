class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None:
                return head
        node = head
        length = 1
        while node.next:
            node = node.next
            length +=1
            
        m =  k % length
        if m == 0:
            return head
        else:
            cur = head
            for i in range(length-m-1):   
                cur = cur.next
            newHead = cur.next
            cur.next = None
            node.next = head
        return newHead
            
