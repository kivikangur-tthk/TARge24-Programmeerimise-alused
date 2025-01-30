"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras,
lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
kus linnade arv leitakse vastava funktsiooni abil.
"""


def print_list(capitols, numbered=False):
    for number, name in enumerate(capitols):
        if numbered:
            print(f"{number + 1}. {name}")
        else:
            print(f"{name}")


if __name__ == '__main__':
    capitols = ["Tallinn", "Riia", "Helsinki", "Stockholm", "Vilnius",
                "Varssav", "Brüssel", "Pariis", "Lissabon", "Berlin"]
    print_list(capitols)
    for i in range(2):
        new_capitol = input(f"Sisesta {i + 1}. lisa pealinn: ")
        capitols.append(new_capitol)
    capitols.sort()
    print_list(capitols, numbered=True)
    print(f"Meie järjendis on {len(capitols)} Euroopa pealinna")
