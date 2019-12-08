# He agregado este comentario.
# Ahora le he ingresado este otro comentario.

error=0
linea=0
columna=0

with open("/home/pablobarbag/PythonCode/OpenOrder2.txt") as fp:
    for i in fp:
        linea+=1
        cadena=i

        if (linea==1):

            #
            # Validate header section
            #

            print("Validating Header...")
            if (cadena=="Sku\tLocationName\tOrderType\tOverDueFlag\tFrozenOrderFlag\tOrderStatus\tOrderNumber\tOrderLine\tShipDate\tRecDate\tQty\tCustomerSupplierName\tOrderInfo\tDataCreateDate\n"):
                print("Header match: Open Order\n")

            elif (cadena=="Sku\tLocationName\tOrderTyp\tOverDueFlag\tFrozenOrderFlag\tOrderStatus\tOrderNumber\tOrderLine\tShipDate\tRecDate\tQty\tCustomerSupplierName\tOrderInfo\tDataCreateDate\n"):
                print("Header match: Observation Data\n")
            else:
                print("Header error!!!\n\n")

            #
            # End of header section
            #

        while len(cadena)>0:
            indiceTAB = cadena.find('\t')

            if indiceTAB==-1: #No hay mas TABs
                break
            elif indiceTAB==len(cadena)-1: #el TAB es el ultimo caracter de la cadena
                break
            elif indiceTAB==0: #el TAB es el primer caracter de la cadena
                cadena=cadena[1:len(cadena)]
            else:
                if cadena[indiceTAB-1] == ' ': #Reviso si tengo un espacio antes del TAB
                    cadena = cadena[indiceTAB + 2:len(cadena)]
                    columna=(len(i)-len(cadena))-3
                    error+=1
                    print("Space found before TAB\n" + "Line Number: " + str(linea) + "\n" + "Column: " + str(columna) + "\n" + "Line Text: " + str(i))
                    print("****************************************************")
                if cadena[indiceTAB+1] == ' ': #Reviso si tengo un espacio despues del TAB
                    cadena = cadena[indiceTAB + 1:len(cadena)]
                    columna = (len(i) - len(cadena))
                    print("Space found after a TAB\n" + "Line Number: " + str(linea)+"\n" + "Column: " + str(columna) + "\n" + "Line Text: " + str(i))
                    print("****************************************************")
                    error+=1
                else:
                    cadena=cadena[indiceTAB+1:len(cadena)]
print("Number of errors: " + str(error))
print("Process complete")

/home/pablobarbag/.PyCharmCE2019.1/config/scratches/Prueba.py
