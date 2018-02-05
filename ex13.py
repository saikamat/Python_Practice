## more files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s." %(from_file, to_file)

# we could do these two on line too, how?

input = open(from_file)
indata = input.read()

print "the input file is %d bytes big." %len(indata)

print "does the output file exist? %r " %exists(to_file)

print "ready, hit ENTER to continue, STRG-C to abort."

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "all right, we're all done."

output.close()
input.close()