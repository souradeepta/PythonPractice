# Tree Traversal
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, TypeVar, Generic, List

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

    def serialize(self, node: Optional[Node]) -> List:
        serialized_tree = []
        if node:
            self.serialize(node.left)
            serialized_tree.append(node.data)
            self.serialize(node.right)
        return serialized_tree


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

    h = Node(1)
    g = Node(2)
    f = Node(3)
    e = Node(4)
    d = Node(3, g, h)
    c = Node(2, f)
    b = Node(4, d, e)
    a = Node(1, b, c)

    tree = Tree(a)
    print("\nin-order")
    tree.in_order(a)
    print(tree.serialize(a))