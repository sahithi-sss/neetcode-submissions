# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        #left part of inorder (div at ind) is left subtree and viceversa
        ind = inorder.index(root_val)
        #inorder[0:ind] = left subtree || inorder[ind+1:] = right
        #preorder[1:len(left_sub)+1] -> left || preorder[1+len(left_sub)+1:] -> right

        left_sub_inorder = inorder[0:ind]
        right_sub_inorder = inorder[ind+1:]
        lng = len(left_sub_inorder)
        root.left = self.buildTree(preorder[1:lng+1],left_sub_inorder)
        root.right = self.buildTree(preorder[1+lng:],right_sub_inorder)
        return root