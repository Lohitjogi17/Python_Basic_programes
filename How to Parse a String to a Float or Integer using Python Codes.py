# How to Parse a String to a Float or Integer using Python Codes
#Solution1:Parse string into integer

string="12345"
print(type(string))
int_str=int(string)
print(type(int_str))

#Solution2:Parse string into float

string="123.45"
print(type(string))
float_str=float(string)
print(type(float_str))

#Solution3: Parse String float Numeral into Integer

string="123.45"
print(type(string))
str_float_int=int(float(string))
print(type(str_float_int))
