
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


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
