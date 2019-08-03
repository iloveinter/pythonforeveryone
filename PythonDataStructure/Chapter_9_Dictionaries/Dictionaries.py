purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

ccc = dict()
#print(ccc['csev'])
#
'csev' in ccc
#False

# count names
counts = dict()
names = ['csev','cwen','cesv','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


counts = dict()
names = ['csev','cwen','cesv','zqian','cwen']
#x = counts.get(name,0)
if name in counts:
    x = counts[name]
else:
    x = 0

counts = dict()
names = ['csev','cwen','cesv','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)
