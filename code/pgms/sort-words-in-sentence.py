from typing import List


def sort_words(sentence: List) -> List:
    words_list = sentence.split()
    dup_removed_list = list(set(words_list))
    sorted_list = sorted(dup_removed_list)

    return " ".join(sorted_list)


sentence = "hello world and practice makes perfect and hello world again"
print(f'{sort_words(sentence)}')





