# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 105. 从前序与中序遍历序列构造二叉树
'''
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/
通过先序遍历我们可以找到root，知道inorder中，当前root的左侧的所有点就是其左子树，root的右侧的所有点就是当前root的右子树，再递归对当前root的左右子树进行构造。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0]) #根据preorder可以确定root
        idx = inorder.index(preorder[0]) #根据root可以划分出左右子树
        # 对左右子树递归
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root