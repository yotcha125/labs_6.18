import itertools

# Группа рабочих
workers = list(range(1, 21))

# Размеры бригад
brigade_sizes = [3, 5, 12]

# Генерация всех возможных комбинаций
combinations = list(itertools.combinations(workers, sum(brigade_sizes)))

# Фильтрация комбинаций по размерам бригад
valid_combinations = []
for combo in combinations:
    brigade1 = combo[:brigade_sizes[0]]
    brigade2 = combo[brigade_sizes[0]:brigade_sizes[0]+brigade_sizes[1]]
    brigade3 = combo[brigade_sizes[0]+brigade_sizes[1]:]
    if sorted(brigade1) == list(range(1, brigade_sizes[0]+1)) and \
       sorted(brigade2) == list(range(brigade_sizes[0]+1, brigade_sizes[0]+brigade_sizes[1]+1)) and \
       sorted(brigade3) == list(range(brigade_sizes[0]+brigade_sizes[1]+1, sum(brigade_sizes)+1)):
        valid_combinations.append(combo)

# Вывод всех возможных вариантов
for i, combo in enumerate(valid_combinations):
    print(f"Вариант {i+1}: {combo}")