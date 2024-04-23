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

