# Date Verificator
from datetime import date

while True:
    day= int(input("Insira o dia: "))
    if 1 <= day <= 31:
        break
    else:
        print(" It's a invalid day. Try again.")


while True:
    month= int(input("Insert the month: "))
    if 1<=month<=12:
        if month == 2 and day>29:
            print(" February doen't have more than 29 days. Try again.")
        elif month in [4,6,9] and day>30:
                    print(" This month doesn't have more than 30 days. Try again.")
        else:
            break

    print(" It's a invalid month. Try again.")    
    
 
while True:
    year= int(input('Insert the year'))# only years with 4 digits
    if 1000>year or year>date.today().year:
        print(" It's a invalid month. Try again.")
    else:    
        bissexto= (year%100!=0 and year%4==0)  or (year%100==0 and year%400==0)
        if  month==2 and day==29 and bissexto==False : 
            print(" This month hasn't more than 28 days. Try again.")
        else:
            break