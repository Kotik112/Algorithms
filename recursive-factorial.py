
def calculate_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


if __name__ == '__main__':
    print(recur_factorial(5))
    print(calculate_factorial(5))
