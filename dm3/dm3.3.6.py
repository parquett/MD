import nltk
from collections import defaultdict

print("DM task 3.6")


book_title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"

interests = nltk.word_tokenize(book_title)
interests.append('Books')

people_interests = []
with open("people_interests.txt", 'r', encoding='utf-8') as f:
    contents = f.read()
    rows = contents.split('\n')
    for row in rows:
        elements = row.split(' : ')
        elements = [element.strip() for element in elements[1].split(" ")]
        people_interests.append(elements)

adjacency_matrix = []

influence = []

with open('influence.txt', 'r') as f:
    contents = f.read()
    rows = contents.split('\n')
    for row in rows:
        elements = row.split(' : ')
        influence.append(float(elements[1]))


# print(influence)

with open('matrix.txt', 'r') as f:
    contents = f.read()
    rows = contents.split('\n')
    for row in rows:
        elements = row.split('|')
        elements = [element.strip() for element in elements]
        adjacency_matrix.append(elements)

names = adjacency_matrix[0].copy()
adjacency_matrix = adjacency_matrix[1:]

for i in range(len(adjacency_matrix) - 1):
    a = adjacency_matrix[i][1].split(" ")
    adjacency_matrix[i] = [int(x) for x in a if x != '']
adjacency_matrix.pop()


ratings = []

for initial_vertex in range(len(adjacency_matrix)):
    levels = [100 for i in range(len(adjacency_matrix))]
    levels[initial_vertex] = 0
    spt_set = set()
    all_vertices = set([i for i in range(len(adjacency_matrix))])

    for step in range(len(adjacency_matrix)):
        # looking for the vertex with the lowest level that is still not in spt_set
        current_vertex = levels.index(max(levels))
        for i in all_vertices:
            if i not in spt_set and levels[i] < levels[current_vertex]:
                current_vertex = i

        # add current_vertex to spt_set
        spt_set.add(current_vertex)

        # update adjacent elements
        for next_vertex in all_vertices:
            if adjacency_matrix[current_vertex][next_vertex] == 1:
                levels[next_vertex] = min(levels[next_vertex], levels[current_vertex] + 1)

    r = 0
    for level in levels:
        if level != 0:
            r += level

    coinciding_interests = 0

    for interest in people_interests[initial_vertex]:
        if interest in interests:
            coinciding_interests += 1

    ratings.append(r * influence[initial_vertex] * 0.5 * 0.2 * coinciding_interests)




a = defaultdict(float)

for i in range(len(adjacency_matrix)):
    a[i] = ratings[i]

sorted_a = sorted(a.items(), key=lambda x: x[1], reverse=True)

cnt = 0
for i in sorted_a:
    cnt += 1
    if cnt > 5:
        break
    print(f"{names[i[0]]:20}  {i[1]:.2f}")