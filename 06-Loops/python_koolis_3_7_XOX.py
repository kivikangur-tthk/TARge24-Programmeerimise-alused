"""
Koosta programm, mis küsib kasutajalt arvu N ja
 väljastab O-tähtedest koosneva ruudu suuruses NxN.
  Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d,
X 0 X
0 X 0
X 0 X
"""


def print_square(size):
    """
    Print a square with "O" times size.
    :param size:
    :return:
    """
    for row in range(size):
        for col in range(size):
            symbol = "O"
            if row == col or row + col + 1 == size:
                symbol = "X"
            print(f"{symbol}", end=" ")
        print()


if __name__ == '__main__':
    numbers = "123"
    numbers = numbers.replace("1", "5")
    size = int(input("Kui suurt ruutu soovid? "))
    print_square(size)
