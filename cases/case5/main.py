import logging


def main():
    test_logger = logging.getLogger("test1")

    test_handler1 = logging.StreamHandler()
    test_handler2 = logging.NullHandler()
    test_handler3 = logging.NullHandler()

    test_logger.addHandler(test_handler1)
    test_logger.addHandler(test_handler2)
    test_logger.addHandler(test_handler3)

    test_logger.removeHandler(test_handler2)

    assert test_logger.handlers[0] == test_handler1
    assert test_logger.handlers[1] == test_handler3


if __name__ == "__main__":
    main()
