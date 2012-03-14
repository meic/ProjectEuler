import time
startTime=time.clock()



i = 1
for f1 in xrange(0, 200+1, 100):
    for p50 in xrange(0, 200+1-f1, 50):
        for p20 in xrange(0, 200+1-f1-p50, 20):
            for p10 in xrange(0, 200+1-f1-p50-p20, 10):
                for p5 in xrange(0, 200+1-f1-p50-p20-p10, 5):
                    for p2 in xrange(0, 200+1-f1-p50-p20-p10-p5, 2):
                        i += 1
print i # 73682 time 0.0315790176392


endTime=time.clock()
print endTime-startTime