# import numpy
# import numpy as np
#
# # Open the file in read mode and read its contents into a string
# with open('matrix.txt', 'r') as f:
#     contents = f.read()
#
# # Split the string into a list of lines
# lines = contents.split('\n')
# people = []
# # Iterate through the list of lines
# for i in lines[0].split('\t')[5].split('|'):
#     people.append(i.strip())
#
# dict = {}
#
# for i in range(len(people)):
#     dict[people[i]] = 0
#
# arr = numpy.zeros((len(people), len(people)))
#
# for i in range(1, len(lines)-1):
#     for j in lines[i].split('\t'):
#         k = 0
#         for l in j.split('|')[1]:
#             if l.isnumeric():
#                 arr[i-1][k] = int(l)
#                 print()
#                 k += 1
#
# maxValue = 0
# mostFamous = []
# for i in range(len(people)):
#     temp = list(dict.keys())[i]
#     for j in range(len(people)):
#         dict[temp] += arr[i][j]
#     if dict[temp] > maxValue:
#         maxValue = dict[temp]
#
# for i in range(len(list(dict.values()))):
#     if list(dict.values())[i] == maxValue:
#         mostFamous.append(list(dict.keys())[i])
#
# print(mostFamous)
# # print(sorted(dict.items(), key=lambda x: x[1]))

with open('matrix.txt', 'r') as f:
    matrix = f.readlines()
f.close()
count = 0
index = 0
all_persons = []
for i in range(1, len(matrix)):
    aux = 0
    for number in matrix[i]:
        if number == "1":
            aux += 1
    words = matrix[i].split()
    for word in range(0, len(words), 2):
        if words[word].isalpha():
            all_persons.append((aux, f"{words[word]} {words[word+1]}"))
    if aux > count:
        count = aux
        index = i
print("The person/s with the most friends are:")
for i in range(len(all_persons)):
    if all_persons[i][0] == count:
        print(all_persons[i][1])
print("")
print("Sort all the people by the number of friends")
all_persons.sort(reverse=True)
for i in range(len(all_persons)):
    print(f"{all_persons[i][1]} {all_persons[i][0]}")
