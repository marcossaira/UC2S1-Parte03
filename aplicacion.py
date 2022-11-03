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
            print("************************")
            print("                        ")
            print("Dato Persona")
            print("1. Listar personas")
            print("2. Agregar personas")
            print("3. Salir")
        else:
            n=n+1
            print("************************")
            print("Login o Clave incorrecto")
            print("                        ")

    print("Ha superado los 2 intentos. Adios")

validar()