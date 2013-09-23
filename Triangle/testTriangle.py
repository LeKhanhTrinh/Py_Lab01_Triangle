'''
Created on Sep 23, 2013

@author: KHANHTRINH
'''
import unittest
import math
import TriangleUnitTest

class triangle(unittest.TestCase):
    def testInputInvalid(self): # Test invalid
        print "Test case: a = %r, b = %r, c = %r" % ("-1",2,0)
        self.assertEqual(TriangleUnitTest.typeOfTriangle("-1", 2.0, 0.0), "Gia tri dau vao khong phu hop\n", "FAIL")
    def testInputValid(self):   # Test invalid.
        print "Test case: a = %r, b = %r, c = %r" % (1,4,5)
        self.assertEqual(TriangleUnitTest.typeOfTriangle(1.0, 4.0, 5.0), "Khong phai tam giac\n", "FAIL")
    def testTGVuong(self):  # Tam giac vuong
        print "Test case: a = %r, b = %r, c = %r" % (3,4,5)
        self.assertEqual(TriangleUnitTest.typeOfTriangle(3.0, 4.0, 5.0), "Tam giac vuong\n", "FAIL")
    def testTGcan(self):    # Tam giac can
        print "Test case: a = %r, b = %r, c = %r" % (2,2,1)
        self.assertEqual(TriangleUnitTest.typeOfTriangle(2.0, 2.0, 1.0), "Tam giac can\n", "FAIL")
    def testTGdeu(self):    # Tam giac deu
        print "Test case: a = %r, b = %r, c = %r" % (2,2,2)
        self.assertEqual(TriangleUnitTest.typeOfTriangle(2.0, 2.0, 2.0), "Tam giac deu\n", "FAIL")
    def testTGvuongcan(self):   # Tam giac vuong can
        print "Test case: a = %r, b = %r, c = %r" % (1,1,math.sqrt(2))
        self.assertEqual(TriangleUnitTest.typeOfTriangle(1.0, 1.0, math.sqrt(2.0)), "Tam giac vuong can\n", "FAIL")
    def testTGthuong(self):     # Tam giac thuong
        print "Test case: a = %r, b = %r, c = %r" % (3, 5, 7)
        self.assertEqual(TriangleUnitTest.typeOfTriangle(3, 5.0, 7.0), "Tam giac binh thuong\n", "FAIL")
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()