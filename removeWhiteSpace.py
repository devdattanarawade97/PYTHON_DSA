""""
Removing white spaces from a string: Write a program that removes all white spaces from the given string.
"""

class removeWhiteSpace:


    def removeSpace():


        givenString=input('enter your string : ')


        resultString=""


        for x in givenString:


            if(x!=" "):

                resultString=resultString+x

            
        return resultString
    

    print(removeSpace())

