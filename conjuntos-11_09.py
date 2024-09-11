user_Thor = {'mysql','CPU','RAM','SSD1','Google'}
user_Thanos = {'LoL','RAM','CPU','HD','Google'}
user_CA = {'mysql','LOL','RAM','CPU','Firefox'}
user_TS = {'mysql','CPU','RAM','SSD1','Google'}

#####################################################################################################################################

# conjunto_processador = {'CPU','Registrador','Core'}
# print(conjunto_processador)
# print(type(conjunto_processador))
# conjunto_processador.add('Cache')
# print(conjunto_processador)
# conjunto_processador.remove('Cache')
# print(conjunto_processador)
# conjunto_processador.discard('Registrador')
# print(conjunto_processador)
# conjunto_processador.clear()
# print(conjunto_processador)
# del conjunto_processador
# # print(conjunto_processador)

#####################################################################################################################################

# conjunto_processador = set(['CPU','Registrador','Core'])
# print(conjunto_processador)
# print(type(conjunto_processador))

# lista_processador = {'CPU','Registrador','Core','CPU'}
# conjunto_processador2 = set (lista_processador)
# print(conjunto_processador2)

#####################################################################################################################################

# inventario1 = user_Thor | user_CA
# print(inventario1)

# inventario2 = user_Thor | user_CA | user_Thanos | user_TS
# print(inventario2)

# inventario3 = user_Thor.union(user_CA)
# print(inventario3)

#####################################################################################################################################

# inventario1 = user_Thor.union(user_CA, user_Thanos, user_TS)
# print(inventario1)

#####################################################################################################################################

# inventario1 = user_Thor & user_CA
# print(inventario1)

# inventario2 = user_Thor.intersection(user_Thanos)
# print(inventario2)

#####################################################################################################################################

# inventario1 = user_Thor & user_CA & user_TS & user_Thanos
# print(inventario1)

# inventario2 = user_Thor.intersection(user_Thanos, user_CA, user_TS)
# print(inventario2)

#####################################################################################################################################

# inventario = user_TS - user_Thor - user_CA - user_Thanos
# print(inventario)

#####################################################################################################################################

# print('CPU' in user_TS)
# print('Firefox' in user_Thanos)

# print('LoL' not in user_Thor)
# print('LoL' not in user_Thanos)

#####################################################################################################################################

# print('LoL' not in user_Thanos & user_Thor & user_CA & user_TS)

#####################################################################################################################################

# print(user_Thor.issubset(user_Thanos))
# print(user_Thor.issubset(user_TS))
# print(user_Thor <= user_TS)
# print(user_TS.issuperset(user_Thor))
# print(user_TS >= (user_Thor))

#####################################################################################################################################

# print(user_TS == user_Thor)
# print(user_TS != user_Thor)
# print(user_TS == user_CA)
# print(user_TS != user_CA)

#####################################################################################################################################

print(user_TS.issuperset(user_Thor & user_CA & user_Thanos))
print(user_TS.issubset(user_Thor & user_CA & user_Thanos))