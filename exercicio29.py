#EST.MOD_LT01.29
#Declaração de variáveis

#Início
def calc_investimento(poupança,rendafixa,invest):
   poup2=(poupança+(poupança*0.03)+invest)
   rfix2=(rendafixa+(rendafixa*0.05)+invest)
   print("O novo valor na poupança é:",poup2)
   print("O novo valor em renda fixa é:",rfix2)

def main():
    print("--- Exercício 29 ---")
    poup1=int(input("O valor na poupança: "))
    rfix1=int(input("O valor em renda fixa: "))
    inv=int(input("O valor investido: "))
    calc_investimento(poup1,rfix1,inv)

if __name__ == "__main__":
    main()

#Fim
