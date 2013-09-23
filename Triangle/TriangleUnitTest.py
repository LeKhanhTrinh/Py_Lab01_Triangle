'''
Created on Sep 16, 2013

@author: KHANHTRINH
'''
import math

def typeOfTriangle(a, b, c):
    if ((isinstance(a, float) or isinstance(a, int)) and (isinstance(b, float) 
            or isinstance(b, int)) and (isinstance(c, float) or isinstance(c, int))):
        if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
            if a == b and b == c and c == a:
                return"Tam giac deu\n"
            elif (a == b) or (b == c) or (c == a):
                if (math.sqrt(a*a + b*b) == c) or (math.sqrt(c*c + b*b) == b) or (math.sqrt(a*a + c*c) == b):
                    return "Tam giac vuong can\n"
                else:
                    return"Tam giac can\n"
            elif (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
                return"Tam giac vuong\n"
            else:
                return"Tam giac binh thuong\n" 
        else:
            return "Khong phai tam giac\n"
    else:
        return "Gia tri dau vao khong phu hop\n" 
    
    
