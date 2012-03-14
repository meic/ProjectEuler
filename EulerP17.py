import time
startTime=time.clock()

onetonine=3+3+5+4+4+3+5+5+4

tentonineteen=3+6+6+8+8+7+7+9+8+8

twentytoninety=6+6+5+5+5+7+6+6

onetoninetynine=onetonine*9+tentonineteen+twentytoninety*10

hun=7
hunand=10

oneto999=10*onetoninetynine+99*9*hunand+9*hun+100*onetonine

onethousand = 11

total=oneto999+onethousand

print total

endTime=time.clock()
print endTime-startTime