#No código abaixo primeiramente importamos a biblioteca Numpy usando ~as~ para enomear a biblioteca como ~np~:
import numpy as np 


#Definimos um contador que serve como referêncial para mostrar as linhas da matriz:
c=0


#Definimos nossa Matriz com  M(2x3) para Mij sendo i(linhas) e j(colunas):
M=np.array([(3,2,1),(1,2,3)])


#Construímos um laço que para cada linha na matriz M seja dado print na mesma com uma legenda intuindo a posição dos seus elementos:
for i in M:
    c+=1
    print(f'{i} {c}º linha(a{c}xj)')

