class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def solution(self, root):
        lists = []
        if root is None:
            return lists

        def bfs( root, level):
            if (len(lists) == level):
                lists.append([])

            if root:
                lists[level].append(root.value)

            if root.left:
                bfs(root.left, level+1)

            if root.right:
                bfs(root.right, level+1)

        bfs(root, 0)
        return lists



ro
ot = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print (root.solution(root))
