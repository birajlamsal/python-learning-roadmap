import re

# have zero understanding in this
txt = "The rain in Spain"

# Search for a match from the start to the end of the string
x = re.search("^The.*Spain$", txt)
if x:
    print(x)
else:
    print("No match found for '^The.*Spain$'")

# Find all occurrences of "ai"
x = re.findall("ai", txt)
print(x)

# Find occurrences of "Portugal" (which doesn't exist in the string)
x = re.findall("Portugal", txt)
print(x)

# Search for the first whitespace character
x = re.search("\s", txt)
if x:
    print("The first white-space character is located in position:", x.start())
else:
    print("No whitespace found in the string.")

# Attempt to search for "Portugal" (which doesn't exist in the string)
x = re.search("Portugal", txt)
if x:
    print(x)
else:
    print("No match found for 'Portugal'")

# Split the string by whitespace
x = re.split("\s", txt)
print(x)

# Split the string by whitespace, but limit the split to once
x = re.split("\s", txt, 1)
print(x)