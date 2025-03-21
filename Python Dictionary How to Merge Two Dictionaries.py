# Python Dictionary: How to Merge Two Dictionaries

# Solution 1:Using | operator
#dict1={"John":89,"Lisa":67}
#dict2={"Lisa":80,"Morkel":77}
#print(dict1 | dict2)

# Solution 2:Using ** operator
#dict1={"John":89,"Lisa":67}
#dict2={"Lisa":80,"Morkel":77}
#print({**dict1,**dict2})

# Solution 3:Using copy() and update() methods
dict1={"John":89,"Lisa":67}
dict2={"Lisa":80,"Morkel":77}
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)
