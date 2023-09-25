#Checking whether a string contains only digits: Write a program that checks whether the given string contains only digits.

class checkDigitsInString:


    def checkDigit():

        status=True

        givenString=input("enter string : ")

        for x in givenString:


            if not x.isdigit():

                return False
            
            else:
                status=True

            
            return status
        
    print(checkDigit())

            