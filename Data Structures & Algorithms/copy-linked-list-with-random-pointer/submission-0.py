"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # hashmap 2 pass, time O(n), space O(n)
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     oldToCopy = {None: None}

    #     curr = head
    #     while curr:
    #         copy = Node(curr.val)
    #         oldToCopy[curr] = copy
    #         curr = curr.next

    #     curr = head
    #     while curr:
    #         copy = oldToCopy[curr]
    #         copy.next = oldToCopy[curr.next]
    #         copy.random = oldToCopy[curr.random]
    #         curr = curr.next

    #     return oldToCopy[head]

    # hashmap 1 pass, time O(n), space O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]