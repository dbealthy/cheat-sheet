class AlreadyInitailizedError(Exception): ...


def singltonize1(cls_):
    obj = None

    def safe_new(method):
        def wrapper(cls, *args, **kwargs):
            nonlocal obj
            if obj:
                raise AlreadyInitailizedError
            obj = method(cls)
            return obj

        return wrapper

    setattr(cls_, "__new__", safe_new(getattr(cls_, "__new__")))

    return cls_


def singltonize2(cls_):
    obj = None

    class _SingleTone(cls_):
        def __new__(cls, *args, **kwargs):
            nonlocal obj
            if obj:
                raise AlreadyInitailizedError
            obj = super().__new__(cls)

            return obj

    return _SingleTone


@singltonize
class SingleTone:
    def __init__(self, id: int):
        self.id = id


# o = SingleTone(1)
o = SingleTone(5)
o = SingleTone(1)
print(o.id)
