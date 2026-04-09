#EST.MOD_LT01.18
#Declaração de variáveis
v1=0
v2=0

#Início
def calc_diff():
    global v1, v2
    if v1 > v2:
        resultado=v1-v2
    else:
        resultado=v2-v1
    print("A diferença do maior pelo menor é:", resultado)

def main():
    global v1, v2
    print("--- Exercicio 18 ---")
    v1 = int(input("Insira o primeiro valor: "))
    v2 = int(input("Insira o segundo valor: "))
    calc_diff()

if (__name__ == "__main__"):
    main()

#Fim
