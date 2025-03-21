# How to Check if a String is a Valid Keyword or Not
import keyword

words=["break","john","three","continue","lambda","global","peter","for","while","string","number"]

for i in range(len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is a keyword in python")
    else:
        print(words[i],"is not a keyword in python")

# to get keyword list
print(keyword.kwlist)
