#Что должно быть подсчитано:
#    Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#    Все строки (не важно, являются они ключами или значениям или ещё чем-то)
def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, int):
        sum += data_structure  #суммируем все числа int
    if isinstance(data_structure, str):
        sum += len(data_structure)  #суммируем количество длин всех строк str
    if isinstance(data_structure, list):
        for i in data_structure:
            sum += calculate_structure_sum(i)  #суммируем количество длин всех строк list
    if isinstance(data_structure, tuple):
        for i in data_structure:
            sum += calculate_structure_sum(i)  # суммируем количество длин всех строк tuple
    if isinstance(data_structure, set):
        for i in data_structure:
            sum += calculate_structure_sum(i)  # суммируем количество длин всех строк set
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)  # суммируем количество длин всех строк ключей
            sum += calculate_structure_sum(value)  # суммируем количество длин всех строк значений
    # Возвращаем сумму
    return sum


# Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Вывод результата
result = calculate_structure_sum(data_structure)
print(result)