from random import randint
#binario = ""
Cryptografia = input("enter a phrase to be encrypted:")
#for bit in range(Cryptografia):
    #    binario += str(randint(0 , 1))
    #
    #inteiro = int(binario)
    #print(bin(inteiro))
    #print(binario.bit_length(binario))
    # for x in Cryptografia.encode("utf-8"):     
    #     print(x, bin(x), sep="\t")
caracteres = dict()

for bit in Cryptografia:
    print("Caractere: {}".format(bit))
    print(f"ascii: {ord(bit)}")
    print("Binário: {}".format(bin(int(ord(bit)))))
    caracteres[bit] = bin(int(ord(bit)))
print(caracteres)