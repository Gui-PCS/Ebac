import re

def calculo(calc):                          #resolve uma operação (definida por calc[1]) de 2 números (calc[0] e calc[2])
    if calc[1] == '+':
        result = int(calc[0])+int(calc[2])
    elif calc[1] == '-':
        result = int(calc[0])-int(calc[2])
    elif calc[1] == '*':
        result = int(calc[0])*int(calc[2])
    elif calc[1] == '/':
        result = int(int(calc[0])/int(calc[2]))
    else:
        result = ("Operação invalida")
    return(result)

def calculadora(op):                        #prepara a operação para ser resolvida na função Calculo
    ops = r"(\+|\-|\*|/)"
    calc = re.split(ops, op)                #transforma a sting op em uma lista de números e operadores
    if len(calc) == 3:
        return(calculo(calc))
    elif len(calc) > 3:
        while len(calc) > 1:                #como a função Calculo opera apenas com uma lista de 3 elementos por vez
            resultado = calculo(calc[:3])   #3 elementos são enviados
            calc = calc[3:]                 #os 3 já utilizados são descartados
            calc.insert(0, str(resultado))  #e o resultado do primeiro calculo é adicionado ao inicio da lista para que a operação possa continuar
        return(resultado)
    else:
        return("Operação invalida")

loop = 's'                                  #loop para permitir farias operações diferentes
while loop == 's':
    op = input(str("Escreva a operação:"))  #operação pode ser escrita inteira
    print(calculadora(op))                  #chamado da função Calculadora
    loop = input(str("Repetir?[s/n]"))      #encerra ou continua o loop
