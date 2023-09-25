

#Counting occurrences of a certain character: Write a program that counts the occurrences of a certain character in a given string.


class countOccurances:


    def countOccurance():


        givenString=input('enter string : ')

        givenChar=input('enter char : ')


        count=0


        for x in givenString:


            if x==givenChar:

                count=count+1

        
        return count
    

    print(countOccurance())

