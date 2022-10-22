opc=100
print("0.Salir")
print("1.Agregar ciclista")
print("2.Ver mejor tiempo")
print("3.Ver todos los tiempos")

ciclistas=[]

while(opc!=0):
    ciclista={}

    opc=int(input("Ingrese una opción"))
    if(opc==1):
        ciclista ['Nombre']=input("Digite un Nombre: ")
        ciclista ['Edad'] = int(input("Digite el Edad: "))
        ciclista ['País']=input("Digite el país: ")
        ciclista ['Equipo']=input("Digite el equipo: ")
        ciclista ['tiempo']=int(input("Digite el tiempo en minutos: "))
        print("Ciclista agregado")
        ciclistas.append(ciclista)

    elif(opc==2):
        tiempo=100
        for ciclista in ciclistas:
            if(ciclista['tiempo']<tiempo):
              tiempo=ciclista['tiempo']
              nombre=ciclista['Nombre']
 
        print(f"El ciclista más rápido fue {nombre} con {tiempo}")    
    else:
     print("Dígite una opción válida")   

   
        
        
