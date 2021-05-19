def reverse_num(input):
    result = 0

    while input > 0:
        remainder = input % 10
        result = result*10 + remainder

        input = input//10

    return result


def main():
    print(reverse_num(234))
#    ans = reverse_num(234)
#    print(ans)


if __name__ == "__main__":
    main()
