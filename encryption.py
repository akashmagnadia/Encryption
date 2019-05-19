
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    output = ''
    for i in range (len(msg)):
        if (msg[i] == ' '):
            output += '$'
        elif (letters.index(msg[i])+ key > 25):
            temp = int(letters.index(msg[i])+ key)
            while (temp > 25):
                temp -= 26
            output += letters[temp]
        else:
            output += letters[(letters.index(msg[i]))+ (key)]
        
        
    print("Encrypted Message: " + output)

def decrypt():
    output = ''
    for i in range (len(msg)):
        if (msg[i] == '$'):
            output += ' '
        elif (letters.index(msg[i]) - key < 0):
            temp = int(letters.index(msg[i]) - key)
            while (temp < 0):
                temp += 26
            output += letters[temp]
        else:
            output += letters[(letters.index(msg[i])) - (key)]

    print("Decrypted Message: " + output)

def convert():
    num = 0
    multiplier = 1;
    word = input("what's the word you would like to encrypt with? ")
    for i in range (len(word)):
        if (i > 0):
            multiplier *= 10
            num += letters.index(word[i]) * multiplier

    
again = input("Are you sure you want to run this program? ")

while((again != 'no')):
    option = (input("Do you want to encrypt or decrypt? "))
    if ((option == 'encrypt') | (option == 'Encrypt')):
        msg = (input("What's the message you want to encrypt? "))
        convert = input("Would you like to encrypt with word or number? ")
        
        if (convert == 'word'):
            num = 0
            multiplier = 1;
            word = input("what's the word you would like to encrypt with? ")
            for i in range (len(word)):
                if (i > 0):
                    multiplier *= 10
                    num += letters.index(word[i]) * multiplier
                    key = num
        else:
            key = int((input("What's the encryption number")))
        encrypt()
    elif ((option == 'decrypt') | (option == 'Decrypt')):
        msg = (input("What's the encrypted message? "))
        convert = input("Would you like to decrypt with word or number? ")
        
        if (convert == 'word'):
            num = 0
            multiplier = 1;
            word = input("what's the word you would like to decrypt with? ")
            for i in range (len(word)):
                if (i > 0):
                    multiplier *= 10
                    num += letters.index(word[i]) * multiplier
                    key = num
        else:
            key = int((input("What's the decryption number")))

        decrypt()
    else:
        print("I don't understand")
    again = input("Do you want to run this program once again? ")

