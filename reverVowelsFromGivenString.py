


def reverseVowelInGivenString():

    input_val=input("enter string : ")


    vowels=[]

    for character in input_val:

        if character in "aeiouAEIOU":
            vowels.append(character)
    
    result_string=""
    reversed_vowels=vowels[::-1]
    counter=0
    for character in input_val:

        if character in "aeiouAEIOU":
            result_string=result_string+reversed_vowels[counter]
            counter=counter+1
        
        else:
            result_string=result_string+character




    print(result_string)

reverseVowelInGivenString()