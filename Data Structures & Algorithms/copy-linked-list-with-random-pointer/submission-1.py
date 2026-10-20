"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToMap = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToMap[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToMap[cur]
            copy.next = oldToMap[cur.next]
            copy.random = oldToMap[cur.random]
            cur = cur.next
        
        return oldToMap[head]


        