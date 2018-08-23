#imprimir los numeros correspondientes a los dias de la semana


print "dime el dia de la semana que quieras y te dire a que numero corresponde \n"
print 'domingo'
print 'lunes'
print 'martes'
print 'miercoles'
print 'jueves'
print 'viernes'
print 'sabado'
print 'salir'
elijo = raw_input('elijo: ')

while elijo != 'salir':

    if elijo == 'domingo' :
        print 'domingo es el primer dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'lunes':
        print 'lunes es el segundo dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'martes':
        print 'martes es el tercer dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'miercoles':
        print 'miercoles es el cuarto dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'jueves':
        print 'jueves es el quinto dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'viernes':
        print 'viernes es el sexto dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')
        
    elif elijo == 'sabado':
        print 'sabado es el septimo dia de la semana'
        print 'si quiere salir, escriba salir, de lo contrario mencione otro dia'
        elijo = raw_input('elijo: ')

    elif elijo != 'domingo' or 'lunes' or 'martes' or 'miercoles' or 'jueves' or 'viernes' or 'sabado':
        print '''opcion incorrecta, si quiere continuar mencione un dia de la semana o
                   escriba salir para cerrar el programa'''
        elijo = raw_input('elijo: ')
