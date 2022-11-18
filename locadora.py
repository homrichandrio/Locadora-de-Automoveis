## exibir tela com a seleção incial 
# variavel opcao1 define qual será o fluxo que o usuário irá seguir
# variavel opcao2 define qual será o carro que será locado quando houver
import os
import sys
import time as tm

portfolio_catalogo = [
'Fiat Hatch - R$ 90',
'Chevrolet Hatch - R$ 100',
'Hyundai Hatch - R$ 110',
'Fiat Sedan - R$ 110',
'Chevrolet Sedan - R$ 120',
'Hyundai Sedan - R$ 140',
'Fiat SUV - R$ 150',
'Chevrolet SUV - R$ 165',
'Hyundai SUV - R$ 170'
]

portfolio_alugado = []
portfolio_disponivel = []


while True:
    os.system('cls') or None
    print("---------------------------------------------------------------------\nSoftware de Gestão de Locação de Veículos\n---------------------------------------------------------------------\n")
    print('| 0 - Exibir Portfolio | 1 - Alugar um Veículo | 2 - Devolver um Veículo | 3 - Sair |')
    opcao1 = int(input('Selecione a opção conforme as opções acima: ')) 
# exibição do catalogo completo
    if opcao1 == 0:
        os.system('cls') or None
        print("---------------------------------------------------------------------\nCATÁLOGO DE VEÍCULOS\n---------------------------------------------------------------------\n")
        print('Confira nossos veículos:\n')
        for i in portfolio_catalogo:
            print('{} - {}'.format(portfolio_catalogo.index(i),i))
        input('\nDeseja voltar? (Tecle X e Enter)\n')
        continue
# seleção do carro a ser alugado        
    elif opcao1 == 1:
        os.system('cls') or None
        print("---------------------------------------------------------------------\nVEÍCULOS DISPONÍVEIS PARA LOCAÇÃO\n---------------------------------------------------------------------\n")
        print('Confira nossos veículos disponíveis: \n')
        portfolio_disponivel = [i for i in portfolio_catalogo if i not in portfolio_alugado]
        for i in portfolio_disponivel:
            print('{} - {}'.format(portfolio_disponivel.index(i),i))
        print('')
        escolha_carro_disponivel = int(input('Digite o código do carro que você deseja alugar: '))
        os.system('cls') or None
        print("---------------------------------------------------------------------\nPERÍODO DE LOCAÇÃO\n---------------------------------------------------------------------\n")
        print('Veículo {} Selecionado. O valor da diária para aluguel do carro é de R$ {}.'.format(portfolio_disponivel[escolha_carro_disponivel],(portfolio_disponivel[escolha_carro_disponivel].split(' '))[4]))
        dias_alugado = input('Você gostaria de alugar por quantos dias? \n')
        valor_aluguel = int((portfolio_disponivel[escolha_carro_disponivel].split(' '))[4])*int(dias_alugado)
        os.system('cls') or None
        print("---------------------------------------------------------------------\nCONFIRMAÇÃO DE LOCAÇÃO\n---------------------------------------------------------------------\n")
        escolha_confirmacao = input('O valor do aluguel será de R$ {}. Deseja continuar? \n(Tecle X para Cancelar e Enter. Para continuar pressione qualquer tecla e pressione Enter. )\n'.format(valor_aluguel))
        if escolha_confirmacao == 'X' or escolha_confirmacao == 'x':
            continue
        else:
            portfolio_alugado.append(portfolio_disponivel[escolha_carro_disponivel])
        # seleçõa do carro a ser devolvido
    elif opcao1 == 2:
        os.system('cls') or None
        print("---------------------------------------------------------------------\nDEVOLUÇÃO DE VEÍCULOS\n---------------------------------------------------------------------\n")
        print('Selecione o veículo a ser devolvido: \n')
        for i in portfolio_alugado:
            print('{} - {}'.format(portfolio_alugado.index(i),i))
        escolha_carro_devolucao = int(input('\nDigite o código do carro que você deseja devolver: '))
        os.system('cls') or None
        print("---------------------------------------------------------------------\nCONFIRMAÇÃO DE DEVOLUÇÃO\n---------------------------------------------------------------------\n")
        print('Veículo {} Selecionado. Deseja continuar com a devolução? \n(Aperte X e Enter para Cancelar. Para continuar, pressione qualquer tecla) \n'.format(portfolio_alugado[escolha_carro_devolucao]))              
        opcao2 = input()
        if opcao2 == 'x' or opcao2 == 'X':
            continue
        else:
            print('Veículo {} devolvido à locadora.'.format(portfolio_alugado[escolha_carro_devolucao]))
            portfolio_alugado.remove(portfolio_alugado[escolha_carro_devolucao])

    elif opcao1 == 3:
        os.system('cls') or None
      
        break

print('------------------------------------------------------------------\nVocê utilizou o programa Software de Gestão de Locação de Veículos\n------------------------------------------------------------------\n')
print('Este programa foi desenvolvido por Andrio Homrich.\nVersão 1.1 lançada em 17.11.2022\n\n------------------------------------------------------------------\nVolte Sempre!\n------------------------------------------------------------------\n')
tm.sleep(2)      
sys.exit()