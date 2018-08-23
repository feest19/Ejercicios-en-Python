print "Los dias de la semana!!!"
print"menciona un dia y te dire cual es el numero que le correcponde en la semana"
dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabados"]
elijo = raw_input ("elijo: ")

while elijo != "salir":

    if elijo == "domingo":
        print dias[0], "es el primer dias de la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "lunes":
        print dias[1], "es el segundo dias de la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "martes":
        print dias[2], "es el tercer dia de la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "miercoles":
        print dias[3], "es el cuarto dia de la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "jueves":
        print dias[4], "es el quinto dia de la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "viernes":
        print dias[5], "es el sexto dia de la semana... y el cuerpo lo sabe jejejeje"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo == "sabado":
        print dias[6], "es el septimo dia se la semana"
        print"si quiere continuar escriba un dia, de lo contrario escriba salir"
        elijo = raw_input("elijo: ")
    elif elijo != dias[0:6]:
        print"opcion incorrecta, mencione un dia o escriba salir si quiere salir"
        elijo = raw_input("elijo: ")
