print("========Calculo de Força========")
print("Digite a massa do corpo, em kg: ")
m = float(input())
print("Digite a aceleração do corpo, em m/s^2 ")
a = float(input())
força = m*a
print("O corpo está realizando uma força de", força, "N")
print("Deseja calcular o trabalho ? (s/n)")
answer = str(input())
print("")
if (answer == "s" or answer=="sim"):
    print("========Calculo do Trabalho========")
    print("Qual o deslocamento do corpo ?(em metros)")
    desl= float(input())
    trab= força*desl
    print("O trabalho realizado será de ", trab,"J")
    print("Fim do algoritmo")
else:
    print("Fim do algoritmo")
