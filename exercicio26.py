#EST.MOD_LT01.26
#Declaração de variáveis
x=0
y=0

#Início
def calc_ordem():
    global x,y
    if (x==0 or y==0):
        print("O valor de",0,"é indivisível.")
    elif (x>y and x%y==0):
        print("O valor de",x, "é divisível por",y,".")
    elif (y>x and y%x==0):
        print("O valor de",y, "é divisível por",x,".")
    elif(x>y and x%y!= 0):
        print("Os valores não são divisíveis entre si.")
    else:
        print("Os valores não são divisíveis entre si.")
    
def main():
    global x,y
    print("--- Exercicio 26 ---")
    x=int(input("Dê o valor inicial: "))
    y=int(input("Dê o valor seguinte: "))
    
    calc_ordem()
    
if (__name__ == "__main__"):
    main()

#Fim
