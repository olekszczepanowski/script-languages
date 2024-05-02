def forall(pred, iterable):
    return all(pred(x) for x in iterable)


def exists(pred, iterable):
    return any(pred(x) for x in iterable)


def atleast(n, pred, iterable):
    return sum(1 for x in iterable if pred(x)) >= n


def atmost(n, pred, iterable):
    return sum(1 for x in iterable if pred())


