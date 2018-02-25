# put your code here.
from sys import argv

script, filename = argv

data = open(filename)

word_count = {}
punctuation = ['"', '.', ',', ';', ':', '?', '!']

for line in data:
    line = line.rstrip().split(" ")
    for word in line:
        word = word.lower()
        # print word
        if len(word) != 0:
            if word[-1] in punctuation:
                word = word[:-1]
            if word[0] in punctuation:
                word = word[1:]
            word_count[word] = word_count.get(word, 0) + 1

for key, value in word_count.iteritems():
    print "{} {}".format(key, value)


data.close()
