# Exercício 1) Faça um código em Python

# Se a=2, atribua:
# potencia_ao_quadrado = a**2
# potencia_ao_cubo = a**3
# potencia_a_quarta = a**4
# Imprima o resultado das strings

print("Exercicio 1")
print("-----------")

a = 2
potencia_ao_quadrado = a**2
print(potencia_ao_quadrado)

potencia_ao_cubo = a**3
print(potencia_ao_cubo)

potencia_a_quarta = a**4
print(potencia_a_quarta)

print("#############################################################")

# ######################################################################################################################

from math import pow

# Exercício 2) Faça um código em Python

# Se x=512, atribua:
# raiz_quadrada_de_x =
# raiz_cúbica_de_x =
# raiz_quarta_de_x =
#  Imprima o resultado das strings

print("Exercicio 2")
print("-----------")

x = 512

raiz_quadrada_de_x = x**1/2
print(raiz_quadrada_de_x)

raiz_cubica_de_x = x**1/3
print(raiz_cubica_de_x)

raiz_a_quarta_de_x = x**1/4
print(raiz_a_quarta_de_x)

print("#############################################################")

# ######################################################################################################################

# Exercício 3) dado o valor de w anteriormente, import as funções floor, ceil da biblioteca math e
# determine o piso, o teto e o arredondamento.

print("Exercicio 3")
print("-----------")

w = 3345.61

from math import floor
from math import ceil

print(floor(w))
print(ceil(w))
print(round(w))

print("#############################################################")

# ######################################################################################################################

# Exercício 4) Porquenãoimportamosoround?Façauma pesquisanos sources “round não é
# função em python”. Vamos ver como usar o round (número[,ndigits]).
# w= 3345,61
# round (w,1)
# Explique a saída da função anterior, e se usássemos round(w,0)?

print("Exercicio 4")
print("-----------")

print(round(w,1))
print(round(w,0))

print("#############################################################")

# ######################################################################################################################

# Exercício 5) Arredonde os números a seguir, deixando ndigits = none

print("Exercicio 5")
print("-----------")

x1=1.456
x2=3.678
x3=7.5

print(round(x1,None))
print(round(x2,None))
print(round(x3,None))

print("#############################################################")

# ######################################################################################################################

# Exercício 6) Voltando ao caso do floor e ceil, por padrão estas funções retornam valores
# decimais,ou seja, com ponto flutuante. Podemos determinar que ambas funções resultem em
# uma saída com inteiro mantendo a mesma característica de piso e teto. Faça o teste com o
# comando a seguir:

print("Exercicio 6")
print("-----------")

print(int(floor(1.456)))

print("#############################################################")

# ######################################################################################################################

# Super Exercício 7) Resolva em Python a expressões a seguir:

print("ativ 1")
print("--------")

print(2**3)

print("-----------------------------------------------")

print("ativ 2")
print("--------")

print(-2**3)

print("-----------------------------------------------")

print("ativ 3")
print("--------")

print(1**0)

print("-----------------------------------------------")

print("ativ 4")
print("--------")

print(-1**0)

print("-----------------------------------------------")

print("ativ 5")
print("--------")

print(2**0)

print("-----------------------------------------------")

print("ativ 6")
print("--------")

print((2/5)**3)

print("-----------------------------------------------")

print("ativ 7")
print("--------")

print(3**-2)

print("-----------------------------------------------")

print("ativ 8")
print("--------")

print((1/2)**-3)

print("-----------------------------------------------")

print("ativ 9")
print("--------")

print((-1**3)**4)

print("-----------------------------------------------")

print("ativ 10")
print("--------")

print(0.5**3)

print("-----------------------------------------------")

print("ativ 11")
print("--------")

print(0.25**4)

print("-----------------------------------------------")

print("ativ 12")
print("--------")

print(0**4)

print("-----------------------------------------------")

print("ativ 13")
print("--------")

print(1+(0.41**2))

print("-----------------------------------------------")

print("ativ 14")
print("--------")

print((1/4)+(5**2)-(2**-4))

print("-----------------------------------------------")

print("ativ 15")
print("--------")

print((2**-3)+(-4**-5))

print("-----------------------------------------------")

print("ativ 16")
print("--------")

print((((4/5)-(1/2)+(1))**2)+((1/(1+(3**2)-(4-5)))**-2))

print("-----------------------------------------------")