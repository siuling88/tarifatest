'''
Created on Feb 11, 2015

@author: johanna
'''

import unittest
from calcularCosto import *

class Test(unittest.TestCase):


    def testcalcularEstadia(self):
        h1, h2 = calcularEstadia(datetime.datetime(4,4,4,7,50), datetime.datetime(4,4,4,14,55))
        
        
    def testcostoHorasCompletas(self):
        self.assertEqual(costoHorasCompletas(4,5),20)
        
    def testcostoFraccionHoraEsquema1(self):
        self.assertEqual(costoFraccionHoraEsquema1(0, 0), 0)
        self.assertEqual(costoFraccionHoraEsquema1(0, 5), 0)
        self.assertEqual(costoFraccionHoraEsquema1(5, 0), 0)    
        
    def testcostoFraccionHoraEsquema2(self):
        # si la fraccion es igual a 0

        self.assertEqual(costoFraccionHoraEsquema2(0, 0), 0)
        self.assertEqual(costoFraccionHoraEsquema2(0, 5), 0)   
        
        # si la fraccion es menor o igual que 30
        
        self.assertEqual(costoFraccionHoraEsquema2(25, 0), 0) 
        self.assertEqual(costoFraccionHoraEsquema2(25, 5), 2.5) 
        
        self.assertEqual(costoFraccionHoraEsquema2(30, 0), 0)
        self.assertEqual(costoFraccionHoraEsquema2(30, 10), 5)
                  
    def testcostoFraccionHoraEsquema3(self):
    
        #si la fraccion es igual a 0
        self.assertEqual(costoFraccionHoraEsquema3(0, 0), 0)
        self.assertEqual(costoFraccionHoraEsquema3(0, 5), 0)
        self.assertEqual(costoFraccionHoraEsquema3(5, 0), 0)
        
        #si la fraccion es diferente a 0
        
        self.assertEqual(costoFraccionHoraEsquema3(10, 120), 20)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()