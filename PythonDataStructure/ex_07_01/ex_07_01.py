# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case
fname = input('Enter a File Name: ')
try:
    fhand = open(fname)
except:
    print('Please Input a Valid File Name!')
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())

#print(fname)
