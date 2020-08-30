# 236. Lowest Common Ancestor of a Binary Tree
# 236. 二叉树的最近公共祖先

'''
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
1. 当left和right同时为空：说明root的左/右子树中都不包含p,q，返回null；
2. 当left和right同时不为空：说明p,q分列在root的异侧（分别在左/右子树），因此root为最近公共祖先，返回root；
3. 当left为空，right不为空：p,q都不在root 的左子树中，直接返回right。具体可分为两种情况：
    p,q其中一个在root的右子树中，此时right指向p（假设为p）；
    p,q两节点都在root的右子树中，此时的right指向最近公共祖先节点；
4. 当left不为空，right为空：与情况 3. 同理；
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root # 当left和right同时为空：说明root的左/右子树中都不包含p,q，返回null；
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return
        if not left: return right
        if not right: return left
        return root




'''
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-di-gui-by-xu-chen-chen-d/
如果两边各有一个p或q，那么答案应该直接是根节点root。
如果都在左，则答案是left。
如果都在右，则答案是right。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left




class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left