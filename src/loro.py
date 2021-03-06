import sys
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

import os, re
from datetime import datetime
import configparser

import gui as gui
import ascii_art as art

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
    6 = funcao 
    7 = digitacao
    '''

    DESCRICAO_TIPO = ['Não identificado', 'Tecla', 'Variável', 'Timer', 'Lista', 'Click', 'Funcao', 'Digitacao']

    def __init__(self, lista_comandos, config = None):
        com, tipo, aux = self.__validacoes__(lista_comandos)
        self.comando = com
        self.tipo_comando = tipo
        self.aux = aux
        self.config = config
    
    def __validacoes__(self, com):
        #tecla
        if len(com) == 1:
            return com, 1, None

        #variavel
        elif re.fullmatch(r'_#\w+', com) != None:
            return com[2:], 2, None

        #timer
        elif re.fullmatch(r'_>\d+(.\d+)?', com) != None:
            return float(com[2:]), 3, None

        #lista
        elif re.match(r'_\[.+', com) != None:
            aux = com.replace(' ','')
            if re.fullmatch(r'_\[\w+,\w+(,\w+)?\]', aux) != None:
                aux = aux.replace('_[','').replace(']','')
                lista = aux.split(',')
                for i in lista:
                    if self.__existeTecla__(i) == False:
                        return com, 7, None
                return lista, 4, None

            return com, 7, None

        #click
        elif re.fullmatch(r'_{\d+,\d+}', com) != None or  re.fullmatch(r'_{\d+,\d+}:\w\d', com) != None:
            aux = None
            if re.fullmatch(r'_{\d+,\d+}:\w\d', com) != None:
                aux = [com[-2], int(com[-1])]
                com = com[:-3]
            com = com.replace('_{','').replace('}','').replace(' ','')
            lista = com.split(',')
            return lista, 5, aux

        #funcao
        elif re.fullmatch(r'_\|\w+(:\d+)?', com) != None:
            if re.fullmatch(r'_\|(tab):\d+', com) != None:
                pos = com.rfind(':')
                aux = int(com[pos+1:])
                com = com[:pos]
                return com[2:], 6, aux
            elif re.fullmatch(r'_\|(down):\d+', com) != None:
                pos = com.rfind(':')
                aux = int(com[pos+1:])
                com = com[:pos]
                return com[2:], 6, aux
            elif re.fullmatch(r'_\|(up):\d+', com) != None:
                pos = com.rfind(':')
                aux = int(com[pos+1:])
                com = com[:pos]
                return com[2:], 6, aux
            elif re.fullmatch(r'_\|print', com) != None:
                return com[2:], 6, None
            
            return com, 7, None

        #tecla
        elif self.__existeTecla__(com):
            return com, 1, None

        #digitacao
        else:
            return com, 7, None

    def get_tipo(self):
        return self.tipo_comando
    
    def get_instrucao(self):
        return self.comando

    def set_aux(self, aux):
        self.aux = aux

    def __existeTecla__(self, tecla):
        return tecla in pyautogui.KEYBOARD_KEYS

    def __str__(self):
        txt = 'Instrucao: '+self.DESCRICAO_TIPO[self.tipo_comando]+' ('+str(self.tipo_comando)+') - '+str(self.comando)
        if self.aux != None:
            txt += ' - ' + str(self.aux)
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
            self.__exec_funcao__()
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
            else:
                pyautogui.hotkey(lista[0], lista[1], lista[2])
        except:
            raise Exception('Lista de comandos invalido!')

    def __exec_click__(self):
        lista = self.comando
        aux = self.aux
        try:
            x= int(lista[0])
            y= int(lista[1])
            if aux != None:
                if aux[0] == 'L':
                    button='left'
                else: 
                    button='right'
                pyautogui.click(x=x, y=y, button=button, clicks=aux[1], interval=0.25)
            else:
                pyautogui.click(x=x, y=y)

        except:
            raise Exception('A lista de posições {} é inválida')
    
    def __exec_funcao__(self):
        try:
            if self.comando == 'tab':
                for i in range(self.aux):
                    pyautogui.press('tab')
                    time.sleep(self.config.get_timer_padrao())
            elif self.comando == 'down':
                for i in range(self.aux):
                    pyautogui.press('down')
                    time.sleep(self.config.get_timer_padrao())
            elif self.comando == 'up':
                for i in range(self.aux):
                    pyautogui.press('up')
                    time.sleep(self.config.get_timer_padrao())
            elif self.comando == 'print':
                file_name = str(datetime.now()).replace(':','').replace('.','').replace(' ','').replace('-','')+'_print.png'

                pyautogui.screenshot(self.config.get_dir_output()+file_name)
            else:
                raise Exception('Funcao invalida!')
        except:
            raise Exception('Erro na execucao da funcao!')
           

    def __exec_digitacao__(self):
        try:
            pyautogui.typewrite(self.comando, 0.0001)
        except:
            raise Exception('Texto invalido!')


class Config():
    def __init__(self):
        self.titulo = 'LORO v0.2'
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

def __executa_instrucoes__(lista, config):
    instrucoes = []
    for inst in lista:
        x = Instrucao(inst, config)
        if x.get_tipo() == 2:
            x.set_aux(gui.inputDescricao(config.get_titulo(), 'Defina o valor da variável "{}":'.format(x.get_instrucao())))
        instrucoes.append(x)
    
    for i in instrucoes:
        i.executar()
        time.sleep(config.get_timer_padrao())

def main():
    config = Config()
    config.ler_config()
    
    titulo = config.get_titulo()
    dir_comandos = config.get_dir_comandos()
    timer = config.get_timer_padrao()
    dir_output = config.get_dir_output()

    arquivo_selecionado = ''

    if len(sys.argv) > 1:
        arquivo_selecionado = sys.argv[1]
    else:
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
        __executa_instrucoes__(comandos.tolist(), config)
        gui.alerta(titulo, 'Automatização finalizado!')
    
    return True

if __name__ == "__main__":
    print(art.parrot())
    print('LORO - O automatizador super simples para tarefas repetitivas!')
    print('+ informações em https://github.com/hideraldus13/loro')
    print('')
    print('> Execução iniciada')
    main()
    print('> Execução finalizada')
