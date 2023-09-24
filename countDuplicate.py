

class countDuplicate:


    def countDuplicateChar():


        givenString=input('lets input given String : ')

        charSet=set()

        

        for x in givenString:
                

                charSet.add(x)

            

        print(len(givenString)- len(charSet))

    
    countDuplicateChar()



            

