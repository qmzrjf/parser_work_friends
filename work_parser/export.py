def test(x: int) -> int | None:
    if x % 2 == 0:
        return x
    return None


t = test(123)
