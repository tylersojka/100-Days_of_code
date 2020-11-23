# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
ordered_list = []
#student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for num in student_scores:
    if ordered_list == []:
        ordered_list.append(num)
    elif num > ordered_list[-1]:
        ordered_list.append(num)
    elif num < ordered_list[0]:
        ordered_list.insert(0,num)


print(f' the highest score is {ordered_list[-1]}\n the lowest score is {ordered_list[0]}')

# ordered_list = []
# student_score = [78, 65, 89, 86, 55, 91, 64, 89]
# for num in student_score:
#     if ordered_list == []:
#         ordered_list.append(num)
#     elif num > ordered_list[-1]:
#         ordered_list.append(num)
#     elif num < ordered_list[0]:
#         ordered_list.insert(0,num)

# 55 66 74 23 54 88 98 100 12 32 1 98