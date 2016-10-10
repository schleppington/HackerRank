def check_binary_search_tree_(root):
    return checkBST(root, float('inf'), float('-inf'))

def checkBST(root, max, min):
    if root is None:
        return True
    if root.data < min or root.data > max:
        return False
    return (checkBST(root.left, root.data -1, min) and checkBST(root.right, max, root.data+1))
