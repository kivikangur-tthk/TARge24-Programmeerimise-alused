"""
Kirjuta programm, mis küsib kasutajalt ilma ja kuupäeva ning
olenevalt vastusest kirjutab erineva tegevuse ekraanile.

Kasutame liit tingimust ja vähemalt kolme erinevat tegevust.
"""
rainy = "vihmane"
date_before_christmas = "20.12.2024"
date_in_autumn = "10.10.2025"

weather = input("Milline ilm on?")
date = input("Mis on kuupäev?")

if weather == rainy and date == date_before_christmas:
    print("Pole eriti talvine ilm, aga jalutada võib ikka.")
elif weather == rainy and date == date_in_autumn:
    print("Ilus sügisilm, mine porilompi hüppama.")

if weather == rainy:
    if date == "20.12.2024":
        print("Pole eriti talvine ilm, aga jalutada võib ikka.")
    elif date == "10.10.2025":
        print("Ilus sügisilm, mine porilompi hüppama.")
