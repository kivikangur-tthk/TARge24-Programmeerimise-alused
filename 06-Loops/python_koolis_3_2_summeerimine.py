"""
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.

Täienda seda programmi nii, et kasutajalt küsitakse arve seni,
 kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
  Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""


def sum_ten_for():
    pass


def sum_ten_while():
    counter = 0
    total = 0
    while counter < 10:
        counter += 1
        user_number = int(input(f"Sisesta {counter}. täisarv: "))
        total += user_number
    print(f"Sisestatud arvude summa on {total}")


def sum_unlimited():
    counter = 0
    total = 0
    while True:
        counter += 1
        user_input = input(f"Sisesta {counter}. täisarv: ")
        if user_input == "":
            break
        user_number = int(user_input)
        total += user_number
    print(f"Sisestatud {counter - 1} arvu summa on {total}")


if __name__ == '__main__':
    sum_unlimited()
