# Dados constantes ajustados
energia_total = 53
tamanhoPista = 2,933  # Capacidade total da bateria em kWh   # Distância total percorrida em metros (ajustada)
TempoTotal_min = 45
# Exemplo de corredor já inserido
corredor1 = {'nome': 'Sam Bird', 'DistanciaTotal': 90.923, 'Numero de Voltas' : 32, 'Velocidade Média': 121.23, 'Energia Consumida': 52, 'Energia Restante': 1}
corredores = [corredor1]
print(corredores)

def calcular_performance():
    nome_corredr = input("Digite Nome do Corredor: ")
    velocidade_media = float(input('Digite a Velocidade Média de seu carro: '))
    tempo_hora = TempoTotal_min/60
    DistanciaTotal = velocidade_media * tempo_hora
    TotalVoltas = (DistanciaTotal + 2.933)/2933
    
    velocidade_media_ms = velocidade_media * (1000 / 3600)

    # Calcular a resistência aerodinâmica (Fd)
    rho = 1.225  # Densidade do ar em kg/m^3
    Cd = 0.7  # Coeficiente de arrasto
    A = 1.5  # Área frontal do carro em m^2
    forca_aerodinamica = 0.5 * rho * Cd * A * (velocidade_media_ms ** 2)
    print(forca_aerodinamica)
    # Calcular a resistência ao rolamento (Fr)
    massa_carro_kg = 900  # Massa do carro em kg
    Cr = 0.01  # Coeficiente de resistência ao rolamento
    g = 10  # Aceleração devido à gravidade em m/s^2
    forca_rolamento = Cr * massa_carro_kg * g
    print(forca_rolamento)
    # Calcular a força total (Ft)
    forca_total = forca_aerodinamica + forca_rolamento
    print(forca_total)
    # Calcular a potência média (P)
    potencia_media_watts = forca_total * velocidade_media_ms  # em watts
    potencia_media_kw = potencia_media_watts / 1000  # converter de watts para kW
    print(potencia_media_watts)
    print(potencia_media_kw)
    # Calcular a energia consumida (E)
    energia_consumida = potencia_media_kw * tempo_total_horas
    print(energia_consumida)    
    # Calcular a energia restante em porcentagem
    energia_restante = (1 - (energia_consumida / energia_total)) * 100
    print(energia_restante)
    
    
    # Armazenar as informações em um dicionário
    corredor = {
        'nome': nome_corredr, 'DistanciaTotal': DistanciaTotal, 'Numero Voltas' : TotalVoltas, 'Velocidade Média': velocidade_media, 'Energia Consumida': energia_consumida, 'Energia Restante': energia_restante}
    corredores.append(corredor)
    print(corredor)    
    
calcular_performance()
                            