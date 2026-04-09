#EST.MOD_LT01.19
#Declaração de variáveis
a=0
b=0
c=0

#Início
def calc_2grau():
    global a , b , c
    delta=((b**2)-(4*a*c))
    if (delta<0):
        print ("Não há nenhuma raíz e o delta é negativo")
        return
    elif (delta==0):
        print ("Há apenas uma raíz e delta é:",delta)
    else:
        print ("Há duas raízes e delta é:",delta)
        
    raiz1=(-(-b)+(delta**0.5)/2*a)
    raiz2=(-(-b)-(delta**0.5)/2*a)
    if (raiz1==raiz2):
        print ("O valor da raiz é:",raiz1)
    elif (raiz1>0 and raiz2>0):
        print (f"O valor das raízes são: {raiz1} e {raiz2}.")
    elif (raiz1<0 and raiz2<0):
        print ("O valor da raíz é:",raiz2)
    else:
        print ("O valor da raíz é:",raiz1)
        
def main():
    global a , b , c
    print("--- Exercicio 20 ---")
    a=int(input("Insira o primeiro valor: "))
    b=int(input("Insira o segundo valor: "))
    c=int(input("Insira o terceiro valor: "))
    calc_2grau()
    
if (__name__ == "__main__"):
    main()

#Fim
