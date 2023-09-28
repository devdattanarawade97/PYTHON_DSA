
def removeDuplicate(numbers):
    
  

    for i in range(len(numbers)):
       

        for k in range( len(numbers)-1,i+1,-1):

            
            if numbers[i]==numbers[k]:
                
                del numbers[k]

                #print(f'i={i} k={k}')
                
                
                
        
    return len(numbers)       
    
    



print(removeDuplicate([1,2,3,1,2,4,5,4]))

