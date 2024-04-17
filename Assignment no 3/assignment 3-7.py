#This Code was drafted by Shubham Mhaske
def filter_long_words(word_list, length):
    return [word for word in word_list if len(word) > length]

words = ['Car', 'bike ', 'cherry', 'date', 'elderberry']
length = 5
print(filter_long_words(words, length))
