   # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BTress:
    """  (Problem 988) You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

    Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

    As a reminder, any shorter prefix of a string is lexicographically smaller.

    For example, "ab" is lexicographically smaller than "aba".
    A leaf of a node is a node that has no children."""
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
       

        lex_translation = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'
                            ,'w','x','y','z']
        if root.left is None and root.right is not None:
            smallest_array = self.get_smallest_array_DFS(root.right)
            smallest_array.append(root.val)
        elif root.right is None:
            smallest_array = self.get_smallest_array_DFS(root.left)
            smallest_array.append(root.val)
        else:
            smallest_array = self.get_smallest_array_DFS(root, 1)
  
        output = ''
        for val in smallest_array:
            output+=lex_translation[val] 
      
        return output
       

    def get_smallest_array_DFS(self,root, isroot=0):

       
        if root is None:
          
            return []
        elif root.left is None and root.right is None:
        
            return [root.val]
        left_array = []
        right_array = []
        if root.left is not None:
            left_array = self.get_smallest_array_DFS(root.left)
        if root.right is not None: 
            right_array=self.get_smallest_array_DFS(root.right)

        if not len(left_array) and len(right_array):
            
            right_array.append(root.val)
            return right_array
        elif  len(left_array) and not len(right_array):
       
            left_array.append(root.val)
            return left_array

        
        right_array.append(root.val)
        left_array.append(root.val)
        i = 0
        while i < len(left_array) and i <len(right_array):
            if left_array[i] < right_array[i]:
                return left_array
            elif left_array[i]>right_array[i]:
                return right_array
            i+=1
        
        
        if isroot:
            return right_array if len(right_array)<len(left_array) else left_array
        elif len(left_array)>len(right_array):
            return left_array
        else:
            return  right_array
      
            
        
    
    