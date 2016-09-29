import archivo


def deletePal(lista):
    #eliminar y retornar lista actualizada
    pal = input('Escriba palabra a eliminar: ')
    if pal in lista:
        lista.remove(pal)
        print ('La palabra ha sido eliminada exitosamente!')
    else:
        print('La palabra ingresada no existe!')
    return lista

def modpal(lista, cat):
    #modificar palabra
    pal = input('Escriba palabra que desea modificar: ')
    if pal in lista:
        lista.remove(pal)
        nue = input('Escriba nueva palabra: ')
        lista.append(nue)
        lista.sort()
        print ('La operacion se ha realizado exitosamente!')
    elif pal != 'atras':
        print('La palabra ingresada no existe!')
    return lista

def modcateg(dic, cat):
    #modificar categoria
    nuecateg = input('Escriba nueva categoria: ')
    if nuecateg not in dic:
        lista = dic[cat]
        del dic[cat]
        dic[nuecateg] = lista
        print ('La operacion se ha realizado exitosamente!')
    else:
        print('Error. Debio ingresar categoria no existente.')
    return dic


def modificar(dic, x):
    #modificar palabra o categoria
    claves = dic.keys()

    print ('*'*50)
    print('\nMODIFICAR: \n')

    print ('- Para regresar al Menu principal escriba "atras"\n')

    cat = input ('Escriba categoria: ')

    while cat != 'atras':
        if cat in dic:
            if x == 'pal':
                lista = modpal(dic[cat],cat)
                dic[cat] = lista
            else:
                dic = modcateg(dic,cat)
        elif cat != 'atras':
            print ('Error. No existe esa categoria.')
        cat = input('Escriba categoria: ')
    return dic


def eliminar(dic):
    #eliminar palabra
    
    claves = dic.keys()

    print ('*'*50)
    print ('\nELIMINAR PALABRAS:\n')
    print ('- Para regresar al Menu principal escriba "atras"\n')
    
    cat = input('Escriba categoria: ')

    while cat != 'atras':
        if cat in dic:
            lista = deletePal(dic[cat])
            dic[cat] = lista
        elif cat != 'atras':
            print ('Error. No existe esa categoria.')
        cat = input('Escriba categoria: ')

    return dic
            
    

def insertar(cat, dic):
    #insetar nueva palabra
    pal = input('Escriba nueva palabra: ')

    while pal != 'atras':
        lista = dic[cat]
        if pal in lista:
            print ('La palabra ya existe!')
        elif pal != 'atras':
            lista.append(pal)
            lista.sort()
            dic[cat] = lista

        pal = input('Escriba nueva palabra: ')
    return dic



def cargar(dic): #SUBMENU PARA CARGAR UNA PALABRA
    
    claves = dic.keys()

    print ('*'*50)
    print ('AGREGAR PALABRAS\n\n')
    print ('\n- Para regresar al Menu principal escriba "atras"\n')
    
    cat = input ('Escriba categoria: ')

    while cat != 'atras':
        if  cat in claves:
            nuedic = insertar(cat, dic)
            print ('La/s operacion/es se realizo/aron exitosamente!')
            return nuedic

        elif cat != 'atras':
            print('Error. La categoria ingresada no existe')
            cat = input('Escriba categoria: ')
    return dic
