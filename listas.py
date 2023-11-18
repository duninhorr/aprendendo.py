

# listas 


#antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com listas 

notas = [ 7.9, 9.7, 8.2]

# criando listas 

lista = [ ] # lista vazia 

lista =list()
lista =[26,'luis ',3.5565, False]
lista_de_listas = [10, [1,2,3]]

# o comando "list" cria uma lista vazia. 




# indexação de slices ( fatiamento)

lista = [ 10 ,'luis', 23.5454, True]



# slices 

#serve pra acessar o indice de cada elemento 
#da lista , e começa sempre do indice 0. 
print( lista [0])
print( lista [1])
print( lista [2])
print( lista [3])

#  ou seja, uma lista com 4 elementos , tem 4 indices, porem parte do 0 , 1 ,2  e 3. 


lista=[10,20,30,40,50,60]

print(lista [0:3]) # percorrer do indice 0 até o indice 3 
print( lista [3:6]) # percorrer do 3 ao 6
print(lista[3:]) #  percorrer do 3 
print (lista[2:6:2]) # percorrer do 2 até o 6 , de 2 em 2 


# alteraçoes com fo 

#  2 utilizando os proprios elementos da lista

for elemento in lista :
    
    print(elemento)
# ele imprime todos os elementos da lista 

# utilizando  os indices 


#  ele mosta o comprimento da lista com o  comando "len".
print('comprimento da lista', len (lista))
# o comando "len" ler a quantidade de posiçoes da lista .



# ele vai no indice e ler indice por indice da lista 
for i in range(len(lista)):
    print(lista[i])
