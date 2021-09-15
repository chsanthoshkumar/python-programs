"""4.	Print all Prime numbers in an Interval"""
lower=int(input("enter lower"))
upper=int(input("enter upper"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
