class Test1:
    """
    Class with staticmethod
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def calc(a: int, b: int) -> int:
        ret: int = 1
        for i in range(a):
            ret *= i * b * ret
        return ret


class Test2:
    """
    Class with normal method
    """

    def __init__(self) -> None:
        pass

    def calc(self, a: int, b: int) -> int:
        ret: int = 1
        for i in range(a):
            ret *= i * b * ret
        return ret


class TestEx:
    """
    Class with classmethod
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def calc(cls, a: int, b: int) -> int:
        ret: int = 1
        for i in range(a):
            ret *= i * b * ret
        return ret
