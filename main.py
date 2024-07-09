
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    userinput = input()
    return list(map(int, userinput.split()))


def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(len(numbers) // 2):
        storage = numbers[i]
        numbers[i] = numbers[-i-1]
        numbers[-i-1] = storage
    return numbers

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
