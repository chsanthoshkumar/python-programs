def check(str1, sstr): 
   if (str1.find(sstr) == -1): 
      print(sstr,"Is not present in the string") 
   else: 
      print(sstr,"Is present in the string") 

str1 = input("Enter the string ::>")
sstr=input("Enter Substring ::>")
check(str1, sstr) 
