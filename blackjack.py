# 블랙잭 카드게임
'''
1.내 재산
2.유저의 카드 2장 랜덤으로 받기
3.컴퓨터의 카드 2장 랜덤으로 받기
4.힛, 스탠드, 더블(처음만), 블랙잭 나오면 자동 스탑
'''
import random
import os
wallet=10000
while True:
    my_card=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11]
    com_card =[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11]
    # 알림판
    print("[WELCOME TO THE BLACKJACK!!!]")
    #딜러는 무조건 17에서 스탠드, 16이 나오기 전까지 히트
    print("[Dealer must stand on 17 and must draw to 16]")

    gamble=int(input("Set Money: "))
    pan_money=wallet-gamble
    # 카드 2장 받는다.    
    mc=random.sample(my_card,2)
    #컴퓨터도 2장 받는다.
    cc=random.sample(com_card,2)
    print("My Cards: ",mc,"Score: ", sum(mc))
    # 버스트
    # 드로우
    #딜러의 첫 번째 카드는 볼 수 있다!         
    print("Dealer's 1st Card","[",cc[0],"]")           
    while True:
            # 2장이 블랙잭일때!
        if sum(mc)==21:
            if sum(mc)>sum(cc):
                print(" BLACKJACK!!!","\n","My Cards: ",mc,"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                wallet+=gamble
                print("My Money: ", wallet)
            break
            #컴퓨터가 블랙잭일 때
        if sum(cc)==sum(mc)==21:
          print(" BLACKJACK!!! BUT DRAW...",cc,"Dealer's score",sum(cc))
        else:
            #컴퓨터 패
            while True:
            #16이 이하는 무조건 드로우
                if sum(cc)<=16:
                    b=random.choice(com_card)
                    cc.append(b)
                #17이상 20이하일때 스탠드
                elif 17<=sum(cc)<=20:
                    break
                elif sum(cc)>21:
                    break
                #블랙잭
                else:
                    break            
        print("="*30)
        hos=int(input("Draw(1) or Stand(2)? : "))
        if hos ==1:
            if sum(mc)<21: 
                a=random.choice(my_card)    
                mc.append(a)
                print("My Cards: ",mc,"Score: ", sum(mc))
                
                #버스트 승패 조건
                if sum(mc)>21:
                    print("BUST...","\n","My Cards: ",mc,"My Score: ", sum(mc),"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                    wallet-=gamble
                    print("My Money: ", wallet)                      
                    break
                #블랙잭
                elif sum(mc)==21:
                    if sum(mc)>sum(cc):
                        print(" BLACKJACK!!!","\n","My Cards: ",mc,"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                        wallet+=gamble
                        print(" My Money: ", wallet)
                        break                        
                    elif sum(mc)==sum(cc):
                        print(" BLACKJACK!!! BUT DRAW...",cc,"Dealer's score",sum(cc))
                        print(" My Money: ",wallet)                        
                        break   

        #스탠드
        else:
            if sum(cc)>21:
                print("Dealer BUST!!!","\n","My Cards: ",mc,"My Score: ", sum(mc),"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                wallet+=gamble
                print("My Money: ", wallet) 
                break   
            if sum(mc)>sum(cc): # 승
                print(" WIN!!!","\n","My Cards: ",mc,"My Score: ", sum(mc),"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                wallet+=gamble
                print(" My Money: ",wallet)                  
                break
            elif sum(mc)<sum(cc)<=21:
                print(" Lose...","\n","My Cards: ",mc,"My Score: ", sum(mc),"\n","Dealer's Cards: ",cc,"Dealer's score",sum(cc))
                wallet-=gamble
                print(" My Money: ",wallet)                     
                break

            elif sum(mc)==sum(cc):                   #무승부
                print(" DRAW!","\n","My Cards: ",mc,"My Score: ", sum(mc),"\n","Dealer's Cards: ",cc
