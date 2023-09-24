
def rotateArray(arr,n):

    i=0
    result=[]
    while i<n:
        
        if i>0:
            result.append(arr[i])
        if i==n-1:
            result.append(arr[0])
            break
        i=i+1
    return result




    

print(rotateArray([1,2,3,4],4))











    




        
    
           
   
 

    



    
