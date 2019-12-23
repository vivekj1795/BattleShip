
import re
import datetime as dt
from datetime import date
from datetime import time
from datetime import datetime

mydata = open('dates.txt', 'r')
txt = mydata.read()

the_main_list = []
firstformat = r"\d+/\d+/\d+"
secondformat = r"\d+-\d+-\d+"

def todate(format, thesplit):
    founddates = re.findall(format, txt)
    successfulConversion = 0
    for i in founddates:
        x = re.split(thesplit, i)
        year = int(x[2])
        day = int(x[1])
        month = int(x[0])

        if len(str(year)) == 2:
            year += 1900
        try:
            a = datetime(year, month, day)
            the_main_list.append(a)
            successfulConversion += 1
        except ValueError:
            print("Error at position: " + i)

    print("Total list size: {} \nTotal Sorted: {}\n".format(len(founddates), successfulConversion))



todate(firstformat, "/")
todate(secondformat, "-")
the_main_list.sort()
stripped1 = [datetime.strftime(thedate, "%m/%d/%Y") for thedate in the_main_list]
print(stripped1)
print("Total dates extracted: {}".format(len(stripped1)))


thirdformat = r"([a-zA-Z]+)  (\d+)  (\d+)"
third = re.findall(thirdformat,txt)
