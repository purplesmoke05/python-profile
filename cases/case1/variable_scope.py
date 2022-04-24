from typing import List


class Test1:
    """
    instance variable
    """
    hoge: str

    def __init__(self) -> None:
        # instance variable
        self.hoge = "".join([str(i) for i in range(100)])

hoge: str

class Test2:
    """
    global variable
    """
    def __init__(self) -> None:
        # global variable
        hoge = "".join([str(i) for i in range(100)])

