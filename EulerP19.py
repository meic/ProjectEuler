import time
startTime=time.clock()

import datetime

startDate = datetime.date(1901,1,1)  #is a tuesday
endDate = datetime.date(2000, 12,31) 

count = 0

for year in range(1901,2001):
        for month in range(1,13):
                currentDate = datetime.date(year,month,1)
                if (currentDate - startDate).days % 7 ==5:
                        count+=1
                        
print count

endTime=time.clock()
print endTime-startTime