

# estruturas condicionais 


idade = 20 

if idade >= 18:
    # if é uma codição de : " se " , ou seja comparativa . 
 print ( ' voce é maior de idade')
else:
    print ( ' vc é menor de idade ') 
  # else é a condição de: " senão " , ela toma uma decisão caso nao antenda a condição . 
     
""" 
iamagine que você queira imprimir " aprovado(o)" , caso o estudante tenha uma meidia superior a 7 , e " reprovada(o)",caso a media seja inferior a 7 
"""  

media = float(input('infome a media do estudante:'))
              
if media >= 7: #se 
    print('aprovado ')
elif  media >= 5:      #se senão
 print( 'recuperação')   
else:  # senao
    print('reprovado')
    
    
    
    # AND  ou OR = "e"  ou  "outra"
    
    media = 10 
    presenca = 100
    
    if media >= 7 and presenca >= 70 :
        print (' aprovado ')
    else:
        print(' reprovado')
    