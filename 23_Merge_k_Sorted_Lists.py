"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


def mergeKLists(self, lists):
    from heapq import heappush, heappop, heapreplace, heapify
    dummy = node = ListNode(0)
    h = [(n.val, n) for n in lists if n]
    heapify(h)
    while h:
        v, n = h[0]
        if n.next is None:
            heappop(h) #only change heap size when necessary
        else:
            heapreplace(h, (n.next.val, n.next))
        node.next = n
        node = node.next

    return dummy.next