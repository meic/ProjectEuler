import time
# import math
startTime=time.clock()
        
f = open(".\EulerP54.data","r")

def hands():
        for line in f:
                hand=line.split(" ")
                hand[-1]=hand[-1][0:2]
                yield hand

order=[str(n) for n in range(2,10)]+["T","J","Q","K","A"]
# print order

def rank(fiveCards):
        #check flush
        isflush=1
        for i in range(1,5):
                if fiveCards[i][1]!=fiveCards[0][1]:
                        isflush=0
                        break
        #check straight
        isstraight=1
        straightList=[]
        for card in fiveCards:
                straightList.append(order.index(card[0]))
        straightList.sort()
        straightList.reverse()
        for i in range(1,5):
                if straightList[i]!=straightList[0]-i:
                        isstraight=0
                        break
        
        #straight flush 8
        if isstraight and isflush:
                return [8,straightList[0]]
        #max count
        maxCount=1
        for card in straightList:
                if straightList.count(card)>maxCount:
                        maxCount=straightList.count(card)
                
        # four of a kind 7
        if maxCount==4:
                for card in straightList:
                        if straightList.count(card)==4:
                                x=card
                        if straightList.count(card)==1:
                                y=card
                return [7,x,y]
        
        #full house 6
        if maxCount==3:
                for card in straightList:
                        if straightList.count(card)==2:
                                y=card
                                for card in straightList:
                                        if straightList.count(card)==3:
                                                x=card
                                                break
                                return [6,x,y]
        
        #flush 5
        if isflush:
                return [5,]+straightList
        
        #straight 4
        if isstraight:
                return [4,straightList[0]]
                
        #three of a kind 3
        if maxCount==3:
                retlist=[3,0,]
                for card in straightList:
                        if straightList.count(card)==3:
                                retlist[1]=card
                        if straightList.count(card)==1:
                                retlist.append(card)
                return retlist
        #two pairs 2
        if maxCount==2:
                tpcount=0
                for card in straightList:
                        if straightList.count(card)==2:tpcount += 1
                if tpcount==4:
                        tplist=[]
                        for card in straightList:
                                if straightList.count(card)==2:tplist.append(card)
                                if straightList.count(card)==1:x=card
                        return [2,tplist[0],tplist[2],x]
        
        #one pair 1
        if maxCount==2:
                retlist=[1,0,]
                for card in straightList:
                        if straightList.count(card)==2:
                                retlist[1]=card
                        if straightList.count(card)==1:
                                retlist.append(card)
                return retlist
        #high card 0
        return [0,]+straightList
        
        return [0,straightList]    

        
def winner(p1list,p2list):
        for i in range(len(p1list)):
                if p1list[i]>p2list[i]:
                        return True
                elif p1list[i]<p2list[i]:
                        return False
        print "SHITTT"
n=0
checkdig=0
p1wins=0
for hand in hands():
        # print hand
        # if rank(hand[:5])[0]==checkdig:
                # print "player 1"
                # print hand[:5]
                # print rank(hand[:5])
        # if rank(hand[5:])[0]==checkdig:
                # print "player 2"
                # print hand[5:]
                # print rank(hand[5:])
        if winner(rank(hand[:5]),rank(hand[5:])):p1wins+=1
        n+=1
print p1wins
        # print n
        # if n==10: break
        
# print rank(["5D","6H","8S","7C","9D"])        
        
endTime=time.clock()
print endTime-startTime