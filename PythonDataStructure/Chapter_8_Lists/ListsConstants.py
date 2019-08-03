print([1, 24, 76])

print(['red', 'yellow', 'blue'])

print([1, [5,6], 7])

print([])

friends = ['Joseph', 'Glenn', 'Sally']

print(range(4))
x = range(4)
print(x[1])
#[0, 1, 2, 3]

print(range(len(friends)))
# [0, 1, 2]
for i in range(len(friends)):
    friend = friends[i]
    print(friend)
# Manipulating Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# list Can be sliced using:
t = [9,41,12,3,74, 15]
print(x[1:3])

# Building a List from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)


#Is something in a Lists
some = [1, 9, 21, 10, 16]
9 in some
#True
20 not in some
#True

#List are in Order
print(friends)
friends.sort()
print(friends)

# sum(), min(), max()..
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    print(value, sum(numlist), max(numlist),sum(numlist)/len(numlist))
