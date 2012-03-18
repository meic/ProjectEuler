

f = open( 'keylog.txt' , 'r')

keys = []
for line in f:
        keys.append(line[:3] )

final =[]
        
def findNext():        
        pFirst = []
        for key in keys:
                if len(key):
                        if not key[0] in pFirst:
                                pFirst.append(key[0])
                

        for x in pFirst:
                poss = True
                for key in keys:
                        if x in key:
                                if key.index(x) != 0:
                                        
                                        poss = False
                                        break
                if poss:
                        final.append(x)
                        print x
                        
        for i in range(len( keys ) ):
                if len(keys[i]):
                        if keys[i][0] == final[-1]:
                                keys[i] = keys[i][1:]
                        
        print keys

while max([len(key) for key in keys])>0:      
        findNext()
        
print ''.join(final)