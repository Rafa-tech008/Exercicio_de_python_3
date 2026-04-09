#EST.MOD_LT01.23
#Declaração de variáveis
n1=0
n2=0
n3=0
n4=0

#Início
def calc_seq():
    global n1, n2, n3, n4
    if(n4>n3>n2>n1):
        print("A ordem dos valores é:",n1,",",n2,",",n3,"e",n4)
    elif(n3>n4>n2>n1):
        print("A ordem dos valores é:",n1,",",n2,",",n4,"e",n3)
    elif(n3>n2>n4>n1):
        print("A ordem dos valores é:",n1,",",n4,",",n2,"e",n3)
    else:
        print("A ordem dos valores é:",n4,",",n1,",",n2,"e",n3)

def main():
    global n1, n2, n3, n4
    print("--- Exercicio 23 ---")
    n1=int(input("O valor 1: "))
    n2=int(input("O valor 2 que é maior que 1: "))
    n3=int(input("O valor 3 que é maior que 2: "))
    n4=int(input("O valor 4 que é aleatório: "))
    calc_seq()
    
if (__name__ == "__main__"):
    main()

#Fim
