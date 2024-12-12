"""Function examples."""


def func():
    """Print to console - I´m inside the function."""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """
    Print to console - My name is [name].

    :param name: name you want to use
    """
    print(f"My name is {name}")


def sum_six(num: int) -> int:
    """
    Add six to given number.

    :returns: result of 6 + num
    :param num: number to use
    """
    return 6 + num


# sum_numbers()


# usd_to_eur()

if __name__ == '__main__':
    func()
    my_name_is("Kristjan")
    my_name_is("Mari")
    print(sum_six(11))
