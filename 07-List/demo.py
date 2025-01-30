def decrement_all(numbers: list):
    result = numbers[::]
    for i in range(len(result)):
        result[i] -= 1
    return result


numbers = [1, 2, 3]
print(f"{numbers=}")
decremented_numbers = decrement_all(numbers)
print(f"{numbers=}")
print(f"{decremented_numbers=}")

numbers = [1, 2, 3, 4]
numbers[1:3] = [10, 11]
print(numbers)  # [1, 10, 11, 4]

numbers[1:3] = [0]
print(numbers)  # [1, 0, 4]

numbers.append(5)
numbers += [6]
print(f"{numbers=}")

matrix = [[1], [2, 3], [4, 5, 6]]
print(f"{matrix=}")
if [4] in matrix:
    matrix.remove([4])
matrix = []
if len(matrix) > 0:
    removed = matrix.pop(-1)
    print(f"{removed=}")
print(f"{matrix=}")

print(min(["42", "122", "99", "61"]))  # -> 214

names = ["AGO", "mati", "reinuvader", "kasparr", "guido"]


def reverse_lower(name):
    return name[::-1].lower()


print(min(names, key=reverse_lower))
