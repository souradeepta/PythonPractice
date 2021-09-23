# Stack
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def empty(self) -> bool:
        return not self.items

    def get_max(self) -> T:
        return max(self.items)

    def print(self) -> None:
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i], " ")


# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
stack.push(4)
stack.push(12)
stack.push(25)
stack.push(22)
stack.pop()
stack.push(3)
stack.print()
print(stack.get_max())
