from typing import List
from inject import *
from memory_profiler import profile
from injector import Injector, InstanceProvider


def configure(binder):
    binder.bind(Inner, to=InstanceProvider(Inner(10 * 1000)))


@profile
def test1(num: int):
    injector = Injector(configure)
    test1_instances: List[Test1] = []
    for _ in range(num):
        outer = injector.get(Test1)
        test1_instances.append(outer)


@profile
def test2(num: int):
    test2_instance: List[Test2] = []
    for _ in range(num):
        inner = Inner(10 * 1000)
        test2_instance.append(Test2(inner))


def main():
    NUM = 10 * 1000 * 10
    test1(NUM)
    test2(NUM)


if __name__ == "__main__":
    main()
