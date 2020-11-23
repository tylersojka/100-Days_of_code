even_sum = 0
even_list =[]
for num in range(0, 101, 2):
    even_sum += num
    even_list.append(num)

print(even_sum)
print(even_list)