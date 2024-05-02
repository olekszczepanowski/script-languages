def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def make_generator(f):
    i = 0
    while True:
        yield f(i)
        i = i + 1


numSequence = lambda x: 4*x+7

if __name__ == '__main__':
    testA = make_generator(fibonacci)
    testB = make_generator(numSequence)
    print("Test a:")
    for i in range(20):
        print(next(testA))

    print("Test b:")
    for i in range(20):
        print(next(testB))


