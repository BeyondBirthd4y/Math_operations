encerrar = 0
while (encerrar!="s"):
    d = float(input("Digite a distância percorrida, em km:"))
    t = float(input("Digite o tempo do trajeto, em horas:"))
    v=d/t
    print("A velocidade do trajeto foi de", v,"km/h")
    print()
    encerrar = str(input("Deseja encerrar o programa [s/n] ?"))
    print("")
    if (encerrar!="s"):
        continuar= str(input("deseja calcular a velocidade em m/s ?"))
        if(continuar=="s"):
            met_sec= v/3.6
            print("A velocidade é de", met_sec, "m/s")
            encerrar = str(input("Deseja encerrar o programa [s/n] ?"))
            
    
    
    
    
