salir = " "

while salir != "s":

	numero = int(raw_input('primero escriba la cantidad o (s) si decea salir: '))
	grado = str(raw_input('seleccione f para convertir a fahrenheit o c para celcius: '))
	
	if grado == "c":
		resultado = (numero - 32) * 5/9
		print resultado
        print'si quiere salir precione (y) de lo contrario digite otro numero:'
        numero = raw_input('primero escriba la cantidad o (s) si decea salir:' )
        grado = raw_input('seleccione f para convertir a fahrenheit o c para celcius:' )
    elif grado == "f":
		resultado = (numero * 9/5) + 32
        print resultado
        print'si quiere salir precione (s) de lo contrario digite otro numero:'
        numero = raw_input('primero escriba la cantidad o (s) si decea salir:' )
        grado = raw_input('seleccione f para convertir a fahrenheit o c para celcius:' )


 
