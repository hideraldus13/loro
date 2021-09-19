# :parrot: Documentação do Loro

* [Onde configuro os comandos?](#onde-configuro-os-comandos-)
  * [Comandos disponíveis](#comandos-disponíveis)
    + [Tecla](#tecla)
    + [Clique](#clique)
    + [Pausa](#pausa)
    + [Lista de teclas disponíveis:](#lista-de-teclas-disponíveis-)
  * [Configurações avançadas](#configurações-avançadas)
## Onde configuro os comandos?
O arquivo com os comandos para o Loro deve possuir as seguintes características:
- deve estar no diretório <i>comandos</i> (ver [Configurações avançadas](#configurações-avançadas))
- deve possuir a extensão .csv
- deve possuir apenas uma coluna, sem cabeçalho
- os comandos devem estar organizados por linha, em ordem de execução crescente
- os comandos não necessitam de aspas simples ou duplas
- os espaços em branco serão considerados como parte do comando

> Verifique no diretório <i>comandos</i> os modelos já disponíveis.

## Comandos disponíveis
### Tecla
#### Definição:
- Comando similar ao pressionar uma tecla do teclado
#### Regras:
- Qualquer caracter será considerado uma tecla. <i>Ex: a (pressionar a tecla 'a')</i>
- Qualquer palavra que corresponda a uma tecla, será considerada uma tecla <i>(ver [Lista de teclas disponíveis](#lista-de-teclas-disponíveis))</i>
#### Exemplo de uso:
- No Chrome, para acessar rapidamente a barra de navegação, basta teclar o F6
```
f6
www.google.com.br
enter
```
### Clique

#### Definição:
- 
#### Regras:
-
#### Exemplo de uso:
-
### Pausa
#### Definição:
- Comando de breve interrupção na sequência de execução, realizando uma pausa de tempo entre o último e o próximo comando. 
#### Regras:
- Deve-se iniciar com _> seguido pelo valor em segunda referente a pausa. <i>Ex: _>3 (pausa de 3 segundos)</i>
- Pode-se inserir um valor decimal. Sendo o separador decimal o '.'. <i>Ex: _>0.5 (pausa de meio segundo)</i>
#### Exemplo de uso:
- Ao abrir um aplicativo é interessante aguardar até o mesmo estar apto ao uso
```
_[win,r]
chrome
enter
_>3
```
### Lista de teclas disponíveis: 
>'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright'

## Configurações avançadas
-