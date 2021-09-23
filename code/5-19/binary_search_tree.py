# Binary Search Tree
"""
                27
             /     \
            14     35
           / \    /  \
          10  9  31 42


    Returns:
        [type]: [description]
    """
from __future__ import annotations
from typing import TypeVar

T = TypeVar('T')


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value: T) -> None:
        """insert into a BST

        Args:
            value ([T]): [description]
        """
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

    def search(self, value: T) -> bool:
        if not self.data:
            return False
        else:
            if value < self.data:
                if self.left is None:
                    return False
                return self.left.search(value)
            elif value > self.data:
                if self.right is None:
                    return False
                return self.right.search(value)
            else:
                return True

    def delete(self, value: T) -> None:
        if not self.data:
            return None
        else:
            if value < self.data:
                pass

    def print(self) -> T:
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
print(root.search(7))
print(root.search(14))
print(root.print())
