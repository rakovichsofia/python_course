numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_num = 0
for num in numbers:
    if num is not None:
        sum_num += num
filtered_list = []
for num in numbers:
    if num is None:
        filtered_list.append(sum_num / len(numbers))
    else:
        filtered_list.append(num)
print("Измененный список:", filtered_list)
