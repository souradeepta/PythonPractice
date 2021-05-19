def prime_checker(input: int) -> bool:
    for i in range(2, input):
        if input % i == 0:
            return False
        return True


print(f'{prime_checker(28)}')
