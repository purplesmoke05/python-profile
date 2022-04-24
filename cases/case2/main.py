from memory_profiler import profile
from loader import *
import os


def test():
    test1 = Test1()
    test1.load()

    assert test1.sample_value1 == os.environ.get("SAMPLE_VALUE1", default="")

    test2 = Test2()
    test2.set("hogehoge")

    assert test1.sample_value1 == os.environ.get("SAMPLE_VALUE1", default="")

    test1.load()

    assert test1.sample_value1 == "hogehoge"


def main():
    test()


if __name__ == "__main__":
    main()
