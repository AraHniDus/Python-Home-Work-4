lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")

def get_unique_numbers(lst):
    new_lst = []
    unique_numbers = set(lst)

    for lst in unique_numbers:
        new_lst.append(lst)

    return new_lst

print(f"Отредактированный список:{get_unique_numbers(lst)}")