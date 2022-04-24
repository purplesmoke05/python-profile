from injector import inject


class Inner:
    const_value: int

    @inject
    def __init__(self, value: int) -> None:
        self.const_value = value


class Test1:
    """
    Outer Class using DI
    """

    inner: Inner

    @inject
    def __init__(self, inner: Inner) -> None:
        self.inner = inner


class Test2:
    """
    Outer Class not using DI
    """

    inner: Inner

    def __init__(self, inner: Inner) -> None:
        self.inner = inner
