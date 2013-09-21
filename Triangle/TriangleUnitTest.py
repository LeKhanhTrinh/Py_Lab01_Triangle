'''
Created on Sep 16, 2013

@author: KHANHTRINH
'''
import unittest
import math

def typeOfTriangle(a, b, c):
    if (float(a)) and (float(b)) and (float(c)):
        if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
            if a == b and b == c and c == a:
                print"Tam giac deu\n"
                return True
            elif (a == b) or (b == c) or (c == a):
                if (math.sqrt(a*a + b*b) == c) or (math.sqrt(c*c + b*b) == b) or (math.sqrt(a*a + c*c) == b):
                    print "Tam gia vuong can\n"
                    return True
                else:
                    print"Tam giac can\n"
                    return True
            elif (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
                print"Tam giac vuong\n"
                return True
            else:
                print"Tam giac binh thuong\n"
                return True 
        else:
            print"Khong phai tam giac\n"
            return False
    else:
        print"Gia tri dau vao khong phu hop\n" 
        return False
    
class triangle(unittest.TestCase):
    def testInputInvalid(self): # Test invalid
        print "Test case: a = %r, b = %r, c = %r" % ("-1",2,0)
        self.assertFalse(typeOfTriangle("-1", 2, 0), "Khong dung chuan so nguyen")
    def testInputValid(self):   # Test invalid
        print "Test case: a = %r, b = %r, c = %r" % (1,4,5)
        self.assertFalse(typeOfTriangle(1, 4, 5), "Khong dung do dai canh")
    def testTGVuong(self):  # Tam giac vuong
        print "Test case: a = %r, b = %r, c = %r" % (3,4,5)
        self.assertTrue(typeOfTriangle(3, 4, 5), "Khong phai tam giac vuong")
    def testTGcan(self):    # Tam giac can
        print "Test case: a = %r, b = %r, c = %r" % (2,2,1)
        self.assertTrue(typeOfTriangle(2, 2, 1), "Khong phai tam giac can")
    def testTGdeu(self):    # Tam giac deu
        print "Test case: a = %r, b = %r, c = %r" % (2,2,2)
        self.assertTrue(typeOfTriangle(2, 2, 2), "Khong phai tam giac deu")
    def testTGvuongcan(self):   # Tam giac vuong can
        print "Test case: a = %r, b = %r, c = %r" % (1,1,math.sqrt(2))
        self.assertTrue(typeOfTriangle(1, 1, math.sqrt(2)), "Khong phai tam giac deu")
    def testTGthuong(self):     # Tam giac thuong
        print "Test case: a = %r, b = %r, c = %r" % (3, 5, 7)
        self.assertTrue(typeOfTriangle(3, 5, 7), "Khong phai tam giac thuong")
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    
