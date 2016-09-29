import random

def imprimir(lista):
    for i in lista:
        print (i)
        
def mostrarCat(dic,opc):

    print ('*'*50) #separador de menues
    print ('MOSTRAR:\n')
        
    print('\n- Para regresar al Menu principal escriba "atras"\n')
    
    cat = input('Escriba categoria: ')
        
    while cat != 'atras':
        if opc == 'dev' and (cat in dic):
            if len(dic[cat]) > 0:
                print ('\b\b-'+random.choice(dic[cat])+'\n')
            else:
                print ('No existe palabras en esta categoria!\n')
        elif cat != 'atras' and (cat in dic):
             print('\n\b\bLista de palabras:')
             imprimir(dic[cat])
             if (len(dic[cat]) == 0):
                 print ('No hay palabras cargadas!\n')
             print ('\b\bFin de lista\n')
        elif cat == 'atras':
            break
        else:
            print ('Error. Ingrese correctamente una categoria existente!')
        cat = input('Escriba categoria: ')
