#EST.MOD_LT01.20
#Declaração de variáveis
n1=0.0
n2=0.0
n3=0.0
n4=0.0

#Início
def calc_notas():
    global n1, n2, n3, n4
    media=(n1+n2+n3+n4)/4
    if (media>10):
        print("Inválido")
        return
    elif (media>=6.0):
        print("Aprovado, sua média foi:",media)
    elif (media<6.0 and media>=3.0):
        print("Exame, sua média foi:",media)
    else:
        print("Reprovado, sua média foi:",media)
        
def main():
    global n1, n2, n3, n4
    print("--- Exercicio 21 ---")
    n1=float(input("Insira a primeira nota: "))
    n2=float(input("Insira a segunda nota: "))
    n3=float(input("Insira a terceira nota: "))
    n4=float(input("Insira a última nota: "))
    calc_notas()
    
if (__name__ == "__main__"):
    main()

#Fim
