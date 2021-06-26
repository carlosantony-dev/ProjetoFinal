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
if salariobruto <= 1100:
    salarioseminss = salariobruto - (0.075*salariobruto)
    aliquotainss = 0.075
    
if salariobruto >= 1100.01 and salariobruto <= 2203.48:
    salarioseminss = salariobruto - (0.09*salariobruto)
    aliquotainss = 0.09

if salariobruto >= 2203.49 and salariobruto <= 3305.22:
    salarioseminss = salariobruto - (0.12*salariobruto)
    aliquotainss = 0.12

if salariobruto >= 3305.23:
    salarioseminss = salariobruto - (0.14*salariobruto)
    aliquotainss = 0.14


# Calculo substração do IRFF e férias

if salariobruto <= 1903.98 :
    salarioseminsssemirff = salarioseminss
    aliquotairrf = 0

if salariobruto >= 1903.99 and salariobruto <= 2826.6:
    salarioseminsssemirff = salarioseminss - (0.057*salarioseminss)
    aliquotairrf = 0.075

if salariobruto >= 2826.66 and salariobruto <= 3751.05:
    salarioseminsssemirff = salarioseminss - (0.15*salarioseminss)
    aliquotairrf = 0.15

if salariobruto >= 3751.06 and salariobruto <= 4664.68:
    salarioseminsssemirff = salarioseminss - (0.225*salarioseminss)
    aliquotairrf = 0.225

if salariobruto >= 4664.69:
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
    inssferias = (salariobruto*aliquotainss)
    irrfferias = (salariobruto*aliquotairrf)
    desconto = inssferias + irrfferias
    ferias = provento - desconto
    
    
 #CalculoDecimoTerceiro

if meses < 12:
    feriasSituacao = 'Não é elegível a receber decimo terceiro salário com menos de 12 meses trabalhados via CLT'
else:
    total = (salariobruto/12)*meses
    if total <= 1751.81:
        inssdecimo = 0.08*total
        totalseminss = total - inssdecimo
        aliquotainss1 = 0.08
    
    if total >= 1751.82 and total <= 2919.72:
        inssdecimo = (0.09*total)
        totalseminss = total - inssdecimo
        aliquotainss2 = 0.09

    if total >= 2919.73 and total <= 5839.45:
        inssdecimo = (0.11*total)
        totalseminss = total - inssdecimo
        aliquotainss2 = 0.11

    if total >= 5839.45:
        inssdecimo = 642.34
        totalseminss = total - inssdecimo
        aliquotainss4 = 642.34

    if totalseminss <= 1903.98 :
        totalseminsssemirff = totalseminss
        aliquotairrf = 0
        decimo = round(totalseminsssemirff,2)
        deduzirdecimo = salariobruto - totalseminsssemirff
    
    if totalseminss >= 1903.99 and totalseminss <= 2826.6:
        totalseminsssemirff = totalseminss - (0.057*totalseminss)
        aliquotairrf = 0.075
        decimo = round(totalseminsssemirff,2)
        deduzirdecimo = salariobruto - totalseminsssemirff

    if totalseminss >= 2826.66 and totalseminss <= 3751.05:
        totalseminsssemirff = totalseminss - (0.15*totalseminss)
        aliquotairrf = 0.15
        decimo = round(totalseminsssemirff,2)
        deduzirdecimo = salariobruto - totalseminsssemirff

    if totalseminss >= 3751.06 and totalseminss <= 4664.68:
        totalseminsssemirff = totalseminss - (0.225*totalseminss)
        aliquotairrf = 0.225
        decimo = round(totalseminsssemirff,2)
        deduzirdecimo = salariobruto - totalseminsssemirff

    if totalseminss >= 4664.69:
        totalseminsssemirff = totalseminss - (0.275*totalseminss)
        aliquotairrf = 0.275
        decimo = round(totalseminsssemirff,2)
        deduzirdecimo = salariobruto - totalseminsssemirff
    
    

    

valordeinss = salariobruto*aliquotainss
valordabasedecalculo = salariobruto
valoradeduzir = salariobruto - salarioseminsssemirff
valordeirrf = salariobruto*aliquotairrf
salarioliquido = (salariobruto - valordeinss) - valordeirrf

# Impressão no txt
with open('Valores.txt', 'w') as arquivo:
    arquivo.write('Nome: ' + nome + '\n')
    arquivo.write('Setor: ' + setor + '\n')

    arquivo.write('\n')
    arquivo.write('| SALÁRIO MENSAL |' + str(salariobruto) + '\n')
    arquivo.write('\n')

    arquivo.write('INSS:' + '\n')
    arquivo.write('Valor total bruto: ' + str(salariobruto + bonus) + '\n')
    arquivo.write('Valor de INSS: ' + str(valordeinss) + '\n')
    arquivo.write('Valor da base de cálculo: ' + str(valordabasedecalculo) + '\n')

    arquivo.write('\n')

    arquivo.write('IRFF:' + '\n')
    # arquivo.write('Valor a deduzir:' + str(valoradeduzir) '\n')
    arquivo.write('Valor de IRRF: ' + str(valordeirrf) +'\n')
    arquivo.write('Valor a deduzir: ' + str(valoradeduzir) +'\n')
    arquivo.write('Valor Salário líquido: ' + str(salarioliquido) +'\n')

    arquivo.write('\n')

    arquivo.write('FÉRIAS:' + str(feriasSituacao) + '\n')
    arquivo.write('Valor total de férias :' + str(provento) + '\n')
    arquivo.write('Valor de INSS de férias :' + str(inssferias) + '\n')
    arquivo.write('Valor da base da Cálculo de Férias :' + str(valordabasedecalculo) + '\n')
    arquivo.write('Valor a deduzir de Férias :' + str(desconto) + '\n')
    arquivo.write('Valor de IRRF de férias :' + str(irrfferias) + '\n')
    arquivo.write('Férias líquido :' + str(ferias) + '\n')
    
    arquivo.write('\n')
    
    arquivo.write('13º SALÁRIO' + '\n')
    arquivo.write('Valor total trabalhado: ' + str(total) + '\n')
    arquivo.write('Valor de INSS de 13º Salário: ' + str(inssdecimo) + '\n')
    arquivo.write('Valor da Base da Cálculo de 13º Salário: ' + str(salariobruto) + '\n')
    arquivo.write('Valor a deduzir de 13º Salário: ' + str(deduzirdecimo) + '\n')
    arquivo.write('Valor de IRRF de 13º Salário: ' + str(aliquotairrf) + '\n')
    arquivo.write('13º Salário líquido: ' + str(decimo) + '\n')
