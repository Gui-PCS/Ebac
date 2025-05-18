# Ebac

Este script implementa uma calculadora simples que processa operações matemáticas básicas, soma, subtração, múltiplicação e divisão (+, -, *, /), a partir de uma string digitada pelo usuário. Ele permite executar várias operações sequenciais e processa expressões da esquerda para a direita, sem considerar precedência de operadores.

### Função: calculo(calc)
```
def calculo(calc):
```
Executa uma operação aritmética básica entre dois operandos com base no operador fornecido.

Parâmetro:
- calc: lista com 3 elementos no formato [1º número, operador, 2º número].
Funcionamento:
- Realiza a operação correspondente (+, -, *, /) entre calc[0] e calc[2].
- Retorna o resultado inteiro da operação.
- Se o operador for inválido, retorna "Operação invalida".

Exemplo:
```
calculo(["3", "+", "5"])  # Retorna 8
```

### Função: calculadora(op)
```
def calculadora(op):
```
Objetivo:
Processa uma string representando uma expressão matemática simples e resolve-a sequencialmente.

Parâmetro:
op: string representando a operação (ex: "2+3*4").

Funcionamento:
1. Usa re.split com uma expressão regular para dividir a string op em operandos e operadores.
2. Se houver apenas 3 elementos (ex: "2+3"), chama diretamente calculo.
3. Se houver mais de 3 (ex: "2+3+4"), resolve sequencialmente da esquerda para a direita:
4. Executa a operação com os 3 primeiros elementos.
5. Substitui esses elementos pelo resultado e continua o processo até sobrar apenas um resultado final.
6. Caso a entrada seja inválida, retorna "Operação invalida".

### Loop Principal
```
loop = 's'
while loop == 's':
```
Objetivo:
Permite que o usuário faça várias operações seguidas.

Funcionamento:
- Solicita ao usuário a operação completa.
- Chama a função calculadora para processar e exibir o resultado.
- Pergunta ao usuário se deseja repetir (s para sim, n para não).

### Exemplo de Execução
```
Escreva a operação: 2*3+4
Resultado: 10  <- (interpreta como (2*3)=6, depois 5+4=10)
Repetir?[s/n]: n <- (fim do loop)
```

##Execução
Para executar o script use: `./calculadora.sh` em um terminal Linux.
