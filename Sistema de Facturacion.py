intentos = 0
salir = "si"
total_general = 0

print("===================== Área Registro ==========================")

nombre = input("Escriba su nombre: ")
cedula = int(input("Digite su cédula: "))
numero_cel = int(input("Digite su número de teléfono: "))
correo = input("Escriba su correo: ")
ID = int(input("Digite su ID correspondiente: "))  # ID´s disponibles: 1 y 2

if ID == 1:
    contraseña = 1
elif ID == 2:
    contraseña = 2
while intentos < 3:
    cred = int(input("Digite la contraseña: "))
    if cred == contraseña:
        print("Credencial correcta. Ingresando a la siguiente pestaña...")
        print("\n===================== Bienvenida =====================")
        print("Bienvenido/a a SportZone!")
        print("Es un placer atenderle")

        while True:
            oper = int(input("\nSeleccione el tipo de operación que desea hacer: 1. Ver Productos, 2. Ver Servicios, 3. Ver Paquetes, 4. Pagar/Salir: "))

            if oper == 1:
                while True:
                    print("\n===================== Productos =====================")
                    print("1. Bicicleta de Montaña - ₡136000")
                    print("2. Casco - ₡33350")
                    print("3. Guantes - ₡10200")
                    print("4. Kit Herramientas - ₡21500")
                    print("5. Colchoneta - ₡14425")
                    print("6. Cuerda para Saltar - ₡6300")
                    print("7. Botella de Agua - ₡9000")
                    print("8. Volver al menú principal")

                    producto = int(input("Seleccione el producto que desea (1-8): "))
                    precios = {1: 136000, 2: 33350, 3: 10200, 4: 21500, 5: 14425, 6: 6300, 7: 9000}

                    if producto == 8:
                        break
                    if producto in precios:
                        cantidad = int(input("¿Cuántos desea llevar?: "))
                        subtotal = precios[producto] * cantidad
                        monto_total = subtotal + (subtotal * 0.13)
                        total_general += monto_total
                        print(f"Monto a pagar: {int(monto_total)}")

                        input("\nPresione Enter para volver al menú principal ")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")

            elif oper == 2:
                while True:
                    print("\n===================== Servicios =====================")
                    print("1. Asesoría uso de productos - ₡8500")
                    print("2. Asesoría de entrenamiento - ₡8500")
                    print("3. Membresía GYM - ₡24000")
                    print("4. Volver al menú principal")

                    servicio = int(input("Seleccione una opción (1-4): "))

                    if servicio == 4:
                        break

                    if servicio in [1, 2, 3]:
                        if servicio == 1 or servicio == 2:
                            precio = 8500
                        else:
                            precio = 24000

                        cantidad = int(input("¿Cuántos desea llevar?: "))
                        subtotal = precio * cantidad
                        monto_total = subtotal + (subtotal * 0.13)
                        total_general += monto_total
                        print(f"Monto a pagar: {int(monto_total)}")

                        input("\nPresione Enter para volver al menú principal ") #Aqui no hace falta presiona enter en si, pq el programa igual lo va a continuar si selecciona un 1,2,3,4,etc
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")

            elif oper == 3:
                while True:
                    print("\n===================== Paquetes =====================")
                    print("1. Bicicleta, Casco, Guantes, Herramientas - ₡170900")
                    print("2. Colchoneta, Cuerda, Botella de Agua - ₡21000")
                    print("3. 4 Clases Boxeo, 2 Running, Membresía GYM - ₡50000")
                    print("4. Entrenamiento, Nutrición, Evaluación, Camisa - ₡75000")
                    print("5. Volver al menú principal")

                    paquete = int(input("Seleccione el paquete que desea (1-5): "))
                    precios_paquetes = {1: 170900, 2: 21000, 3: 50000, 4: 75000}

                    if paquete == 5:
                        break

                    if paquete in precios_paquetes:
                        cantidad = int(input("¿Cuántos desea llevar?: "))
                        subtotal = precios_paquetes[paquete] * cantidad
                        monto_total = subtotal + (subtotal * 0.13)
                        total_general += monto_total
                        print(f"Monto a pagar: {int(monto_total)}")


                        input("\nPresione Enter para volver al menú principal... ")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")

            elif oper == 4:
                print("\n===================== Facturación =====================")
                print(f"Nombre: {nombre}")
                print(f"Cédula: {cedula}")
                print(f"Teléfono: {numero_cel}")
                print(f"Correo: {correo}")
                print(f"Total a pagar: {int(total_general)}")
                print("\nGracias por preferirnos!!")
                print("\nTe recordamos nuestro horario de atención")
                print("Lunes - Jueves: 8:00am - 5:00pm")
                print("Viernes: 8:30am - 5:00pm")
                print("Sábado: 8:00am - 1:00pm")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        break
    else:
        intentos += 1
        print(f"Intento fallido. Te quedan {3 - intentos} intentos")
        if intentos >= 3:
            print("Demasiados intentos fallidos. Saliendo del sistema")
            break
