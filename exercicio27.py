#EST.MOD_LT01.27
#Declaração de variáveis

#Início
def calc_velocidade(voltas, distancia, temp):
    dtotal = (distancia / 1000) * voltas
    ttotal = temp / 60
    vm = dtotal/ttotal
    print("A velocidade média é:", round(vm, 2), "km/h")

def main():
    print("--- Exercício 27 ---")
    dist = float(input("Insira a extensão do circuito, em metros: "))
    nvoltas = float(input("Insira a quantidade de voltas: "))
    tempo = float(input("Insira a duração, em minutos: "))
    calc_velocidade(nvoltas,dist, tempo)

if __name__ == "__main__":
    main()

#Fim]
