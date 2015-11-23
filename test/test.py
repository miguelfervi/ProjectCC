# encoding: utf-8
import unittest

import os
import inspect

from script import *



# test para compobar que la ruta a un archivo (o archivo) existe
def existe(ruta):
    if os.stat(ruta):
	return os.stat(ruta)
    else: 
	return 0

# test para comprobar que existe una clase
def existe_clase(clase):
	try:
		return  type(clase)
	except:
		return 0

# test para comprobar que nos hemos conectado
def test_dbcon():
	return db==client.usuarios

class test (unittest.TestCase):
	# Inserción de un usuario en la base de datos
	def test_1(self):
		post = {"user": "miguel",
		    	"nombre": "miguel",
		    	"apellidos": "fernandez",
		    	"correo": "miguel@correo.es",
		    	"dia": "5",
		    	"mes": "7",
		    	"anio": "1991",
			"direccion": "Calle secreta prueba",
		    	"password": "123456",
		    	"pago": "VISA",
		    	"visa": "1111-1111-1111-1111",
		    	}

		posts=db.posts
		post_id = posts.insert(post)    

		#Comprobamos si realmente se ha insertado en la base de datos
		query=posts.find({"user": "miguel"})
		return query.count() == 1

	    def test_2(self):	
		existe_clase(registro) 
	
	    def test_3(self):	
		existe_clase(login)
	
	    def test_4(self):	
		existe_clase(logout)
	
	    def test_5(self):	
		existe_clase(ver_perfil)
	
	    def test_6(self):	
		existe_clase(editar_perfil)
	
	    def test_7(self):	
		existe_clase(mas_visitadas)
	
	    def test_8(self):	
		existe_clase(rss)
	
	    def test_9(self):	
		existe_clase(highchart)
	
	    def test_10(self):	
		existe_clase(mapa)

   

if __name__ == "__main__":
    unittest.main()
