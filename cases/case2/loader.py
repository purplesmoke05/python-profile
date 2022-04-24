from typing import List
import config


class Test1:
    """ """

    sample_value1: str

    def __init__(self) -> None:
        pass

    def load(self) -> None:
        self.sample_value1 = config.SAMPLE_VALUE1


class Test2:
    """ """

    def __init__(self) -> None:
        pass

    def set(self, value: str) -> None:
        config.SAMPLE_VALUE1 = value
