import random


class PasswordGenerator:
    def __init__(self, length, count, charset="zxcvbnmasdfghjklqwertyuiop1234567890"):
        self.length = length
        self.charset = charset
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count = self.count - 1
            password = ""
            for i in range(self.length):
                password += random.choice(self.charset)
            return password
        else:
            raise StopIteration


if __name__ == "__main__":
    generator = PasswordGenerator(10, 5)
    for password in generator:
        print(password)

    generator2 = PasswordGenerator(5, 2, "a1")
    print(next(generator2))
    print(next(generator2))

