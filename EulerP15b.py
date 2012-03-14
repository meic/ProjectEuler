import time
startTime=time.clock()

size=21
rows = 2*(size-1)-1

matrix=[[0 for y in range(0,size-1)] for x in range(0,size-1)]
#print matrix

for x in range(0,size-1):
        matrix[0][x]=matrix[x][0]=x+2

for row in range(1,rows+1):
        for pos in range(row):
                x=1+pos
                y=row-pos
                if x < size-1 and y<size-1:                
                        matrix[x][y]=matrix[x-1][y]+matrix[x][y-1]

#print matrix
print matrix[-1][-1]                  
                        
endTime=time.clock()
print endTime-startTime