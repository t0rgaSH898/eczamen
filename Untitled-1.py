input_str = input("Введите числа через пробел: ")
numbers = list(map(int, input_str.split()))
n = len(numbers)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
print("Отсортированный массив: ", numbers)
#arr = list(map(float, input ("Числа: "). split()))
#n = len(arr)
#for i in range(n-1):
#   for j in range(n-i-1):
#       if arr[j] > arr[j+1]:
#           arr[j], arr[j+1] = arr[j+1], arr[j]
#print("Отсортировано: ", arr)