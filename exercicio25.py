#EST.MOD_LT01.25
#Declaração de variáveis
hori=0
horf=0
mini=0
minf=0

#Início
def calc_horas():
    global hori,horf,mini,minf
    inicio=(hori*60)+mini
    final=(horf*60)+minf
    dur=final-inicio
    if (dur <= 0):
        dur = dur + 1440 #somando 24h se for negativo ou zero
    horf = dur // 60 # pega as horas cheias
    minf = dur % 60 # pega o que sobrou da divisão por 60 (minutos)
    print("A duração do jogo foi de:", horf, "hora(s) e", minf, "minuto(s).")
    
def main():
    global hori,horf,mini,minf
    print("--- Exercicio 25 ---")
    hori=int(input("Dê a hora inicial: "))
    horf=int(input("Dê a hora final: "))
    mini=int(input("Dê o minuto inicial: "))
    minf=int(input("Dê o minuto final: "))
    
    calc_horas()
    
if (__name__ == "__main__"):
    main()

#Fim
