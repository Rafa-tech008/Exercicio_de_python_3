#EST.MOD_LT01.28
#Declaração de variáveis

#Início
def calc_media(preço,valormen):
    if(valormen<500 and preço<30):
        print ("O valor do produto é igual a:",preço+(preço*0.1))
    elif(valormen>=500 and valormen<1000 and preço>=30 and preço<80):
        print ("O valor do produto é igual a:",preço+(preço*0.15))
    elif(valormen>=1000 and preço>=80):
        print ("O valor do produto é igual a:",preço-(preço*0.05))
    else:
        print ("O valor do produto se mantém igual")

def main():
    print("--- Exercício 28 ---")
    pat=int(input("O preço do produto é: "))
    vmen=int(input("A média de vendas do produto é: "))
    calc_media(pat,vmen)

if __name__ == "__main__":
    main()

#Fim
