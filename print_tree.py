# Defination for a binary tree node
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
########################################################

def printTree(root):
    def depth(root):
        if not root: return 0
        return max(depth(root.left),depth(root.right))+1
    d = depth(root)
    res = [[""]*(2**d-1) for i in xrange(d)]
    def helper(root,s,e,d):
        if not root: return
        c = (s+e)/2
        res[-d][c] = str(root.val)
        # print res
        if root.left:
            helper(root.left,s,c-1,d-1)
        if root.right:
            helper(root.right,c+1,e,d-1)
    helper(root,0,2**d-2,d)
    return res


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.left = TreeNode(-2)

print printTree(root) 