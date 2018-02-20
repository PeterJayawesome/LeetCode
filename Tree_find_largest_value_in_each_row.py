import pprint
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test(root):
	if not root:
		return []
	row = [root]
	res = []
	while row:
	    res.append(max([r.val for r in row]))
	    a = [s for r in row for s in [r.left,r.right] if s!=None]
	    row = a
	    pprint.pprint([r.val for r in row]) 
	return res

import collections
def findFrequentTreeSum(root):
	if not root:
		return []
	val = collections.Counter()
	def Treesum(root):
	    if not root:
	        return 0
	    sum = Treesum(root.left)+Treesum(root.right)+root.val
	    val[sum] += 1
	    return sum
	Treesum(root)
	max_count = max(val.itervalues())
	return [k for k,v in val.iteritems() if v == max_count]
	# return val


root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
# print root.val
print findFrequentTreeSum(root)