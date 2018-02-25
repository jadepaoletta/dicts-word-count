from sys import argv
from collections import Counter
import re

script, filename = argv

data = open(filename)
file_text = data.read()

word_count = Counter()
file_list = re.split(" |\n", file_text)

for word in file_list:
    word_count[word] = word_count.get(word, 0) + 1

for key, value in word_count.iteritems():
    print "{} {}".format(key, value)


data.close()
