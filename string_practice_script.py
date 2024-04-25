# practice with string and string methods

# Quotes make strings
# Use escape (backslash) to make a quote "plain text"
"This is a string"

'This is also a string'

"This isn't a bad idea."

# 'This is a bad idea, isn't it?'

'She told me, "go there"'
# "She told me, "go there"" # this is bad

report = "She told me, \"don't go there\"."
print(report)

print("Here's\na string\nwith some\nline returns\n\n")
print("\u2660")

######################
# find and index

"Here's a short sentence.".count("s")
example_sentence = "Here's a short sentence."
example_sentence.count("s")
example_sentence.find("s")
print(example_sentence[5])
example_sentence.find("s", 6) # looking for the next s

example_sentence.find("z")
example_sentence.index("s", 6) # works the same when it's there
example_sentence.index("z")

# grab surrounding text
search_word = "spam"

with open("spam_song.txt") as fc:
    spam_song = fc.read()

type(spam_song)
len(spam_song)

spam_song.find(search_word)
print(spam_song[400:404])
print(spam_song[380:424])

position = 0
spam_positions = []
while position < len(spam_song):
    found_spam = spam_song.find(search_word, position)
    if found_spam == -1:
        break
    print(spam_song[(found_spam-10):(found_spam+14)])
    spam_positions.append(found_spam)
    position = found_spam + 1
print(spam_positions)

len(spam_positions)
spam_song.count("spam")

###############################
# starting 4/25 lecture with endswith and startswith

import os
files_here = os.listdir()
print(files_here)
type(files_here)
type(files_here[0])

"file.txt".endswith(".txt")
"README.md".endswith(".txt")

for file in files_here:
    print(f"let's check to see if {file} is a TXT file")
    if file.endswith(".txt"):
        print(f"Here's the first 100 bytes of the file {file}")
        with open(file) as file_connection:
            print(file_connection.read(100))

waitress_lines = []
with open("spam_song.txt", "r") as file_connection:
    for line in file_connection:
        if line.startswith("Waitress"):
            waitress_lines.append(line)

print(waitress_lines)

print("\n".join(waitress_lines))

example_csv_line = ["name", "email", "gpa", "year"]
print(example_csv_line[0] + "," +
      example_csv_line[1] + "," +
      example_csv_line[2] + "," +
      example_csv_line[3])

print(",".join(example_csv_line))
# print(",".join([1, 2, 3, 4])) # this fails because .join() only joins strings
print(",".join([str(1), str(2), str(3), str(4)]))

