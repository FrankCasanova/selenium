# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class Hello_World(unittest.TestCase):

    #nuestros text features van a estar definidos como métodos
    #va a ejecutar todo lo necesario antes de hacer una prueba
    #con la versión sin method se ejecuta en ventanas diferentes, para evitar eso
    #usamos el decorador classmethod
    #ese sedcorador se usa en setUp y en tearDown a los cuales hay que incluirles Class al final
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    #modulo de pruebas, prueba unitaria
    #aquí vamos a hacer una serie de acciones para que el navegador las automatice
    #aquí indicamos que abra esas páginas
    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def test_visti_wikipedia(self):
        driver = self.driver
        driver.get('http://www.wikipedia.com')    

    #el siguiente test feature da la salida a lo que estemos escribiendo
    #acciones para finalizar, cerrar la ventana del navegador, para que el equipo evite ponerse lento
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()





    pass

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))	
