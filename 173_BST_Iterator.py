"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        r = root
        self.stack = []
        while r:
            self.stack.append(r)
            r = r.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        
        res = self.stack.pop()
        r = res.right
        while r:
            self.stack.append(r)
            r = r.left
        return int(res.val)
        