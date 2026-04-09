#EST.MOD_LT01.22
#Declaração de variáveis
x=0
y=0

#Início
def calc_seq():
    global x, y
    if (x>y):
        print (f"A ordem é essa:{x} e {y}.")
    else:
        print (f"A ordem é essa: {y} e {x}.")
    
def main():
    global x, y
    print("--- Exercicio 22 ---")
    x=int(input("Insira o primeiro valor: "))
    y=int(input("Insira o segundo valor: "))
    calc_seq()
    
if (__name__ == "__main__"):
    main()

#Fim
