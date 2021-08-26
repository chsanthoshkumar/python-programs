list1 = [55,85,46,241,646,45,54]

max_=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
for i in range(2,len(list1)):
   
   if list1[i]>max_:
      secondmax=max_
      max_=list1[i]
   
   else:
      if list1[i]>secondmax:
         secondmax=list1[i]
print("Second highest number is the list is : ",str(secondmax))
