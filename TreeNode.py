# Defination for a binary tree node
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
########################################################
def findSecondMinimumValue(root):
    row = [root]
    minlist = [root.val,-1]
    while row:
        for r in row:
            if r.val < minlist[0]:
                minlist[1] = minlist[0]
                minlist[0] = r.val
            elif minlist[0] < r.val < minlist[1]:
                minlist[1] = r.val
        row = [r for r in [root.left,root.right] for root in row if r]
        print row
    return minlist[1]

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    if not root:
        return 0
    def helper(root,sum):
        if not root:
            return 0
        if root.val == sum:
            return helper(root.left,0)+helper(root.right,0)+1
        else:
            return helper(root.left,sum-root.val)+helper(root.right,sum-root.val)
    return pathSum(root.left,sum)+pathSum(root.right,sum)+helper(root,sum)



#########################################################
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.left = TreeNode(-2)

print pathSum(root,8) 