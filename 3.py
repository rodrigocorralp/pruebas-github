""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total."""

bvno=(int(input("Ingrese el numero de barras de pan vendidas que no son del día: ")))

costo = bvno*3.49
des = round(costo - (costo*0.60),2)

print("El precio habitual de una barra de pan es de 3.49€. Usted recibe un descuento del 60%. \nCosto total sin descuento:", costo, "\nCosto total con descuento:", des)

