#wap to check the given year is leap or not
'''we have 1.non-centurian
           2.centurian'''

year=int(input())
if (year%100!=0 and year%4==0)or(year%100==0 and year%400==0):
    print("year is a leap year")
else:
    print("NOt leap year")
