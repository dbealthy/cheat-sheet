n = 0


def fn():
    def wp():
        global n
        n += 1
        print(n)

    return wp


x = fn()
x()
x()
x()
x()
