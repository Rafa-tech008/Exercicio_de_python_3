#EST.MOD_LT01.24
#Declaração de variáveis
x=0

#Início
def calc_div():
    global x
    if (x==0):
        return
    elif (x % 2 == 0 and x % 3 == 0):
        print (f"O número é divisível por 2 e 3: {x/2} e {x/3}.")
        return
    if(x % 2 == 0 ):
        print(f"O número é divisível por 2: {x/2}.")
    elif(x % 3 == 0 ):
        print(f"O número é divisível por 3: {x/3}.")
    else:
        print("O número não é divisível nem por 2 e nem por 3.")
    
def main():
    global x
    print("--- Exercicio 24 ---")
    x=int(input("Dê um valor para cálculo: "))
    
    calc_div()
    
if (__name__ == "__main__"):
    main()

#Fim
