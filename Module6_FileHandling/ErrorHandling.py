denominators =[1,2,3,0,5]
number=100

for denom in denominators:
    try:
        result= number/denom
        print(result)
    except ZeroDivisionError:
        print("caught an exception")


print("deva as a error")
