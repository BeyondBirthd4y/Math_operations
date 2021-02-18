#Variáveis para energia
energia_cin=  0
energia_pg= 0
decision= 0

while(decision!="sair"):
    print("Você deseja calcular energia cinética ou potencial gravitacional ?")
    print("Digite cin para calcular Energia Cinética:")
    print("Digite grav para calcular a Energia Potencial Gravitacional:")
    print("Se deseja encerrar o programa, digite sair")
    decision= str(input())
    if(decision=="cin"):
        print("Qual a massa do corpo ?")
        m= float(input())
        print("Qual a velocidade do corpo (em m/s) ?")
        V= float(input())
        energia_cin=(m*(V**2))/2
#m é massa, V é velocidade

        print("A energia cinética do corpo é: ", energia_cin)
        print()
    elif(decision=="grav"):
        print("Qual a massa do corpo ?")
        m= float(input())
        print("Qual a altura em que se encontra ?")
        h= float(input())
        energia_pg= m*9.8*h
#m é massa, h é altura e 9.8 é a aceleração gravitacional da Terra

        print("A energia potencial gravitacional do corpo é: ", energia_pg)
        print()

        
    
