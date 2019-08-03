# read from a file and find all the special lines.
fname = input("Please Enter a File Name: ")
try:
    fhand = open(fname)
except:
    print("Please Input a Valid File Name!")
    quit()

count = 0
totalvalue = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    count = count + 1
    atpos = line.find(':')
    totalvalue = totalvalue + float(line[atpos+1:])

print("Average spam confidence:", totalvalue/count)
