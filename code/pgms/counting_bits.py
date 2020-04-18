#count the number of bits

def count_bits(input: int ) -> int:
    count_bits = 0
    while input:
        count_bits += input & 1
        input >>= 1
    
    return count_bits

def  passed_tests():
    assert count_bits(4) == 1, "Should be 1"
    assert count_bits(3) == 2, "Should be 2"

def failed_tests():
    assert count_bits(33) == 5, "Should be not be 5"

if __name__ == "__main__":
    passed_tests()
    print("Postive Test cases passed")
    failed_tests()
    