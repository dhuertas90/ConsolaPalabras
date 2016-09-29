import archivo
import Mod_categoria
import Mod_funciones
import Mod_altabaja


def main():

    try:
        dic = archivo.desarchivar('abm.txt')
    except IOError:
        f = open('abm.txt', 'wb')
        f.close()
        dic = {}
    
    nuedic = {}
    opc = ''
    txt = '*'*50
    txt += '\n                    BIENVENIDO\n\n'
    txt += '    \bMenu principal:\b\n\n'
    txt += '  0- Devolver una palabra\n\n'
    txt += '  1- Agregar palabras\n\n'
    txt += '  2- Eliminar palabras\n\n'
    txt += '  3- Modificar palabras\n\n'
    txt += '  4- Mostrar categorias\n\n'
    txt += '  5- Agregar categorias\n\n'
    txt += '  6- Eliminar categorias\n\n'
    txt += '  7- Modificar categorias\n\n'
    txt += '  8- Salir\n\n'
    print (txt)
    opc = input ('Ingrese opcion: ')
    
    while opc != '8':

        if opc == '0':
               Mod_categoria.mostrarCat(dic,'dev')
               print (txt)
        elif opc == '1':
               nuedic = Mod_funciones.cargar(dic)
               print (txt)
        elif opc == '2':
               nuedic = Mod_funciones.eliminar(dic)
               print (txt)
        elif opc == '3':
               nuedic = Mod_funciones.modificar(dic,'pal')
               print (txt)
        elif opc == '4':
               Mod_categoria.mostrarCat(dic,'most')
               print (txt)
        elif opc == '5':
               nuedic = Mod_altabaja.agregarCat(dic)
               print (txt)
        elif opc == '6':
               nuedic = Mod_altabaja.eliminarCat(dic)
               print (txt)
        elif opc == '7':
               nuedic = Mod_funciones.modificar(dic,'categ')
               print (txt)
        elif opc != '8' and opc not in ('0','1','2','3','4','5','6','7'):
               print ('Error. Opcion no valida!')
        archivo.archivar(nuedic,'abm.txt')
        opc = input ('Ingrese opcion: ')
    print ('Adios!!')
    print ('*'*50)


main()
