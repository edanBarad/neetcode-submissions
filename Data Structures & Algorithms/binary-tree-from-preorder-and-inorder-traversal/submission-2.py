class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Base cases
        if not inorder:  
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        indexOfRoot = inorder.index(preorder[0])
        
        rightChild = 1 + indexOfRoot
        
        root.left = self.buildTree(preorder[1:rightChild], inorder[:indexOfRoot])
        root.right = self.buildTree(preorder[rightChild:], inorder[indexOfRoot+1:])
        return root