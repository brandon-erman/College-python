# Gather user input
cipherText = str(input("Enter cipher text: ")).lower()

# Declare some variables for the alphabet and punctuation
# There are no integers included in this list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#punctuation = ['.', '!', '?', ',', '(', ')', '[', ']', '{', '}', '/', '\\', '*', '^', '$', ':', ';', '"', '\'', ' ']


# Brute force the cipher
for i in range(0, len(alphabet)):
    cipherDistance = i
    decipheredText = cipherText
    key = []
    
    # Create a key
    for character in range(0, len(alphabet)):
        cipherPosition = cipherDistance + character
        
        if cipherPosition >= len(alphabet):
            cipherPosition = cipherPosition - len(alphabet)
            key.append(alphabet[cipherPosition])
        else:
            key.append(alphabet[cipherPosition])
    
    # Print the shifted distance
    print("shifted: " + str(cipherDistance))
    #print(key)
    
    # Print the text based on the key
    for letter in cipherText:
        try:
            decipheredText = key[alphabet.index(letter)]
        except:
            #try:
            #    decipheredText = punctuation[punctuation.index(letter)]
            #except:
                # This is for numbers and non-included punctuation
                decipheredText = letter
        print(decipheredText, end="")
    print()
