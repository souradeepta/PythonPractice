# Linear Search
# The time complexity of linear search is O(n), meaning that
# the time taken to execute increases with the number of items
# in our input list.
# does not require that a collection be sorted before searching begins.

def linear_search(input_list: list, target: int) -> int:
    for index, value in enumerate(input_list):
        if value == target:
            return index
    return -1


print(linear_search([1, 2, 3, 4, 5, 6, 7], 3))
print(linear_search([1, 2, 3, 4, 5, 6, 7], 10))
print(linear_search([1, -2, 3, 12, 5, 16, 7], -2))
print(linear_search([], 2))
