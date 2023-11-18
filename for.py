 
 
 
 
 
# laço de repetição : comando for, o comando para 
# in , dentro . 
# range , faixa .
"""
for variavel in range(10):
  print(variavel)
  
 # eu to pedindo para(for) variaver ir até dento(in) da faixa(ranger) (10) 
  
  # pode se passar até 3 parametros para o for ( 1),(12),(3)
  #nesse codigo ele pula de 3 em 3 até 12 
  
  nota1 = float(input('digite a nora 1 '))
  nota2 = float(input('digite a nora 2 '))
  nota3 = float(input('digite a nora 3 '))
  """ 
  
  # o F {} string vc coloca uma variavel dentro da strigo , colocando um f no começo antes da variavel, e chaves " {}" no final relacionando a variavel desejada
  
  
soma= 0
  

for  i  in range(1 ,4 ):
    
 nota = float(input(  f'informe a sua nota {i}: ')) 
  
 soma = soma + nota  
  #variavel acumuladora , ela pega um valor e acumula 


 print(soma/3)