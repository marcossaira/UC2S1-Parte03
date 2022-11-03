# -*- coding: utf-8 -*-
def login():
    login=open("login.txt","rt",encoding="utf8")
    dato_login=login.read()
    return dato_login
def clave():
    clave=open("clave.txt","rt",encoding="utf8")
    dato_clave=clave.read()
    return dato_clave

def validar():
    n=0
    while n!=2:
        print("************************************")
        print("BIENVENIDO A LA APLICACION DE LA UC2")
        print("                                    ")
        print("                                    ")
        login1=input("Ingrese el login de su cuenta: ")
        clave1=input("Ingrese la clave de su cuenta: ")
        validar_login=login()
        validar_clave=clave()
    
        if (login1==validar_login and clave1==validar_clave):
            menu_opciones()
            
        else:
            n=n+1
            print("************************")
            print("Login o Clave incorrecto")
            print("                        ")

    print("Ha superado los 2 intentos. Adios")

def menu_opciones():
    print("Dato Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")

    opcion=input("Escriba el numero de su opcion: ")
    if opcion==1:
        listar_personas()
    elif opcion==2:
        agregar_personas()
    elif opcion==3:
        print("Ha escogido salir. Gracias")
    else:
        print("************************")
        print("Escoja una opcion valida")
        print("                        ")
        menu_opciones()

def listar_personas():
    dni=open("dni.txt","rt",encoding="utf8")
    dato_dni=dni.read()
    dni.close()
    nombre=open("nombre.txt","rt",encoding="utf8")
    dato_nombre=nombre.read()
    nombre.close()
    apellido=open("apellido.txt","rt",encoding="utf8")
    dato_apellido=apellido.read()
    apellido.close()

    x_dni=dato_dni.split()
    x_nombre=dato_nombre.split(  )
    x_apellido=dato_apellido.split()
    for i in range(0,10):

        print(f"{x_dni[i]} {x_nombre[i]} {x_apellido[i]}")

def agregar_personas():
    nombre1=input("Ingrese el nombre de la persona:  ")
    apellido1=input("Ingrese el apellido de la persona: ")
    dni1=input("Ingrese el DNI de la persona: ")
    dni=open("dni.txt","at",encoding="utf8")
    nombre=open("nombre.txt","at",encoding="utf8")
    apellido=open("apellido.txt","at",encoding="utf8")
    c_dni=str(dni1)
    c_nombre=str(nombre1)
    c_apellido=str(apellido1)
    dni.write(f"\n{c_dni}")
    apellido.write(f"\n{c_apellido}")
    nombre.write(f"\n{c_nombre}")
    dni.close()
    apellido.close()
    nombre.close()

validar()