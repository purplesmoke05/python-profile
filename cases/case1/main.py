from memory_profiler import profile
from variable_scope import *

@profile
def test1(num: int):
    # instance variable
    test1_instances: List[Test1] = []
    for _ in range(num):
         test1_instances.append(Test1())

@profile
def test2(num: int):
    # global variable
    test2_instance: List[Test2] = []
    for _ in range(num):
        test2_instance.append(Test2())

def main():
    NUM = 10*1000*10
    test1(NUM)
    test2(NUM)

if __name__ == "__main__":
    main()