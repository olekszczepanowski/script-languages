from functools import lru_cache

from task4 import make_generator, fibonacci, numSequence



def make_generator_mem(f):
    @lru_cache(maxsize=None)
    def memoized_f(i):
        return f(i)

    @lru_cache(maxsize=None)
    def make_generator_memo():
        return make_generator(memoized_f)

    return make_generator_memo

if __name__ == '__main__':
    testA = make_generator(fibonacci)
    testB = make_generator(numSequence)
    print("Test a:")
    for i in range(20):
        print(next(testA))

    print("Test b:")
    for i in range(20):
        print(next(testB))
