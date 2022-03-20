#Módulo Math Geral
import math #faça, import [CTRL+ESPAÇO]
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print(f'A raiz de {n} é {raiz:.3f}. ')



#Módulo Math Específico
from math import sqrt
n = int(input('Digite um número: '))
print(f'A raiz de {n} é {sqrt(n):.3f}. ')

#Módulo random
import random
num1 = random.random() 
print('Computador, me dê um número aleatório entre 0 e 1:',num1)

num2 = random.randint(1,100)
print('Computador, agora eu quero um número inteiro:',num2)
#pip list | Esse comando mostra todas as bibliotecas instaladas no pip. Caso a biblioteca emoji não esteja instalada, será necessário importa-la.
#Importando uma biblioteca da comunidade: Para importar uma biblioteca do pypi, necessita usar no terminal o comando(pip install "E o nome do pacote, sem as aspas")
#Caso o terminal não esteja identificando a biblioteca instalada, basta mudar o caminho do interprete (CTRL+SHIFT+P >>> Python Select interpreter >>> Enter interpreter path >>> C:\Python310\python.exe)
import sys
print(sys.executable)

import emoji
print(emoji.emojize('Python é legal :thumbsup:', language='alias'))