#coding utf-8

nome = str(input("Digite o nome do funcionário: "))
setor = str(input("Digite o setor que ele trabalha: "))
salariobruto = float(input("Digite do salário bruto: "))
bonus = float(input("Digite o valor do bônus: "))
meses = int(input("Digite o número de meses trabalhados: "))
diasferias = int(input("Digite o número de dias de férias: "))

# Calculo substração do INSS

# COLOCA ESSE E O DO IRFF DENTRO DE UMA FUNÇÃO para ficar mais clean
if salariobruto <= 1045:
    salarioseminss = salariobruto - (0.075*salariobruto)

if salariobruto >= 1045.01 and salariobruto <= 2089.60:
    salarioseminss = salariobruto - (0.09*salariobruto)

if salariobruto >= 2089.61 and salariobruto <= 3134.40:
    salarioseminss = salariobruto - (0.12*salariobruto)

if salariobruto >= 3134.41:
    salarioseminss = salariobruto - (0.14*salariobruto)


# Calculo substração do IRFF

if salarioseminss >= 1903.99 and salarioseminss <= 2826.6:
    salarioseminsssemirff = salarioseminss - (0.057*salarioseminss)
    aliquotairff = 0.075

if salarioseminss >= 2826.66 and salarioseminss <= 3751.05:
    salarioseminsssemirff = salarioseminss - (0.15*salarioseminss)
    aliquotairff = 0.15

if salarioseminss >= 3751.06 and salarioseminss <= 4664.68:
    salarioseminsssemirff = salarioseminss - (0.225*salarioseminss)
    aliquotairff = 0.225

if salarioseminss >= 4664.69:
    salarioseminsssemirff = salarioseminss - (0.275*salarioseminss)
    aliquotairff = 0.275

valordeinss = salariobruto - salarioseminss
valordabasedecalculo = salariobruto - valordeinss
# valoradeduzir = 
valordeirff= (valordabasedecalculo * aliquotairff) * valoradeduzir

with open('Valores.txt', 'a') as arquivo:
    arquivo.write('Nome: ' + nome + '\n')
    arquivo.write('Setor: ' + setor + '\n')

    arquivo.write('\n')
    arquivo.write('| Salário mensal |' + '\n')
    arquivo.write('\n')

    arquivo.write('INSS:' + '\n')
    arquivo.write('Valor total bruto: ' + str(salariobruto + bonus) + '\n')
    arquivo.write('Salário sem INSS: ' + str(salarioseminss) + '\n')
    arquivo.write('Valor de INSS: ' + str(valordeinss) + '\n')
    arquivo.write('Valor da base de cálculo: ' + str(valordabasedecalculo) + '\n')

    arquivo.write('IRFF:' + '\n')
    # arquivo.write('Valor a deduzir:' + str(valoradeduzir) '\n')


    
