import math




#CALCULOS MPG
def RecuperacaoEletricidade(DistanciaTotal):
    
    EnergiaRecuperavel_perKM = 0.2
    consumo_energia_perKM = 0.67
    eficiencia = 0.70
    recuperaEnergia = EnergiaRecuperavel_perKM * DistanciaTotal * eficiencia
    gastoTotal = (consumo_energia_perKM * DistanciaTotal) - recuperaEnergia
    

    return gastoTotal

def mpg_eletrico(gastoTotal):

    CalcMPG = (33.7/gastoTotal) * 100

    return CalcMPG

def mpg_gasolina(DistanciaTotal):
    
    consumo_Gasolina_perKM = 3

    Consumo_em_mpg = (consumo_Gasolina_perKM * 0.264172)/0.621371

    conversaoMilhas = DistanciaTotal * 0.621371
    
    mpg = conversaoMilhas/Consumo_em_mpg
    
    return mpg

def poluicao(DistanciaTotal):
    Co2Emitido_gramas = DistanciaTotal * 1500
    return Co2Emitido_gramas
    
def custo_gas(DistanciaTotal):
    percorrer = DistanciaTotal * 10
    preco = percorrer * 5.85
    return preco

def custo_elec(DistanciaTotal):
    percorrer = DistanciaTotal * 0.2
    preco = percorrer * 0.656
    return preco

while True:
    print('Bom dia, bem vindo ao comparador de carros de circuitos da formula-e e da formula 1, para iniciar por favor insira o tamanho do percurso onde sera realizada a comparação:')
    tamanhoPista = float(input('Digite Tamanho da pista (em km) ex 2.933 km: \n>'))
    print('Agora por favor insira a velocidade média dos carros:')
    velocidade_media = float(input("Digite a velocidade média do corredor (em km/h) ex: 121.23 km/h:\n>"))  
    print(f'dado a velocidade média de {velocidade_media} e o tamanho da pista de {tamanhoPista}, informaremos a diferenca de MPG (Milhas por galão) entre os carros, a diferença de emissão de gases poluentes e a diferença de custo em dinheiro dos para os carros poderem percorrer o percurso proposto:\n')


    TempoTotal_min = 45  
    tempo_hora = TempoTotal_min / 60
    distancia45 = velocidade_media * tempo_hora  
    DistanciaTotal = distancia45 + tamanhoPista     

    gastoTotal = RecuperacaoEletricidade(DistanciaTotal)
    mpgElect = mpg_eletrico(gastoTotal)
    mpgGAS = mpg_gasolina(DistanciaTotal)
    
    mpgDiff = mpgElect - mpgGAS
    
    if mpgDiff > 0:
        mpg_porcentagem = ((mpgGAS/mpg_eletrico) * 100) - 100
        print(f'O MPG do carro eletrico é mais eficiente por {mpgDiff}, tornando o carro eletrico {mpg_porcentagem}% mais eficiente em gasto de energia\n')
    else: 
        mpg_porcentagem = ((mpg_eletrico/mpgGAS) * 100) - 100
        print(f'O MPG do carro à Gás é mais eficiente por {mpgDiff}, tornando o carro à Gás {mpg_porcentagem}% mais eficiente em gasto de energia\n')

