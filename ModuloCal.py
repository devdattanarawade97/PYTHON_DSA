
class ModuloCal:
    def termsOfAP(x):
        arr=[]
        i=1
        while len(arr)<x:
           
            ans=(3*i)+2
            if ans%4!=0:
                arr.append(ans)
               
            
            i=i+1
        
        
        

        return arr
    
   
    #arr size
    #not divisible by 4
    
    arr=termsOfAP(2)
    print(arr)

