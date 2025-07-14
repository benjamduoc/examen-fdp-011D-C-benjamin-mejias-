productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10],
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32],
        '342FHD': [444990,7],
        'GF75HD': [749990,2],
        'UWU131HD': [349990,1],
        'FS1230HD': [249990,0],
}

def stock_marca():
    input("Ingrese la marca que este buscando: ")
    
    for stock in productos:
        print(f"{stock:{0}}")

def busqueda_precio():
    precio_min = input("ingrese precio minim: ")
    precio_max= input("ingrese precio maximo: ")
    if precio_min > 0 and precio_max < 999999:
        print(productos)
    else:
        print("no se encuentra")

def listado_produc():
    for productos in stock:
        print(productos)


def menu():
    while True:
        print("MENU PRINCIPAL")
        print("1- stock marca")
        print("2- busqueda por precio")
        print("3- listado de producto")
        print("4- salir")

        opcion = input("cual opcion requiere?: ")

        if opcion == '1':
            stock_marca()
        elif opcion == '2':
            busqueda_precio()
        elif opcion =='3':
            listado_produc()
        elif opcion == '4':
            break
        else:
            print("opcion no valida!!!!!")
menu()
