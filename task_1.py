from operator import index

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = numbers.index(None)
numbers[index] = 0
numbers[index] = sum(numbers)/len(numbers)
print("Измененный список:", numbers)
