'''
Created on Sep 16, 2013

@author: KHANHTRINH
'''
import unittest

def typeOfTriangle(a, b, c):
    if (0 < a and a < 2^32-1) and (0 < b and b < 2^32-1) and (0 < c and c < 2^32-1):
        if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
            if a == b and b == c and c == a:
                print("Tam giac deu")
                return True
            elif (a == b) and (b == c) and (c == a):
                print("Tam giac can")
                return True
            elif (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
                print("Tam giac vuong")
                return True
            else:
                print("Tam giac binh thuong")
                return True 
        else:
            print("Khong phai tam giac")
            return False
    else:
        print("Gia tri dau vao khong phu hop") 
        return False
    
class triangle(unittest.TestCase):
    def testInputInvalid(self):
        print("Test case 1:")
        self.assertFalse(typeOfTriangle("-1", 2, 0), "Khong dung chuan so nguyen")
    def testInputValid(self):
        print("\nTest case 2:")
        self.assertFalse(typeOfTriangle(1, 4, 5), "Khong dung do dai canh")
    def testTGVuong(self):
        print("\nTest case 3:")
        self.assertTrue(typeOfTriangle(3, 4, 5), "Khong phai tam giac vuong")
    def testTGcan(self):
        print("\nTest case 4:")
        self.assertTrue(typeOfTriangle(2, 2, 1), "Khong phai tam giac can")
    def testTGdeu(self):
        print("\nTest case 5:")
        self.assertTrue(typeOfTriangle(2, 2, 2), "Khong phai tam giac deu")
    def testTGthuong(self):
        print("\nTest case 6:")
        self.assertTrue(typeOfTriangle(3, 5, 7), "Khong phai tam giac thuong")
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
    
