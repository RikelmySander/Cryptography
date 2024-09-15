import random

textOne = input("Enter a phrase to be encrypted:")

# make a function for use in another files
def Cryptography(text):
    Crypto = dict()
    for Element in text:
        #Conversion test.
            #print("Element: {}".format(Element))
            #print(f"Element in ascii: {ord(Element)}")
            #print("Element in bin: {}".format(bin(ord(Element))))

        #Do arithmetic operations to shuffle the binaries and result in random binaries.
        ascii_Value = ord(Element)
        #this is the private key.
        factors = random.randint(5,15)
        shuffled_value = bin(ascii_Value*factors)
        print(f"Private key:{factors}")
        Crypto[Element] = shuffled_value[2:]
    return Crypto

crypt_dict = Cryptography(textOne)
print("".join(crypt_dict.values()))