from typing import List
from memory_profiler import profile
from static_method import *


@profile
def test1(num: int):
    # instance with staticmethod
    test1_instances: List[Test1] = []
    for _ in range(num):
        test1_instance = Test1()
        test1_instances.append(test1_instance)


@profile
def test2(num: int):
    # instance with normal method
    test2_instances: List[Test2] = []
    for _ in range(num):
        test2_instance = Test2()
        test2_instances.append(test2_instance)


@profile
def testex(num: int):
    # instance with normal method
    testex_instances: List[TestEx] = []
    for _ in range(num):
        testex_instance = TestEx()
        testex_instances.append(testex_instance)


def main():
    NUM = 10 * 1000 * 100
    test1(NUM)
    test2(NUM)
    testex(NUM)


if __name__ == "__main__":
    main()
