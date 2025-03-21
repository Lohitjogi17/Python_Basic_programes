# How to Convert String to DateTime using Python Codes

#Solution1: Using Datetime module

from datetime import datetime

#date="Oct 14 1997 7:15AM"
#print(type(date))
#date_time=datetime.strptime(date,"%b %d %Y %I:%M%p")
#print(date_time)
#print(type(date_time))

#Solution2:Using dateutil module

from dateutil import parser

date_time=parser.parse("Oct 14 1997 7:15AM")

print(date_time)
print(type(date_time))
