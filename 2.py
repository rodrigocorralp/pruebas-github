"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y 
calcule el peso total del paquete que será enviado."""

payasos=(int(input("Ingrese el numero de payasos vendidos: ")))
muñecas=(int(input("Ingrese el numero de muñecas vendidas: ")))

pp= payasos*112
pm= muñecas*75

print("El numero de payasos vendidos es de",payasos, "con un peso de", pp, "gramos. Y el numero total de muñecas vendidas es de", muñecas, "con un peso de", pm, "gramos. El peso total seria de", pp + pm, "gramos." )
