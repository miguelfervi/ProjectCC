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
		self.assertTrue(clase)
		return  type(clase)
	except:
		return 0

# test para comprobar que nos hemos conectado
def test_dbcon():
	return db==client.usuarios

class test (unittest.TestCase):
	
	    def test_1(self):	
		existe_clase(registro) 
	
	    def test_2(self):	
		existe_clase(login)
	
	    def test_3(self):	
		existe_clase(logout)
	
	    def test_4(self):	
		existe_clase(ver_perfil)
	
	    def test_5(self):	
		existe_clase(editar_perfil)
	
	    def test_6(self):	
		existe_clase(mas_visitadas)
	
	    def test_7(self):	
		existe_clase(rss)
	
	    def test_8(self):	
		existe_clase(highchart)
	
	    def test_9(self):	
		existe_clase(mapa)

  
if __name__ == "__main__":
    unittest.main()
