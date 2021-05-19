"""Question:
    given an aray of integers. Compute the pythagorean triplets.
    output of n array would be n-2
    For index i, a triplet exists if any of the rules satisfy:
    a[i]**2 + a[i+1]**2 = a[i+2]**2
    a[i]**2 + a[i+2]**2 = a[i+1]**2
    a[i+1]**2 + a[i+2]**2 = a[i]**2
    @input =  [0, 5, 5, 0, 5, 12, 13]
    @output = [1, 1, 1, 0, 1]
    """

from typing import List


def pythagoreanTriplets(input: List[int]) -> List[int]:
    ans = []
    if not input:
        return ans
    for i in range(len(input)-2):
        ans.append(TripletCheck(i))
        # print(ans)
    return ans


def TripletCheck(index: int) -> int:
    if input[index]**2 + input[index+1]**2 == input[index+2]**2 or \
            input[index+1]**2 + input[index+2]**2 == input[index]**2 or \
            input[index]**2 + input[index+2]**2 == input[index+1]**2:
        return 1
    else:
        return 0


input = [0, 5, 5, 0, 5, 12, 13]
output = [1, 1, 1, 0, 1]

assert output == pythagoreanTriplets(input), "output is incorrect"
