#Program to Count the Number of Each Vowel using list and dictionary comprehnesion
a="The Lion Kingdom and the Animals in the park of jurasic"
vowels="a,e,i,o,u"
a=a.casefold()
count={key:sum([1 for char in a if char==key])for key in vowels}
print(count)
