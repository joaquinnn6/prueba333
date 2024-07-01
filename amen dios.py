


opc = 0
while opc!=4:
    print('-----Menu eShirlitos-----')
    print('1.Registrar puntajes torneo')
    print('2.Listar los todos puntajes')
    print('3.Imprimir por Tipo')
    print('4.Salir del programa')
    try:
        opc=int(input('Igrese una opcion: '))
    except:print('Opcion invalida')
    while opc == 1:
        print('Ingresa tu ID de jugador')
        id_jg = str(input(': '))
        while len(id_jg)==0:
            print('Debe ingresar por lo menos 1 caracter')
            id_jg = str(input(': '))
        print('Ingresa Tu nombre real')
        nombre_real = str(input(': '))
        while len(nombre_real)< 3:
            print('Debe ingresar nombre y apellido')
            nombre_real = str(input(': '))
        print('Registra el puntaje de los juegos en los que compites')
        valorant = str(input('VALORANT: '))
        while len(valorant)==0:
            print('Debe ingresar por lo menos 1 numero')
            valorant = str(input(': '))    
        fort = str(input('FORTNITE: '))
        while len(fort)==0:
            print('Debe ingresar por lo menos 1 numero')
            fort = str(input(': '))
        fifa = str(input('FIFA: '))
        while len(fifa)==0:
            print('Debe ingresar por lo menos 1 numero')
            fifa = str(input(': '))
        print('Ingresa el tipo de jugador que eres(Principiante, Avanzado, Experto)')
        tipo_jg = str(input(': '))
        while len(tipo_jg)==0:
            print('Debe ingresar por lo menos 1 caracter')
            tipo_jg = str(input(': '))
        print('Puntaje registrado con exito!')
        break