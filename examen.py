#Examen de Benjamin Saavedra
# 11-07-25
#Menu para tienda online pybooks
#Diccionarios:

productos ={
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    }

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
    
}
#---------------------------------------------------------------------------------------------------------------
#Arreglos

def stock_marca(prdouctos):
    print("-Stock Marca-")
    total=0
    for dato1,dato2 in productos.items():
        if(dato2[1].lower()==stock.lower()):
            total+=stock[dato1][1]
    print(f"El stock total para {"tipo"} es: {total}")

def busqueda_precio(p_min, p_max):
    print("-Busqueda por precio-")
    resultados=[]
    for productos,stock in productos.items():
        PorPrecio=stock[0]
        total+=resultados
        if (PorPrecio in stock.items()):
            print("El notebook esta")

def listado_de_productos(stock,productos):
    print("-Listado de productos-")
    print(f"Productos disponibles son: {productos.items()}")

#---------------------------------------------------------------------------------------------------------------
def main():          #Menu principal Fijo
    #While para programa continuo
    while True:
        #Menu visual para el usuario
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        try:
            opcMenu=int(input("Ingrese Opción: "))#Opcion de menu principal visual.
            #Opciones seleccionadas por el usuario

            if (opcMenu==1):
                tipoPc=input("Ingrese que marca de computador desea(hp,acer,asus,dell): ")
                stock_marca(productos)
            elif (opcMenu==2):
                listado_de_productos(stock,productos)
            elif (opcMenu==3):
                try:
                    BuscaPorPrecio=float(input("Ingrese el precio de el producto a buscar: "))# 749990
                    if BuscaPorPrecio not in (stock,productos):
                        print("Producto no disponible")
                    else:
                        busqueda_precio(productos,stock)
                        print(stock.items)
                except:
                    print("Producto no encontrado por favor intentelo nuevamente(recuerde no poner comas ni decimales)")   
            elif (opcMenu==4):#Finalizar el programa
                print("Programa finalizado.")
                break
            else:
                print("Debe seleccionar una opción válida!!")
        except:
            print("ERROR. Ingrese un caracter valido")
#Control de errores
if __name__=="__main__":
    main()
