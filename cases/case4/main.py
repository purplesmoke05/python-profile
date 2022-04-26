def main():
    # variable initialized in try can be used in outer scope
    try:
        test_list = []
        hoge = 10/0
    except Exception:
        pass
    assert "test_list" in locals()

    # variable initialized in try can be used in else scope
    try:
        test_list = []
    except Exception:
        pass
    else:
        assert "test_list" in locals()

    # variable not initialized in try can not be used in outer scope
    try:
        test_value = 10/0
    except Exception:
        pass
    assert "test_value" not in locals()


if __name__ == "__main__":
    main()
