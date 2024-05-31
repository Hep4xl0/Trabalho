import math

tamanhoPista = float(input('Digite Tamanho da pista ex 2.933: '))
velocidade_media = float(input("Digite a velocidade média do corredor (em km/h) ex: 121.23: "))  
TempoTotal_min = 45  
tempo_hora = TempoTotal_min / 60
distancia45 = velocidade_media * tempo_hora  
DistanciaTotal = distancia45 + tamanhoPista  
TotalVoltas = DistanciaTotal / tamanhoPista  
numVoltas = math.ceil(TotalVoltas)




gasto_per_km = 3 #L
energia_gerada_per_Litro = 45 #Mj/L




#
def calcular_performance(DistanciaTotal):
    energia_total = 53  
    EnergiaRecuperavel_perKM = 0.3
    consumo_energia_perKM = 0.67


    eficiencia = 0.70
    recuperaEnergia = EnergiaRecuperavel_perKM * DistanciaTotal * eficiencia
    gastoTotal = (consumo_energia_perKM * DistanciaTotal)-recuperaEnergia
    energiaFinal = energia_total - gastoTotal
    return recuperaEnergia

a = calcular_performance(DistanciaTotal)


print(a)




corredor1 = {'nome': 'Sam Bird', 'DistanciaTotal': 93.85, 'Numero de Voltas': 32, 'Velocidade Média': 121.23, 'Energia Consumida': 64, 'Energia Recuperada': 11.2}
corredores = [corredor1]
print(corredores)
