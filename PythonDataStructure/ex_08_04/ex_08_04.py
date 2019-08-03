# open a file, split, sort and print
fname = input('Enter a File Name: ')
try:
    fh = open(fname)
except:
    print('Please Input a Valid File Name!')
    quit()

inp = fh.read()

words = inp.split()
words.sort()
count = range(len(words)-1)
wordlist = list()
wordlist.append(words[0])
for i in count:
    if words[i] == words[i+1]:
        continue
    wordlist.append(words[i+1])
print(wordlist)

#for word in words:
#    print(word)


#print(words)
