   

def eliminarCat(dic): #eliminar una categoria

    print ('*'*50)
    print ('ELIMINAR UNA CATEGORIA\n\n')
    print ('>Para volver escriba " atras "<\n\n')
    cat = input ('Escriba categoria a eliminar: ')

    while cat != 'atras':
        if cat in dic:
            del dic[cat]
            print ('La categoria ha sido eliminada exitosamente!')
        elif cat!= 'atras':
            print ('Error. Ingrese correctamente una categoria existente!')
        cat = input ('Escriba categoria a eliminar: ')
    return dic


def agregarCat(dic): #agregar una categoria

    print ('*'*50)
    print ('AGREGAR UNA CATEGORIA\n')
    print ('>Para volver escriba "atras"<\n\n')
    cat = input ('Escriba nueva categoria: ')

    while cat != 'atras':
        if cat in dic:
            print ('La categoria ya existe!')
        elif cat not in dic:
            dic2 = {cat:[]}
            dic.update(dic2)
            print ('La categoria ha sido agregada exitosamente!')
        cat = input ('Escriba nueva categoria: ')
    return dic
