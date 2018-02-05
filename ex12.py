from sys import argv

script, filename = argv

print "we're going to erase %r" %filename
print "if you don't want that, hit STRG-C."
print "if you want to do that, hit ENTER."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file, goodbye!"
target.truncate()

print "now i'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3+ "\n")

print "closing in..."
target.close()