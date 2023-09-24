class Count1InBinary:

    
    def counter(n):
        number=n
        count=0
        while number>=2:
            if number%2>=1:
               count=count+1

            
            number=number/2
            print(number)
        if number<2:
            count=count+1
                
            

        
        
        return count
    
    print(counter(13))

