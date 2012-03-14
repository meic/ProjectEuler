import time
startTime=time.clock()

def isPerm(int1, int2):
        str1 = str(int1)
        str2 = str(int2)
        if len(str1) != len(str2):
                return False
        for ch in str1:
                if str1.count(ch) != str2.count(ch):
                        return False
        return True
        
print isPerm(345**3,385**3)
print isPerm(345**3,386**3)



endTime=time.clock()
print endTime-startTime