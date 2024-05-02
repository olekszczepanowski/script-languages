def forall(pred, iterable):
    retValue = True
    for item in iterable:
        if not pred(item):
            retValue = False
    return retValue


def exists(pred, iterable):
    retValue = False
    for item in iterable:
        if pred(item):
            retValue = True
    return retValue


def atleast(n, pred, iterable):
    count = 0
    for item in iterable:
        if pred(item):
            count += 1
    return count >= n


def atmost(n, pred, iterable):
    count = 0
    for item in iterable:
        if pred(item):
            count += 1
    return count <= n


if __name__ == '__main__':
    unaryFunc = lambda x: x > 5
    testList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    testList2 = [6,7,8,9]
    testList3 = [1,2,3,4,5]
    testList4 = []
    print("Testy dla listy 1:")
    print(exists(unaryFunc, testList1))
    print(forall(unaryFunc, testList1))
    print(atmost(2, unaryFunc, testList1))
    print(atleast(2, unaryFunc, testList1))
    print("Testy dla listy 2:")
    print(exists(unaryFunc, testList2))
    print(forall(unaryFunc, testList2))
    print(atmost(2, unaryFunc, testList2))
    print(atleast(2, unaryFunc, testList2))
    print("Testy dla listy 3:")
    print(exists(unaryFunc, testList3))
    print(forall(unaryFunc, testList3))
    print(atmost(2, unaryFunc, testList3))
    print(atleast(2, unaryFunc, testList3))
    print("Testy dla listy 4:")
    print(exists(unaryFunc, testList4))
    print(forall(unaryFunc, testList4))
    print(atmost(2, unaryFunc, testList4))
    print(atleast(2, unaryFunc, testList4))


