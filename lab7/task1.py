def liczba(listOfNumbers):
    output = filter(lambda c: (c % 2 == 0), listOfNumbers)
    return len(list(output))


def median(listOfNumbers):
    sortedNums = sorted(listOfNumbers)
    lenSortedNums = len(sortedNums)
    middleIndex = lenSortedNums // 2
    return (sortedNums[middleIndex] + sortedNums[-middleIndex - 1]) / 2


def newtonSqrt(x, epsilon=1e-10):
    def sqrtHelper(x, y, epsilon):
        nextY = (y + x / y) / 2
        return y if abs(nextY - y) < epsilon else sqrtHelper(x, nextY, epsilon)

    return sqrtHelper(x, 1.0, epsilon)


def make_alpha_dict(text):
    words = text.split()
    alpha_chars = {char: [word for word in words if char in word] for char in text if char.isalpha()}
    return alpha_chars


def flatten(lst):
    return [elem for tmpList in lst for elem in (flatten(tmpList) if isinstance(tmpList, list) else [tmpList])]


if __name__ == "__main__":
    # test zad1
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 3, 5, 7, 9 ,11]
    print("Test funkcji z podpunktu 1:")
    test1_1 = liczba(lista1)
    print(test1_1)
    test1_2 = liczba(lista2)
    print(test1_2)
    # test zad2
    print("Test funkcji z podpunktu 2:")
    test2_1 = median(lista1)
    print(test2_1)
    test2_2 = median(lista2)
    print(test2_2)
    # test zad3
    print("Test funkcji z podpunktu 3:")
    print(newtonSqrt(36,-9))
    print(newtonSqrt(0.5))
    print(newtonSqrt(9))
    # test zad4
    print("Test funkcji z podpunktu 4:")
    print(make_alpha_dict("on i ona"))
    # test zad5
    print("Test funkcji z podpunktu 5:")
    print(flatten([1, [2, 3], [[4, 5], 6]]))
    print(flatten([[[]],[]]))
    print(flatten([1,2,3,4]))
