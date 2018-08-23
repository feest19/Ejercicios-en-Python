#calculadora en python

print "elija operacion: "

print "a) suma"
print "b) resta"
print "c) multiplicasion"
print "d) divicion"
print "e) Salir"
print "f) exponente"
print 'g) Historico'
Historico = []
opcion = raw_input('opcion: ')
while opcion != 'e':
    if opcion == 'a':
        CAMPO1 = int(raw_input("primer numero: "))
        CAMPO2 = int(raw_input("segundo numero: "))
        print CAMPO1 + CAMPO2
        Historico.append(str(CAMPO1) + ' + ' + str(CAMPO2) + ' = ' + str(CAMPO1 + CAMPO2))
    elif opcion == 'b':
        CAMPO1 = int(raw_input('primer numero: '))
        CAMPO2 = int(raw_input('Segundo Numero: '))
        print CAMPO1 - CAMPO2
        Historico.append(str(CAMPO1) + ' - ' + str(CAMPO2) + ' = ' + str(CAMPO1 - CAMPO2))

    elif opcion == 'd':
        CAMPO1 = int(raw_input('primer numero: '))
        CAMPO2 = int(raw_input('Segundo Numero: '))
        if CAMPO2 == 0:
            print "No se puede dividir entre CERO"
        else:
            print CAMPO1 / CAMPO2
            Historico.append(str(CAMPO1) + ' / ' + str(CAMPO2) + ' = ' + str(CAMPO1 / CAMPO2))
    
    elif opcion == 'c':
         CAMPO1 = int(raw_input('primer numero: '))
         CAMPO2 = int(raw_input('Segundo Numero: '))
         print CAMPO1 * CAMPO2
         Historico.append(str(CAMPO1) + ' * ' + str(CAMPO2) + ' = ' + str(CAMPO1 * CAMPO2))

    elif opcion == 'f':
        CAMPO1 = int(raw_input('primer numero: '))
        CAMPO2 = int(raw_input('segundo numero" '))
        print CAMPO1 ** CAMPO2
        Historico.append(str(CAMPO1) + ' ^ ' + str(CAMPO2) + ' = ' + str(CAMPO1 ** CAMPO2))
    
    elif opcion == 'g':
        for h in Historico:
            print h
    else:
        print 'opcion incorrecta'
        
    print "elija operacion: "

    print "a) suma"
    print "b) resta"
    print "c) multiplicasion"
    print "d) divicion"
    print "e) Salir"
    print 'f) exponente'
    print 'g) Historico'
    opcion = raw_input('opcion: ')
