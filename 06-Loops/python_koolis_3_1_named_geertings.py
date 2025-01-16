"""
Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda
 ja lisab ka tervituse järjekorranumbri.
"""


def solution():
    name = input("Palun sisesta oma nimi: ")
    for i in range(5):
        print(f"Ole tervitatud, {name}, {i + 1}. korda.")


if __name__ == '__main__':
    solution()
