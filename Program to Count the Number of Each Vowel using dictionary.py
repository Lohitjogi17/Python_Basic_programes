# Program to Count the Number of Each Vowel
# method1: Using Dictionary
a="The Lion Kingdom and the wolf family"
vowels="aeiou"
a=a.casefold()
print(a)
count={}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char]+=1
print(count)
