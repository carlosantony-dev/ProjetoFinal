# Cicero Matheus Cabral  RA: 20630406
# Carlos Antony Blecha Pires RA: 20630414
# Bruno Amorim da Silva RA: 20630380



#coding utf-8

nome = str(input("Digite o nome do funcionário: "))
setor = str(input("Digite o setor que ele trabalha: "))
salariobruto = float(input("Digite o salário bruto: "))
bonus = float(input("Digite o valor do bônus: "))
meses = int(input("Digite o número de meses trabalhados: "))
diasferias = int(input("Digite o número de dias de férias: "))

salariobruto+=bonus

# Calculo substração do INSS

# COLOCA ESSE E O DO IRFF DENTRO DE UMA FUNÇÃO para ficar mais clean
if salariobruto <= 1045:
    salarioseminss = salariobruto - (0.075*salariobruto)
    aliquotainss = 0.075
    
if salariobruto >= 1045.01 and salariobruto <= 2089.60:
    salarioseminss = salariobruto - (0.09*salariobruto)
    aliquotainss = 0.09

if salariobruto >= 2089.61 and salariobruto <= 3134.40:
    salarioseminss = salariobruto - (0.12*salariobruto)
    aliquotainss = 0.12

if salariobruto >= 3134.41:
    salarioseminss = salariobruto - (0.14*salariobruto)
    aliquotainss = 0.14


# Calculo substração do IRFF e férias

if salarioseminss >= 1903.99 and salarioseminss <= 2826.6:
    salarioseminsssemirff = salarioseminss - (0.057*salarioseminss)
    aliquotairrf = 0.075

if salarioseminss >= 2826.66 and salarioseminss <= 3751.05:
    salarioseminsssemirff = salarioseminss - (0.15*salarioseminss)
    aliquotairrf = 0.15

if salarioseminss >= 3751.06 and salarioseminss <= 4664.68:
    salarioseminsssemirff = salarioseminss - (0.225*salarioseminss)
    aliquotairrf = 0.225

if salarioseminss >= 4664.69:
    salarioseminsssemirff = salarioseminss - (0.275*salarioseminss)
    aliquotairrf = 0.275


#CALCULO DAS FÉRIAS

if meses < 12:
    feriasSituacao = 'Não é elegível a retirar férias com menos de 12 meses trabalhados via CLT'
else:
    feriasSituacao = 'Elegível a férias!'
    um_terco = (salariobruto/3)
    valor_dias_ferias = (salariobruto/30)*diasferias
    provento = (valor_dias_ferias + um_terco)
    desconto = (salariobruto - (salariobruto*aliquotainss)) + (salariobruto - (salariobruto-aliquotairrf))
    ferias = provento - desconto
    
    
 #CalculoDecimoTerceiro

if meses < 12:
    feriasSituacao = 'Não é elegível a receber decimo terceiro salário com menos de 12 meses trabalhados via CLT'
else:
    total = (salariobruto/12)*meses
    if total <= 1751.81:
        totalseminss = total - (0.08*total)
        aliquotainss1 = 0.08
    
    if total >= 1751.82 and total <= 2919.72:
        totalseminss = total - (0.09*total)
        aliquotainss2 = 0.09

    if total >= 2919.73 and total <= 5839.45:
        totalseminss = total - (0.11*total)
        aliquotainss2 = 0.11

    if total >= 5839.45:
        totalseminss = total - 642.34
        aliquotainss4 = 642.34
    
    if totalseminss >= 1903.99 and totalseminss <= 2826.6:
        totalseminsssemirff = totalseminss - (0.057*totalseminss)
        aliquotairrf1 = 0.075

    if totalseminss >= 2826.66 and totalseminss <= 3751.05:
        totalseminsssemirff = totalseminss - (0.15*totalseminss)
        aliquotairrf2 = 0.15

    if totalseminss >= 3751.06 and totalseminss <= 4664.68:
        totalseminsssemirff = totalseminss - (0.225*totalseminss)
        aliquotairrf3 = 0.225

    if totalseminss >= 4664.69:
        totalseminsssemirff = totalseminss - (0.275*totalseminss)
        aliquotairrf4 = 0.275
    
    

    

valordeinss = salariobruto - salarioseminss
valordabasedecalculo = salariobruto - valordeinss
valoradeduzir = salariobruto - salarioseminsssemirff
valordeirrf = (valordabasedecalculo * aliquotairrf) * valoradeduzir

# Impressão no txt
with open('Valores.txt', 'a') as arquivo:
    arquivo.write('Nome: ' + nome + '\n')
    arquivo.write('Setor: ' + setor + '\n')

    arquivo.write('\n')
    arquivo.write('| SALÁRIO MENSAL |' + '\n')
    arquivo.write('\n')

    arquivo.write('INSS:' + '\n')
    arquivo.write('Valor total bruto: ' + str(salariobruto + bonus) + '\n')
    arquivo.write('Valor de INSS: ' + str(valordeinss) + '\n')
    arquivo.write('Valor da base de cálculo: ' + str(valordabasedecalculo) + '\n')

    arquivo.write('\n')

    arquivo.write('IRFF:' + '\n')
    # arquivo.write('Valor a deduzir:' + str(valoradeduzir) '\n')
    arquivo.write('Valor de IRRF: ' + str(valordeirrf) +'\n')
    arquivo.write('Valor a deduzir: ' + str(valordeirrf) +'\n')
    arquivo.write('Valor Salário líquido: ' + str(valordeirrf) +'\n')

    arquivo.write('\n')

    arquivo.write('FÉRIAS:' + str(feriasSituacao) + '\n')
    arquivo.write('Valor total de férias :' + '\n')
    arquivo.write('Valor de INSS de férias :' + '\n')
    arquivo.write('Valor da base da Cálculo de Férias :' + '\n')
    arquivo.write('Valor a deduzir de Férias :' + '\n')
    arquivo.write('Valor de IRRF de férias :' + '\n')
    arquivo.write('Férias líquido :' + str(ferias) + '\n')
    
    arquivo.write('\n')
    
    arquivo.write('13º SALÁRIO' + '\n')
    arquivo.write('Valor total trabalhado: ' + '\n')
    arquivo.write('Valor de INSS de 13º Salário: ' + '\n')
    arquivo.write('Valor da Base da Cálculo de 13º Salário: ' + '\n')
    arquivo.write('Valor a deduzir de 13º Salário: ' + '\n')
    arquivo.write('Valor de IRRF de 13º Salário: ' + '\n')
    arquivo.write('13º Salário líquido: ' + '\n')






    
