#EST.MOD_LT01.19
#Declaração de variáveis
v1=0.0
v2=0.0

#Início
def calc_big():
    global v1, v2
    if (v1 > v2):
        print("O maior é o primeiro:",v1)
    else:
        print("O maior valor é o segundo:",v2)

def main():
    global v1, v2
    print("--- Exercicio 19 ---")
    v1 = float (input("Insira o primeiro valor: "))
    v2 = float (input("Insira o segundo valor: "))
    calc_big()

if (__name__ == "__main__"):
    main()

#Fim
