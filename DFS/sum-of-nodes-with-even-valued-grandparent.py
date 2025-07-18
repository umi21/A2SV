"""
    SUM OF NODES WITH EVEN-VALUED GRANDPARENTS

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. 
If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.


Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the 
blue nodes are the even-value grandparents.

Example 2:

Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

"""


from typing import Optional
from definitions import TreeNode


class Solution:
    def dfs(self, subtree, parent):
        ans = 0
        if subtree.left:
            ans += self.dfs(subtree.left, subtree)
            if parent.val%2==0:
                ans += subtree.left.val
        if subtree.right:
            ans+= self.dfs(subtree.right, subtree)
            if parent.val%2==0:
                ans += subtree.right.val
        return ans
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        superParent = TreeNode(val=3,left=root)
        ans = self.dfs(root, superParent)
        return ans