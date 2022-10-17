hight = int(input("what is your hight in (Cm):"))


if hight > 120:
    age = int(input("what is your age:"))
    print("you can ride")
    if age<12 :
        bill = 5
    elif age>=12 and age <=18:
        bill = 7
    else: 
        bill = 12
    wantPhoto = input("do you want a photo")
    if wantPhoto=="true":
        bill = bill +3
        print(f"your bill is {bill} with a photo")
    else :
        print(f"your bill is {bill}")
print("sorry kido you cant ride")   

