# Binary Tree
"""
in-order, pre-order and post-order traversal of binary tree

              A
             / \
            B   C
           / \   \
          D   E   F
         / \
        G   H

    in-order
    G->D->H->B->E->A->F->C
    pre-order
    A->B->D->G->H->E->C->F
    post-order
    G->H->D->E->B->F->C->A
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, TypeVar, Generic

T = TypeVar('T')


@dataclass
class Node:
    data: Generic[T]
    left: Optional[Node] = None
    right: Optional[Node] = None


@dataclass
class Tree:
    root: Node

    def in_order(self, node: Optional[Node]) -> None:
        if node:
            self.in_order(node.left)
            print(node.data, end="->")
            self.in_order(node.right)

    def pre_order(self, node: Optional[Node]) -> None:
        if node:
            print(node.data, end="->")
            self.in_order(node.left)
            self.in_order(node.right)

    def post_order(self, node: Optional[Node]) -> None:
        if node:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.data, end="->")

    def height(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        l_height = self.height(node.left)
        r_height = self.height(node.right)

        return max(l_height, r_height) + 1

    def root_path(self, node: Optional[Node]):
        if not node:
            return False
        curr = self.root
        while curr:
            if curr.data == node.data:
                return True
            else:
                self.root_path(curr.left)
                self.root_path(curr.right)

    def path_sum(self, node: Optional[Node]):
        pass

    def mirror(self, node: Optional[Node]) -> Node:
        pass

    def path_sum_nodes(self, node1: Optional[Node], node2: Optional[Node]):
        pass

    def serialize(self, node: Optional[Node]) -> str:
        """serialize the tree to a list
            inorder output
        Args:
            node (Optional[Node]): root node

        Returns:
            list: output string
        """

        def _serialize(node: Optional[Node], output: list):
            if not node:
                output += "None,"
            else:
                output += node.data + ','
                output = _serialize(node.left, output)
                output = _serialize(node.right, output)

            return output

        return _serialize(node, "")


if __name__ == "__main__":
    h = Node("H")
    g = Node("G")
    f = Node("F")
    e = Node("E")
    d = Node("D", g, h)
    c = Node("C", f)
    b = Node("B", d, e)
    a = Node("A", b, c)

    tree = Tree(a)
    print("\nin-order")
    tree.in_order(a)
    print("\npre-order")
    tree.pre_order(a)
    print("\npost-order")
    tree.post_order(a)

    # h = Node(1)
    # g = Node(2)
    # f = Node(3)
    # e = Node(4)
    # d = Node(3, g, h)
    # c = Node(2, f)
    # b = Node(4, d, e)
    # a = Node(1, b, c)

    # tree = Tree(a)
    # print("\nin-order")
    # tree.in_order(a)
    print("\nSerialized Tree: ")
    print(tree.serialize(a))
    print("\nHeight from root is: ")
    print(tree.height(a))
    print("\nPath exits from D to A: ")
    print(tree.root_path(d))
