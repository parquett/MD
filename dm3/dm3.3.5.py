import nltk
with open('interests.txt', 'r') as f:
    matrix = f.read()
f.close()
words = matrix.split()
title = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats"
title = nltk.word_tokenize(''.join(title))
print("The spectre of interests is : Books ", end="")
for word in title:
    if word in words:
        print(word, end=", ")