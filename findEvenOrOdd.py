
def find(number):


  if(number<=2):

    return number%2==0
  
  return find(number-2)


print(find(3))



  



