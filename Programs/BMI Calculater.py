import math 
hight = float(input("what is your  hight:")) # just normal asking for hight
weight = int(input("what is your weight:"))    # and  

bmi = weight / (hight**2) # callculate bmi
# print to user 
print(f"your bmi is {math.floor(bmi)}") 
