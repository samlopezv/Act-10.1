def precio_antes_descuento(tipo_silla, cantidad) :
        if tipo_silla == 'B':
            return float(700*cantidad)
        elif tipo_silla == 'E':
            return float(900*cantidad)
        elif tipo_silla == 'L':
            return float(1500*cantidad)
        else: 
            print('Dato incorrecto')

def calcula_descuento(precio, tipo_cl) :
        if tipo_cl == 'F':
            return precio*0.2
        elif tipo_cl == 'N':
            if ((precio >= 10000) and (precio < 20000)):
                return precio*0.1
            elif precio>= 20000:
                return precio*0.15
            else:
                return precio*0
            

def main() :
    # pido el tipo de silla (B E L)
    tipo_silla = input("Tipo silla: ")
    # pido el tipo de cliente (N F)
    tipo_cl = input("Tipo cliente: ")
    cantidad = int(input("Cantidad de sillas: "))


    subtotal = precio_antes_descuento (tipo_silla, cantidad)
    desc = calcula_descuento(subtotal, tipo_cl)
    total = subtotal-desc

    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${desc:>7}")
    print(f"Total a pagar    ${total:>7}")

if __name__=='__main__':
    main()
