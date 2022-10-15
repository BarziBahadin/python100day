import math 
hight = float(input("what is your  hight:")) # just normal asking for hight
weight = float(input("what is your weight:"))    # and  

bmi = (weight / (hight**2) )# callculate bmi
# print to user 
# with some information
# ----------------------------------------------------------------

if (bmi<18) :
    print(f"Your bmi is {bmi} and under weights")
elif (bmi>18 and bmi<25):
    print(f"Your bmi is {bmi} and normal")
elif (bmi>25 and bmi<30):
    print(f"Your bmi is {bmi} and over weight")
elif (bmi>30 and bmi<35):
    print(f"Your bmi is {bmi} and obese")
else:
    print(f"Your bmi is {bmi} and clinically obese.")
