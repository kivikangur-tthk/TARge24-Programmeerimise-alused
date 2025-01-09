"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja
 väljastab tulemuse Fahrenheiti kraadides.
 Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi.
"""


def convert(temperature, unit, to_unit):
    from_unit = unit.lower()[0]
    if from_unit == to_unit:
        return temperature, unit
    if from_unit == "c":
        if to_unit == "f":
            result = temperature * 1.8 + 32
            return result, "fahrenheit"
        elif to_unit == "k":
            result = temperature - 273.15
            return result, "kelvin"
    elif from_unit == "f":
        result_c = (temperature - 32) / 1.8
        if to_unit == "c":
            return result_c, "celsius"
        elif to_unit == "k":
            result = result_c - 273.15
            return result, "kelvin"
    return "võimatu", "teisendada"


if __name__ == '__main__':
    temperature = float(input("Mis on temperatuur? "))
    unit = input("Mis ühikutes (celsius/fahrenheit/kelvin)? ")
    to_unit = input("Mis ühikus soovid vastust (c/f/k)? ")
    result_temperature, result_unit = convert(temperature, unit, to_unit)
    print(f"{temperature} {unit} on {result_temperature} {result_unit}")
