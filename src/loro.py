import pip

def install(package):
    pip.main(['install', package])

try:
    import pyautogui
except ModuleNotFoundError:
    install("pyautogui")
    import pyautogui

try:
    import time
except ModuleNotFoundError:
    install("time")
    import time

try:
    import pandas as pd
except ModuleNotFoundError:
    install("pandas")
    install("openpyxl")
    install("xlrd")
    import pandas as pd

import os, csv 
from datetime import datetime
import configparser

import gui as gui

class Instrucao:
    '''
    Classe de instrucao

    Tipos de instrucao:
    0 = não identificado
    1 = tecla
    2 = variável
    3 = timer
    4 = lista
    5 = click
    6 = funcao //desabilitado
    7 = digitacao
    '''

    DESCRICAO_TIPO = ['Não identificado', 'Tecla', 'Variável', 'Timer', 'Lista', 'Click', 'Funcao', 'Tecla', 'Digitacao']

    def __init__(self, lista_comandos):
        com, tipo = self.__validacoes__(lista_comandos)
        self.comando = com
        self.tipo_comando = tipo
        self.aux = None

    def __validacoes__(self, com):
        if len(com) == 1:
            return com, 1

        elif com[0] == '#':
            return com[1:], 2

        elif com[0] == '>':
            return float(com[1:]), 3   

        elif com[0] == '[':
            com = com.replace('[','').replace(']','').replace(' ','')
            lista = com.split(',')
            return lista, 4

        elif com[0] == '{':
            com = com.replace('{','').replace('}','').replace(' ','')
            lista = com.split(',')
            return lista, 5

        elif com[0] == '|':
            pass

        elif self.__existeTecla__(com):
            return com, 1

        else:
            return com, 7

        return com, 0

    def get_tipo(self):
        return self.tipo_comando
    
    def get_instrucao(self):
        return self.comando

    def set_aux(self, aux):
        self.aux = aux

    def __existeTecla__(self, tecla):
        return tecla in pyautogui.KEYBOARD_KEYS

    def __str__(self):
        txt = 'Instrucao: '+self.DESCRICAO_TIPO[self.tipo_comando]+' - '+str(self.comando)
        if self.aux != None:
            txt += ' - ' + self.aux
        return txt

    def executar(self):
        print(self)
        if self.tipo_comando == 1:
            self.__exec_tecla__()
        elif self.tipo_comando == 2:
            self.__exec_variavel__()
        elif self.tipo_comando == 3:
            self.__exec_timer__()
        elif self.tipo_comando == 4:
            self.__exec_lista__()
        elif self.tipo_comando == 5:
            self.__exec_click__()
        elif self.tipo_comando == 6:
            pass
        elif self.tipo_comando == 7:
            self.__exec_digitacao__()

    def __exec_tecla__(self):
        try:
            pyautogui.press(self.comando)
        except:
            raise Exception('Tecla invalida!')
            
    def __exec_variavel__(self):
        try:
            pyautogui.typewrite(self.aux, 0.0001)
        except:
            raise Exception('Variavel invalida!')

    def __exec_timer__(self):
        try:
            time.sleep(float(self.comando))
        except:
            raise Exception('Timer invalido!')

    def __exec_lista__(self):
        lista = self.comando
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
            raise Exception('Lista de comandos invalido!')

    def __exec_click__(self):
        lista = self.comando
        try:
            if len(lista) == 2:
                x= int(lista[0])
                y= int(lista[1])
                pyautogui.click(x=x, y=y)
        except:
            raise Exception('A lista de posições {} é inválida')
    
    def __exec_digitacao__(self):
        try:
            pyautogui.typewrite(self.comando, 0.0001)
        except:
            raise Exception('Texto invalido!')


class Config():
    def __init__(self):
        self.titulo = 'LORO v0.1'
        self.dir_comandos = ''
        self.timer_padrao = 1
        self.dir_output = ''
    
    def get_titulo(self):
        return self.titulo
    
    def get_dir_comandos(self):
        return self.dir_comandos
    
    def get_timer_padrao(self):
        return self.timer_padrao
    
    def get_dir_output(self):
        return self.dir_output

    def ler_config(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.dir_comandos = config.get('DEFAULT', 'DIR_COMANDOS')
            self.timer_padrao = float(config.get('DEFAULT', 'TIMER_PADRAO'))
            self.dir_output = config.get('DEFAULT', 'DIR_OUTPUT')
        except:
            gui.alerta(self.titulo, 'ERRO: Não foi possível ler o arquivo de configuração! ')
            raise Exception('Não foi possível ler o arquivo de configuração!')


def __lista_arquivos__(dir):
    caminhos = [os.path.join(dir, nome) for nome in os.listdir(dir)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    arquivos_csv = [arq for arq in arquivos if arq[-4:] == '.csv']

    dict_arquivos = {}
    for arq in arquivos_csv:
        caminho, nome = os.path.split(arq)
        dict_arquivos[nome] = arq

    return dict_arquivos

def __executa_instrucoes__(lista, timer, titulo):
    instrucoes = []
    for inst in lista:
        x = Instrucao(inst)
        if x.get_tipo() == 2:
            x.set_aux(gui.inputDescricao(titulo, 'Defina o valor da variável "{}":'.format(x.get_instrucao())))
        instrucoes.append(x)
    
    for i in instrucoes:
        i.executar()
        time.sleep(timer)


def main():
    config = Config()
    config.ler_config()
    
    titulo = config.get_titulo()
    dir_comandos = config.get_dir_comandos()
    timer = config.get_timer_padrao()
    dir_output = config.get_dir_output()

    arquivo_selecionado = ''

    try:
        if len(dir_comandos) == 2:
            dir_output = os.path.dirname(os.path.realpath(__file__))
        
        if len(dir_output) == 2:
            dir_output = os.path.dirname(os.path.realpath(__file__)) + '\output'

        dict_arquivos = __lista_arquivos__(dir_comandos)
        opcoes = list(dict_arquivos.keys())
        if len(opcoes) > 1:
            resp = gui.inputOpcoes(titulo, 'Foram encontrados mais de um arquivo de comandos.\nQual você deseja utilizar?', opcoes)
            if resp == 'Nenhuma' or resp == None:
                raise Exception('Nenhuma opção selecionada')
            arquivo_selecionado = dict_arquivos[resp]
        else:
            arquivo_selecionado = dict_arquivos[opcoes[0]]
    except:
        gui.alerta(titulo, 'ERRO: Não foram encontrados arquivos .csv no diretório "{}"!'.format(dir_comandos))
        raise Exception('ERRO: Nao foram encontrados arquivos .csv no diretorio "{}"!'.format(dir_comandos))

    try:
        arquivo = pd.read_csv(arquivo_selecionado, sep=';', header=None, names=['comandos'])
        print('Foram encontrados {} comandos no arquivo {}.'.format(str(arquivo.shape[0]), arquivo_selecionado))

        comandos = arquivo['comandos'].astype('str')
        comandos = comandos.dropna()            
    except:
        gui.alerta(titulo, 'ERRO: Não foi possível ler o arquivo "{}"!'.format(arquivo_selecionado))  
        raise Exception('ERRO: Nao foi possivel ler o arquivo "{}"!'.format(arquivo_selecionado))

    input = gui.inputConfirmacao(titulo, 'Deseja iniciar a automatização?\n(Você não poderá utilizar o mouse e o teclado durante a execução)')
    if input:
        __executa_instrucoes__(comandos.tolist(), timer, titulo)
        gui.alerta(titulo, 'Automatização finalizado!')
    
    return True

if __name__ == "__main__":
    print('## INICIADA A EXECUÇÃO ##')
    main()
    print('## FINALIZADA A EXECUÇÃO ##')
