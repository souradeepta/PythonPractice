from typing import List


def selection_sort(input: List) -> List:
    if not input:
        return None
    
    for i in range(len(input)):
        min_index =i
        for j in range(i+1, len(input)):
            if input[j] < input[min_index]:
                min_index = j
        
        input[i], input[min_index] = input[min_index], input[i]
        
    return input


if __name__ == "__main__":
    input_integers = [1, 2, 3, 4]
    input_integer_repeats = [1, 2, 2, 4, 9, 12]
    input_strings = ["1who", "2what", "3where"]
    input_floats = [0.222, 0.44444444444444444444444444444, 0.9]

    print(
        f"target 2 on list {input_integers} is at {selection_sort(input_integers)}")
    print(
        f"target 2 on list {input_integer_repeats} is at {selection_sort(input_integer_repeats)}")
    print(
        f"target '3where' on list {input_strings} is at {selection_sort(input_strings)}")
    print(
        f"target 0.9 on list {input_floats} is at {selection_sort(input_floats, 0.9)}")

                
        