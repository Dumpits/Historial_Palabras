lista = []
exit = False

while exit == False:
    palabra = input("Escriba una palabra (history revelará el historial)")
    if palabra.upper() == "history".upper():
        print ("Aquí está el array: " , lista)
    else:
        lista.append(palabra)