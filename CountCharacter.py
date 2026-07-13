text="nanamammkkkjjyyytuionhh"
# I create an empty dictionary  in python name freq
freq={}
#  T use  a for loop for iteration 
for currChar in text:
    print("currentCharacter :" ,currChar)
    print("Dictionary:",freq)
    existingFreq=freq.get(currChar,0)
    print("Frequency of current character in dictionary: " ,existingFreq)
    freq[currChar]=existingFreq+1
    print("Increasing frequency by  1 :" ,freq)
    print("Length of String : ",len(text))
