import pip

try:
    import pyautogui
except ModuleNotFoundError:
    install("pyautogui")
    import pyautogui

#class gui():
def __init__(self) -> None:
    pass

def inputConfirmacao(titulo, msg):
    resp = 'Não'
    resp = pyautogui.confirm(text=msg, title=titulo, buttons=['Sim', 'Não'])
    
    if resp == 'Sim':
        return True
    else: 
        return False

def inputDescricao(titulo, msg, msg_padrao = ''):
    resp = pyautogui.prompt(text=msg, title=titulo , default=msg_padrao)
    return resp

def inputOpcoes(titulo, msg, opcoes):
    resp = 'Nenhuma'
    resp = pyautogui.confirm(text=msg, title=titulo, buttons=opcoes)
    return resp

def alerta(titulo, msg):
    pyautogui.confirm(text=msg, title=titulo, buttons=['OK'])  