import random , json
class Administrador_Cajas():

	def genera_cajas( self , ancho_caja , cant_niveles ):
		#El ancho define la divicion por 2 que aremos, 100/2 -> 100/4 -> 100/6 -> 100/8 -> 100/10
			#esto sera el ancho de las cajas
		#Las iteraciones definen la cantidad de niveles de las cajas
			#Las por cada nivel definimos un numero entero aleatorio que sera la altura para todas las cajas
		
		lista_altura_nivel = [ random.randint(1,5) * 2 for iteracion in range(cant_niveles) ] #Es multiplo de 2
		dicc_cajas =  { 'contenedor': (0,0) , "cant_cajas": 0 , 'niveles_cajas': [] }
		altura_contenedor = 0
		divicion = 2

		for altura in lista_altura_nivel: #Define un nivel
			
			altura_contenedor += altura
			
			if divicion == 12:
				divicion = 2
			
			ancho = int( ancho_caja/divicion )
			list_nivel_caja = [ (altura,ancho) ] * divicion
			
			ancho_caja_faltante = ancho_caja - (ancho*divicion)
			if ancho_caja_faltante != 0:
				list_nivel_caja.append( (altura,ancho_caja_faltante) )
			
			dicc_cajas['niveles_cajas'].append( list_nivel_caja )
			dicc_cajas["cant_cajas"] += len( list_nivel_caja )
			divicion += 2

		dicc_cajas['contenedor'] = ( ancho_caja , altura_contenedor )
		return dicc_cajas
	
	def retorna_lista_unica_cajas_txt( self , archivo_json ):
		with open( archivo_json , 'r' ) as file:
			data = json.load(file)
		lista_all_cajas = []
		for nivel in data['niveles_cajas']:
			lista_all_cajas += [ tuple(caja) for caja in nivel ] 

		return lista_all_cajas

	def guardar_datos_caja_txt( self , dicc_datos , nombre_json ):
	
		with open( nombre_json , 'w') as file:
			json.dump( dicc_datos , file , indent=4)


#Configuracion --->>>
#----------------->>>
ancho = 300
niveles = 163
#----------------->>>
#----------------->>>

obj_admin = Administrador_Cajas()

dicc_contenedor = obj_admin.genera_cajas( ancho , niveles )
for nivel_caja in dicc_contenedor['niveles_cajas']:
	break
	#print( nivel_caja )
	#pass
print( dicc_contenedor['contenedor'] )
print( dicc_contenedor['cant_cajas'] )

#obj_admin.guardar_datos_caja_txt( dicc_contenedor , 'salida.txt' )
print( obj_admin.retorna_lista_unica_cajas_txt( 'salida.txt' ) )