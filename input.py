x = float(input("total cart amount: "))

if x<200 and x>0:
    print("your payable amount with delivery charges and taxes is ", x+33+((x/100)*10))
elif x>=200:
    print("you unlocked free delivery with low tax ", x+((x/100)*5))
else:
    print("you cant give -ve amount or 0")