
def find(numbers):
   max=0
   secondMax=0

 
   for i in range(len(numbers)):
    

    for k in range(i+1, len(numbers),1):

      

      if numbers[i]>numbers[k]:
        max=numbers[i]
        secondMax=numbers[k]
      
      else:
        max=numbers[k]
        secondMax=numbers[i]

    


   print(secondMax)

    


  

find([4,5,2,3,7,3,5,7,8])



  



