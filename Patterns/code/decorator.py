def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        nonlocal _cache
        key = str(args) + str(kwargs)
        if key not in _cache:
            result = func(*args, **kwargs)
            _cache[key] = result

        return _cache[key]

    return wrapper


@cache
def calculate_fibanachi(n: int):

    if n == 1:
        return 0
    if n == 2:
        return 1

    return calculate_fibanachi(n - 1) + calculate_fibanachi(n - 2)


if __name__ == "__main__":
    print(calculate_fibanachi(100))
