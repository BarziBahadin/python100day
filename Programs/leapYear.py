year = 2004
print ("Date: ")
if year % 4 == 0: 
    print ("Year: ")
    if year % 100 == 0 or year % 400 == 0:
        print (f"{year} is leap year")
    else:
     print(f"{year} is not a leap year")
else:
     print(f"{year} is not a leap year")
    