import itertools

# Группа рабочих
workers = list(range(1, 21))

# Размеры бригад
brigade_sizes = [3, 5, 12]

max_characteristic_sum = 100

# Характеристики каждого рабочего
characteristics = [5, 3, 7, 2, 4, 6, 1, 8, 9, 10, 3, 2, 6, 5, 4, 7, 2, 3, 1, 9]

# Генерация всех возможных комбинаций
combinations = list(itertools.combinations(workers, sum(brigade_sizes)))

# Фильтрация комбинаций по размерам бригад и сумме характеристик
valid_combinations = []
min_total_characteristics = float('inf')  # Начальное значение для минимальной суммы характеристик

for combo in combinations:
    brigade1 = combo[:brigade_sizes[0]]
    brigade2 = combo[brigade_sizes[0]:brigade_sizes[0] + brigade_sizes[1]]
    brigade3 = combo[brigade_sizes[0] + brigade_sizes[1]:]
    
    # Проверка ограничения на сумму характеристик каждой бригады
    if sum(characteristics[i-1] for i in brigade1) <= max_characteristic_sum and \
       sum(characteristics[i-1] for i in brigade2) <= max_characteristic_sum and \
       sum(characteristics[i-1] for i in brigade3) <= max_characteristic_sum:
        
        # Расчет суммы характеристик для текущей комбинации
        total_characteristics = sum(characteristics[i-1] for i in combo)
        
        # Проверка на минимальность суммы характеристик
        if total_characteristics < min_total_characteristics:
            min_total_characteristics = total_characteristics
            valid_combinations = [combo]
        elif total_characteristics == min_total_characteristics:
            valid_combinations.append(combo)

# Вывод всех возможных вариантов с минимальной суммой характеристик
for i, combo in enumerate(valid_combinations):
    print(f"Вариант {i+1}: {combo}")