import pandas as pd
import json
import numpy as np

ligacao = '\033[31m'
ifRule = '\033[32m'
then = '\033[34m'
equals = '\033[33m'
variavel = '\033[0;0m'

#Vai remover os caracteres especiais das regras
def replaceRule(rule):
    rule = rule.replace("IF ", "")
    rule = rule.replace("AND", ";")
    rule = rule.replace(">", "=>")
    rule = rule.replace("<", "=<")
    return rule

def processRules(rulesList):
    dictionaryRules = []
    for  i in rulesList: 
        if i.find('OR') != -1:
            #quebra em daus siple rule
            i = replaceRule(i)
            compostRule = i.split("THEN")
            rulesBroken = compostRule[0].split("OR")
            target = compostRule[1].split("=")
            for x in range(len(rulesBroken)):
                rulesBroken[x] = rulesBroken[x].split(";");
                dictionaryRule = {}
                for j in rulesBroken[x]:
                    j = j.split("=")
                    dictionaryRule[j[0].strip()] = j[1].strip()
                
                dictionaryRule[target[0].strip()] = target[1].strip()
                
                dictionaryRules.append(dictionaryRule)

        elif i.find('AND') != -1:
            i = replaceRule(i)
            i = i.replace("THEN", ";")
            i = i.split(";")
            
            dictionaryRule = {}
            for x in i:
                x = x.split("=")
                dictionaryRule[x[0].strip()] = x[1].strip()
            dictionaryRules.append(dictionaryRule)
        else:
            i = replaceRule(i)
            i = i.replace("THEN", ";")
            i = i.split(";")
            dictionaryRule = {}
            for x in i:
                #print(x)
                x = x.split("=")
                #print(x)
                dictionaryRule[x[0].strip()] = x[1].strip()
            dictionaryRules.append(dictionaryRule)
    return(dictionaryRules)

def printMenu():
    print("===== Agente inteligente =====")
    print("1 - Cadastrar regras")
    print("2 - Cadastrar variaveis")
    print("3 - Predizer variavel (loop de execusão)")
    print("0 - Sair do programa")
    print("==============================")
    return int(input("Digite uma das opções acima listadas: "))

if __name__ == "__main__" :          
    #Ler o arquivo de regras para iniciar o programa
    with open('rules.txt', 'r') as rulesTxt: 
        rules = json.load(rulesTxt)

    #Ler o arquivo de variaveis para iniciar o programa
    with open('variables.txt', 'r') as variablesTxt: 
        variablesList = json.load(variablesTxt)    
        
    #Transforma as regras em lista
    rulesList = rules

    opcMenu = printMenu()
    while opcMenu:
        if opcMenu == 1:
            rule = 'IF '
            rulePrint = ifRule + 'IF '
            opcRule = 0
            quantVariaveis = 0
            while (opcRule == 1 or quantVariaveis == 0):
                
                print(rulePrint + variavel + "...")
                print("Criando regra:")
                print("1 - Adicionar uma variavel")
                print("2 - Para finalizar (deve conter pelo menos uma variavel)")
                print("0 - Para sair")
                opcRule = int(input("Digite uma opção: "))
                
                if opcRule == 1: 
                    if quantVariaveis != 0: 
                        print("Operador logico: ")
                        print("0 - AND")
                        print("1 - OR")
                        operador = int(input("Digite o operador: "))
                        if (operador):
                            rulePrint += ligacao + " OR "
                            rule += " OR "
                        else:
                            rulePrint += ligacao + " AND "
                            rule += " AND "
                            
                        print(rulePrint + variavel + '...')
                        count = 0
                        for i in variablesList:
                            print(count , " - " ,  i)
                            count += 1
                        opcVariavel = int(input("Escolha uma variavel: "))

                        rulePrint += variavel + list(variablesList.keys())[opcVariavel] + equals + ' = ' + variavel
                        rule += list(variablesList.keys())[opcVariavel] + ' = '

                        print(rulePrint)

                        count = 0
                        for i in variablesList[list(variablesList.keys())[opcVariavel]]:
                            print(count , " - " ,  i)
                            count += 1
                        opcAtt = int(input("Escolha um estado: "))

                        rulePrint += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                        rule += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                        print(rulePrint)
                        quantVariaveis += 1
                    else:
                        count = 0
                        for i in variablesList:
                            print(count , " - " ,  i)
                            count += 1
                        opcVariavel = int(input("Escolha uma variavel: "))

                        rulePrint += variavel + list(variablesList.keys())[opcVariavel] + equals + ' = ' + variavel
                        rule += list(variablesList.keys())[opcVariavel] + ' = '

                        print(rulePrint)

                        count = 0
                        for i in variablesList[list(variablesList.keys())[opcVariavel]]:
                            print(count , " - " ,  i)
                            count += 1
                        opcAtt = int(input("Escolha um estado: "))

                        rulePrint += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                        rule += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                        print(rulePrint)
                        quantVariaveis += 1
                elif opcRule == 2:
                    count = 0
                    rulePrint +=  then + ' THEN ' + variavel
                    rule += ' THEN '
                    print(rulePrint)
                    for i in variablesList:
                        print(count , " - " ,  i)
                        count += 1
                    opcVariavel = int(input("Escolha uma variavel: "))
                    
                    rulePrint += list(variablesList.keys())[opcVariavel] + equals + ' = ' + variavel 
                    rule += list(variablesList.keys())[opcVariavel] + ' = '
                    
                    print(rulePrint)
                    
                    count = 0
                    for i in variablesList[list(variablesList.keys())[opcVariavel]]:
                        print(count , " - " ,  i)
                        count += 1
                    opcAtt = int(input("Escolha um estado: "))
                    
                    rulePrint += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                    rule += variablesList[list(variablesList.keys())[opcVariavel]][opcAtt]
                    print(rulePrint)
                    
                    print ('Nova regra adicionada: ' + rulePrint)
                    print (rule)

                    rulesList.append(rule)
                    break
                else: 
                    quantVariaveis = 1
                    break

        elif opcMenu == 2:
            newVariavel = {}
            nomeVariavel = input("Nome da variavel: ")
            if (len(nomeVariavel) != 0):
                newVariavel[nomeVariavel] = []
                qtdOpc = 0
                while(len(newVariavel) == 0 or qtdOpc == 0):
                    print("Nova variavel : " , newVariavel)
                    print("1 - Criar opção")
                    print("2 - Sair e salvar")
                    print("0 - Sair e descartar")
                    opcVar = int(input("Opção: "))
                        
                    if (opcVar == 1):
                        newOpc = input("Digite a nova opção: ")
                        if (len(newOpc) != 0):
                            newVariavel[nomeVariavel].append(newOpc)
                    elif(opcVar == 2): 
                        print("Nova variável adicionada com sucesso!!!")
                        variablesList[nomeVariavel] = newVariavel[nomeVariavel]
                        break
                    else:
                        break
            else: 
                print("Nome da variavel invalido!!!")
                
        elif opcMenu == 3:
            dictionaryRules = processRules(rulesList)
            print("lista de variaveis do sistema: \n")
            count = 0
            for i in variablesList:
                print("\t", count , " - " , i)
                count += 1
            predicao = input("Digite o nome da variavel que deseja predizer: ")
            useRule = []
            for i in dictionaryRules:
                if (list(i.keys())[-1] == predicao):
                    useRule.append(i)
            if len(useRule) != 0:
                rules = pd.DataFrame(useRule)
                #coloca -1 nos valores nulos
                rules = rules.fillna(-1)
                
                #processa a tabela e converte para numeros
                dict_mask = {}
                for j in range(len(rules.columns)):
                    dict_mask[rules.columns[j]] = [{'Nenhuma das opções' : -1}]
                    keys = list(rules[rules.columns[j]].value_counts().keys())
                    for i in range(len(keys)):
                        if(keys[i] != -1):
                            if (variablesList[rules.columns[j]][0] == 'NUM'):
                                rules[rules.columns[j]] = rules[rules.columns[j]].replace([keys[i]], i)
                                dict_mask[rules.columns[j]].append({keys[i]: i})
                            else:
                                rules[rules.columns[j]] = rules[rules.columns[j]].replace([keys[i]], variablesList[rules.columns[j]].index(keys[i]))
                    
                    if (variablesList[rules.columns[j]][0] != 'NUM'):
                        for val in variablesList[rules.columns[j]]:
                            dict_mask[rules.columns[j]].append({val: variablesList[rules.columns[j]].index(val)})
                
                #Remove as regras duplicadas
                rules = rules.drop_duplicates()
                
                target = list(rules[predicao].values)
                rules = rules.drop([predicao], axis=1)
                values = rules.values
                
                rulesValues = values
                for i in range(len(dict_mask) - 1):
                    print(rules.columns[i])
                    for j in range(len(dict_mask[rules.columns[i]])):
                        print(list(dict_mask[rules.columns[i]][j].values())[0] ,' - ', list(dict_mask[rules.columns[i]][j].keys())[0])
                    answer = int(input("Opção: "))
                    print('\n')
                    
                    filterRules = []
                    for k in range(len(rulesValues)):
                        if (rulesValues[k][i] == answer): 
                            filterRules.append(rulesValues[k])
                    rulesValues = filterRules

                    if len(rulesValues) == 0:
                        print("Não existe um resultado definido pelas regras")
                        break
                    elif len(rulesValues) == 1 and answer != -1:
                        for x in range(len(values)):
                            if np.array_equal(values[x],rulesValues[0]):
                                print("Resultado: ", predicao ,  "->", list(list(dict_mask[predicao])[target[x] + 1].keys())[0])
                        break
                    else:
                        continue

                print("Houve algum problema com as regras")
                
            else:
                #Salva os dados nos arquivos
                with open('rules.txt', 'w') as rulesTxt: 
                    json.dump(rulesList, rulesTxt)

                with open('variables.txt', 'w') as variablesTxt: 
                    json.dump(variablesList, variablesTxt) 
                
                print("Não possui regras para predição dessa variavel")
            


            
        opcMenu = printMenu()
