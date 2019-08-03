# Best Friends: Stings and Lists

abc = 'With three words'
stuff = abc.split()
for w in stuff:
    print(w)

line = 'From stephen.marquar@uct.ac.za Sat Jan 5 9:14:16 2008'
words = line.split()
print(words)

# the double split pattern
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])
