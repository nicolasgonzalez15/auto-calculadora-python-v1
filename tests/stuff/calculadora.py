# Ingreso valores
def suma(nro1,nro2):
    return nro1+nro2

def resta(nro1,nro2):
    return nro1-nro2

def producto(nro1,nro2):
    return nro1*nro2

def division(nro1,nro2):
    return nro1/nro2

def menu():
    print("----------------------------")
    print("Bienvenido a la calculadora.")
    print("----------------------------")
    print("---------Opciones-----------")
    print("1) Suma ")
    print("2) Resta ")
    print("3) Producto ")
    print("4) División ")
    print("0) Salir ")

"""
def main():
    while True:
        menu()


        try:
            print("------------------------------------")
            opcion = int(input("Ingresar opción: "))
            valor1 = int(input("Ingresar primer número: "))
            valor2 = int(input("Ingresar segundo número: "))
            print("------------------------------------")
            match opcion:
                case 1:
                    resultado = suma(valor1,valor2)
                case 2:
                    resultado = resta(valor1,valor2)    
                case 3:
                    resultado = producto(valor1,valor2)  
                case 4:
                    resultado = division(valor1,valor2) 
                case 0:
                    print("------------------------------------")
                    print("Gracias por usar la calculadora.")
                    break  
                case _:
                    print("------------------------------------")
                    print("Error. Número inválido.")

        except ValueError:
            print("------------------------------------")
            print(f"Error, tipo de dato no válido.")
        except ZeroDivisionError:
            print("------------------------------------")
            print("Error. No se puede dividir por 0.")
        else:
            print("------------------------------------")
            print(f"El resultado de la operacion es: {resultado}")
        finally: #cerrar archivos
            print("------------------------------------")
            print("Termina programa.")


main()
"""
"""
if __name__ == "__main__":
    print("Hola estoy adentro del if")
"""