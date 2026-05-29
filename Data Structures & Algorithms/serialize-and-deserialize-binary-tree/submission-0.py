# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        
        def preorder(root):
            if not root:    #Base case(We want to keep track of null!)
                serialized.append("NULL")
                return None

            serialized.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            return root
        
        preorder(root)
        return ",".join(serialized)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        l = data.split(",")
        i = 0
        def build(i ,node):
            if l[i] == "NULL":
                return i+1, None
            
            root = TreeNode(l[i])
            i, root.left = build(i+1, root)
            i, root.right = build(i, root)
            return i, root

        _, root = build(0, None)
        return root




