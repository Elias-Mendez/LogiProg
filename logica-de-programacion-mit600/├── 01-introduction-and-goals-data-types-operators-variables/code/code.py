def demo_primitives() -> None:
    """"
    demonstrates the use of primitive data types and operators in Python.
    """
    a: int = 5
    b: float = 3.14
    c: str = "52"
    print(a + int(c))  # Output: 57
    print(c * 3)    # Output: '525252'
    print(b ** 2, 7 // 3, 7 % 3)    # Output: 9.8596 2 1

if __name__ == "__main__":
    demo_primitives()