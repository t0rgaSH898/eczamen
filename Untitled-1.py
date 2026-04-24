input_str = input("Введите числа через пробел: ")
numbers = []
try:
    temp_numbers = list(map(int, input_str.split()))
    if len(temp_numbers) == 0:
        print("Ошибка: Вы не ввели ни одного числа!")
        exit()
    numbers = temp_numbers
except ValueError:
    print("Ошибка: Введите только целые числа через пробел!")
    exit()
n = len(numbers)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
print("Отсортированный массив: ", numbers)
