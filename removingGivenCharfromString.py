





class removingGivenCharfromString:


    def removeChar():

        givenString=input('enter string : ')

        givenChar=input('enter char to remove : ')


        resultantString=""


        for x in givenString:


            if givenChar!=x:

                resultantString=resultantString+x

            
        return resultantString
        
    
    print(removeChar())

