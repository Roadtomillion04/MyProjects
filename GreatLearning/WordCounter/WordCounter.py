# Letter Counter
with open('./Randomfile.txt', 'r') as file:
    letters = file.read().replace(' ', '')
    print(len(letters))

#Word Counter
with open('./Randomfile.txt', 'r') as file:
    tot_words = file.read().split()
    word_counter = 0
    for word in tot_words:
        word_counter += 1
    print(word_counter)
