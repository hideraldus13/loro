# Doc do LORO
LORO é um automatizador de tarefas super simples e assim deve ser seu sentimento ao usá-lo.
Siga os passos do [Fast Track](fast_track) para já sair usando e depois volte para a ver a [Lista de Comandos](lista_de_comandos) e incrementar suas rotinas. 

## Fast Track

- 1
- 2
- 3
- 4
- 5

## Criando / Editando comandos


## Lista de Comandos


| Comando | Exemplo | Observações |
| ------ | ------ | ------ |
| Tecla | `enter` | Qualquer comando correspondente a uma tecla do teclado (vide [Lista de Teclas](lista_de_teclas))|
| Variável | `_#nome` | |
| Timer | `_>1` | |
| Lista de Teclas | `_[win, up]` | |
| Clique | `_{50,50}` | |
| Função | `_|tab:12` | Funções pré programadas no LORO para facilitar ações (vide [Lista de Funções](lista_de_funcoes))|
| Texto | `teste123` | |

### Lista de Teclas
Abaixo a lista de teclas disponíveis para uso:
```
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

### Detalhes sobre o comando Clique

Ao executar `_{50,50}:R2` teremos a ação de dois cliques com o botão direito na posição dos pixels X=50 e Y=50.
Pois, o comando Clique em sua notação completa é composto por:
```
_{ + posição pixel X + , + posição pixel Y + } + : + R para botão Direito ou L para botão Esquerdo + número de cliques
```
Outros exemplos(testando na minha máquina, é claro :D):
_{1320,750}:L1 - Clica com o botão direito no relógio do Windows 
_{32,28}:R2 - Abre o primeiro ícone da área de trabalho

#### Como descobrir os pixels das posições

Ao executar o arquivo XX, a cada segundo, durante os 30 segundos seguintes, será registrada na tela do aplicativo a posição do mouse no momento. 
Mova-o até as posições que você deseja replicar para ter os valores corretos.

### Lista de Funções

| Função | Exemplo | Observações |
| ------ | ------ | ------ |
| Print | `_|print` | |
| Repetição de Tab | `_|tab:2` | |
| Repetição de Up | `_|up:2` | |
| Repetição de Down | `_|down:2` | |