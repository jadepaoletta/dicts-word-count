# put your code here.
data = open("twain.txt")

word_count = {}

for line in data:
    line = line.rstrip().split(" ")
    for word in line:
        word_count[word] = word_count.get(word, 0) + 1

for key, value in word_count.items():
    print "{} {}".format(key, value)



data.close()