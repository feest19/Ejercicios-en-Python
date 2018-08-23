#mayor y nemor

campo1 = raw_input('primer numero: ')
campo2 = raw_input('segundo numero: ')
salir = str(raw_input('y'))
if campo1 < campo2:
    print ("el menor es" ,campo1)

elif campo1 > campo2:
    print ('el mayor es' ,campo1)

elif campo1 == campo2:
    print 'ambos son iguales'
    
    print 'desea salir?'     

elif salir == 'y':
           exit()
        
        
    

