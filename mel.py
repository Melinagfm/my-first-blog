print('Hello django girls')
if 3 > 2:
    print('Funciona')




idade = input('qual a sua idade?\n')
if int(idade) > 18:
    print('pode entrar')
else:
    print('saia caba safadhu')



def minha_funcao(a, b):
    resultado = (a + b) * (b ** b)
    print(resultado)

a = input('Qual o valor de a?\n')
b = input('Qual o valor de b?\n')

minha_funcao(int(a), int(b))

def hi(name):
    if name == 'Ola':
        print('Olá Ola!')
    elif name == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

name = input('Qual seu nome?')
hi(name)

def teste1():
    nome = input('Qual o seu nome?\n')
    print("Oi, "+ nome)
teste1()

def teste2(nome):
    if  nome == 'mel': 
        print("oi, linda")
    else:
        print("Oi, " + nome)

teste2()

    