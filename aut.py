##################################### INICIO INSTALACAO/IMPORTACAO LIBS

import pip

def install(package):
    pip.main(['install', package])

try:
    import time
except ModuleNotFoundError:
    install("time")
    import time

try:
    import pyautogui
except ModuleNotFoundError:
    install("pyautogui")
    import pyautogui

import os
from datetime import datetime
import configparser

def install(package):
    pip.main(['install', package])

try:
    import pandas as pd
except ModuleNotFoundError:
    install("pandas")
    install("openpyxl")
    install("xlrd")
    import pandas as pd

import gui as gui

##################################### FIM INSTALACAO/IMPORTACAO LIBS

##################################### INICIO VARIAVEIS GLOBAIS

TITULO = 'LORO v0.1'
DIR_COMANDOS = ''
TIMER_PADRAO = 1
DIR_OUTPUT = ''
VAR = {}

##################################### FIM VARIAVEIS GLOBAIS

##################################### INICIO FUNCOES DO AUTOMATIZADOR



class automatizador():
    def __init__(self) -> None:
        pass

    def __exec_click__(com):
        com = com.replace('{','').replace('}','').replace(' ','')
        lista = com.split(',')

        print('{}: {}'.format(com, 'Lista de posições'))
        try:
            if len(lista) == 2:
                x= int(lista[0])
                y= int(lista[1])
                pyautogui.click(x=x, y=y)
        except:
            print('Lista de posições invalido!')
            msg = 'A lista de posições {} é inválida'.format(com)
            return False, msg
        return True, ''

    def __exec_timer__(com):
        print('{}: {}'.format(com, 'Timer'))
        try:
            time.sleep(float(com[1:]))
        except:
            print('Timer invalido!')
            msg = 'O timer {} é inválido'.format(com)
            return False, msg
        return True, ''

    def __exec_tecla__(com):
        print('{}: {}'.format(com, 'Teclar'))
        try:
            pyautogui.press(com)
        except:
            print('Tecla invalida!')
            msg = 'A tecla {} é inválida'.format(com)
            return False, msg
        return True, ''

    def __exec_digitacao__(com):
        print('{}: {}'.format(com, 'Digitar'))
        try:
            pyautogui.typewrite(com, 0.0001)
        except:
            print('Texto invalido!')
            msg = 'O texto {} é inválido'.format(com)
            return False, msg
        return True, ''

    def __exec_vetor__(com):
        com = com.replace('[','').replace(']','').replace(' ','')
        lista = com.split(',')

        print('{}: {}'.format(com, 'Lista de comandos'))
        try:
            if len(lista) == 1:
                pyautogui.press(lista[0])
            elif len(lista) == 2:
                pyautogui.hotkey(lista[0], lista[1])
            elif len(lista) == 3:
                pyautogui.hotkey(lista[0], lista[1], lista[2])
            else:
                pyautogui.hotkey(lista[0], lista[1], lista[2], lista[3])
        except:
            print('Lista de comandos invalido!')
            msg = 'A lista de comandos {} é inválida'.format(com)
            return False, msg
        return True, ''

    def __exec_funcao__(self, com):
        print('{}: {}'.format(com, 'Funcao'))
        try:
            if com[1:4] == 'tab':
                rep = int(com[4:].replace(':',''))
                for i in range(rep - 1):
                    self.__exec_tecla__('tab')
                    self.__exec_timer__(TIMER_PADRAO)
            else:
                print('Funcao invalida!')
                msg = 'A função {} é inválida'.format(com)
                return False, msg
        except:
            print('Erro na execucao da funcao!')
            msg = 'Erro na execução da função {}!'.format(com)
            return False, msg
        return True, ''
        
    def __exec_variavel__(self, com):
        print('{}: {}'.format(com, 'Variavel'))
        try:
            nome_var = com[1:]
            ret, msg = self.__exec_digitacao__(VAR[nome_var])
        except:
            print('Variavel invalida!')
            msg = 'A variável {} é inválida'.format(com)
            return False, msg
        return ret, msg

    def __cria_variaveis__(com):
        nome_var = com[1:]
        if nome_var not in VAR.keys():
            input = gui.inputDescricao(TITULO, 'Defina o valor da variável "{}":'.format(nome_var))
            if input != '' and input != None:
                VAR[nome_var] = input
                print('Variavel {}: {}'.format(nome_var, input))
            else:
                msg = 'Valor inválido da variável {}.'.format(nome_var)
                return False, msg
        return True, ''

    def __executar__(self, com):
        if len(com) == 1:
            ret, msg = self.__exec_tecla__(com)
        elif com[0] == '#':
            ret, msg = self.__exec_variavel__(self, com)
        elif com[0] == '>':
            ret, msg = self.__exec_timer__(com)    
        elif com[0] == '[':
            ret, msg = self.__exec_vetor__(com)
        elif com[0] == '{':
            ret, msg = self.__exec_click__(com)
        elif com[0] == '|':
            ret, msg = self.__exec_funcao__(com)
        elif self.__existeTecla__(com):
            ret, msg = self.__exec_tecla__(com)
        else:
            ret, msg = self.__exec_digitacao__(com)
        return ret, msg

    def executar(self, comandos, timer = 1):
        print(comandos)
        for com in comandos:
            if com[0] == '#':
                ret, msg = self.__cria_variaveis__(com)
                if ret == False:
                    return False, msg
        
        for com in comandos:
            ret, msg = self.__executar__(self, com)
            time.sleep(timer)
            if ret == False:
                return False, msg
        
        return True, ''

    def __existeTecla__(tecla):
        return tecla in pyautogui.KEYBOARD_KEYS

    def funcao_print():
        filename = 'Print'+datetime.now().strftime("%Y%m%d%H%M%S%f")+'.png'
        pyautogui.screenshot(filename)
        time.sleep(1)
        return filename

    def funcao_tab(n, timer):
        filename = 'Print'+datetime.now().strftime("%Y%m%d%H%M%S%f")+'.png'
        pyautogui.screenshot(filename)
        time.sleep(1)
        return filename

##################################### FIM FUNCOES DO AUTOMATIZADOR

def __lista_arquivos__(dir):
    caminhos = [os.path.join(dir, nome) for nome in os.listdir(dir)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    arquivos_csv = [arq for arq in arquivos if arq[-4:] == '.csv']

    dict_arquivos = {}
    for arq in arquivos_csv:
        caminho, nome = os.path.split(arq)
        dict_arquivos[nome] = arq

    return dict_arquivos

def __ler_config__():
    global DIR_COMANDOS
    global TIMER_PADRAO
    global DIR_OUTPUT

    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        DIR_COMANDOS = config.get('DEFAULT', 'DIR_COMANDOS')
        TIMER_PADRAO = float(config.get('DEFAULT', 'TIMER_PADRAO'))
        DIR_OUTPUT = config.get('DEFAULT', 'DIR_OUTPUT')

        print('DIR_COMANDOS: {}'.format(DIR_COMANDOS))
        print('TIMER_PADRAO: {}'.format(TIMER_PADRAO))
        print('DIR_OUTPUT: {}'.format(DIR_OUTPUT))

        return True
    except:
        return False

def main():
    global TITULO
    global DIR_COMANDOS
    global TIMER_PADRAO
    global DIR_OUTPUT

    arquivo_selecionado = ''

    if __ler_config__() != True:
        print('ERRO: Nao foi possivel ler o arquivo de configuracao!')
        gui.alerta(TITULO, 'ERRO: Não foi possível ler o arquivo de configuração! ')
    else:
        try:
            if len(DIR_COMANDOS) == 2:
                DIR_COMANDOS = os.path.dirname(os.path.realpath(__file__))
            
            if len(DIR_OUTPUT) == 2:
                DIR_OUTPUT = os.path.dirname(os.path.realpath(__file__)) + '\output'

            dict_arquivos = __lista_arquivos__(DIR_COMANDOS)
            opcoes = list(dict_arquivos.keys())
            if len(opcoes) > 1:
                resp = gui.inputOpcoes(TITULO, 'Foram encontrados mais de um arquivo de comandos.\nQual você deseja utilizar?', opcoes)
                if resp == 'Nenhuma' or resp == None:
                    return False
                arquivo_selecionado = dict_arquivos[resp]
            else:
                arquivo_selecionado = dict_arquivos[opcoes[0]]
        except:
            print('ERRO: Nao foram encontrados arquivos .csv no diretorio "{}"!'.format(DIR_COMANDOS))
            gui.alerta(TITULO, 'ERRO: Não foram encontrados arquivos .csv no diretório "{}"!'.format(DIR_COMANDOS))
            return False

        try:
            arquivo = pd.read_csv(arquivo_selecionado, sep=';', header=None, names=['comandos'])
            print('Foram encontrados {} comandos no arquivo {}.'.format(str(arquivo.shape[0]), arquivo_selecionado))

            comandos = arquivo['comandos'].astype('str')
            comandos = comandos.dropna()            
        except:
            print('ERRO: Nao foi possivel ler o arquivo "{}"!'.format(arquivo_selecionado))
            gui.alerta(TITULO, 'ERRO: Não foi possível ler o arquivo "{}"!'.format(arquivo_selecionado))  
            return False  
    
        input = gui.inputConfirmacao(TITULO, 'Deseja iniciar a automatização?\n(Você não poderá utilizar o mouse e o teclado durante a execução)')
        if input:
            automatizador.executar(automatizador, comandos.tolist(), TIMER_PADRAO)
            gui.alerta(TITULO, 'Automatização finalizado!')
        
        return True
        

if __name__ == "__main__":
    print('## INICIADA A EXECUÇÃO ##')
    main()
    print('## FINALIZADA A EXECUÇÃO ##')
