from __future__ import annotations
from typing import TypeVar, List
from random import random

T = TypeVar('T')
"""
              1
             / \
            2   3
           / \   \
          4   5   6
         / \
        7   8

Preorder:
Inorder:
Postorder:
"""


class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x: T, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Features(object):
    def inorder_recurrsive(self, root: TreeNode) -> List[T]:
        result = []
        if not root:
            return result

        def _inorder_helper(node, result):
            if node:
                _inorder_helper(node.left, result)
                result.append(node.val)
                _inorder_helper(node.right, result)

        _inorder_helper(root, result)
        return result

    def preorder_recurrsive(self, root: TreeNode) -> List[T]:
        result = []
        if not root:
            return result

        def _preorder_helper(node, result):
            if node:
                result.append(node.val)
                _preorder_helper(node.left, result)
                _preorder_helper(node.right, result)

        _preorder_helper(root, result)
        return result

    def postorder_recurrsive(self, root: TreeNode) -> List[T]:
        result = []
        if not root:
            return result

        def _postorder_helper(node, result):
            if node:
                _postorder_helper(node.left, result)
                _postorder_helper(node.right, result)
                result.append(node.val)

        _postorder_helper(root, result)
        return result

    def inorder_iterative(self, root: TreeNode) -> List[T]:
        result = []
        if not root:
            return result
        stack = [root, ]
        while stack:
            node = stack.pop()
            if node:
                # reversed for stack ordering
                stack.append(node.left)
                result.append(node.val)
                stack.append(node.right)

        return result

    def create_dummy_tree(self) -> TreeNode:
        a = TreeNode(7)
        b = TreeNode(8)
        c = TreeNode(4, a, b)
        d = TreeNode(5)
        e = TreeNode(2, c, d)
        f = TreeNode(6)
        g = TreeNode(3, None, f)
        h = TreeNode(1, e, g)
        return h


f = Features()
root = f.create_dummy_tree()
print(f"Inorder traversal  : {f.inorder_recurrsive(root)}")
print(f"Preorder traversal : {f.preorder_recurrsive(root)}")
print(f"Postorder traversal: {f.postorder_recurrsive(root)}")
print(f"Inorder traversal  : {f.inorder_iterative(root)}")
