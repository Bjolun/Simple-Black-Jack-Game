from random import shuffle
import time


cards = {"H2" : 2, "H3" : 3, "H4": 4, "H5" : 5, "H6" : 6, "H7" : 7, "H8" : 8, "H9": 9, "H10":10,
        "HJ" : 10, "Hq" : 10, "Hk" : 10, "Ha" : 11,
        "C2": 2, "C3": 3, "C4": 4, "C5":5, "C6":6, "C7":7, "C8":8, "C9":9, "C10":10, "Cj":10,
        "Cq" : 10, "Ck" : 10, "Ca" : 11,
        "S2" : 2, "S3" : 3, "S4": 4, "S5": 5, "S6":6, "S7": 7, "S8": 8, "S9": 9, "S10":10,
        "Sj" : 10, "Sq" : 10, "Sk": 10, "Sa" : 11,
        "D2":2,"D3":3,"D4":4,"D5":5,"D6":6,"D7":7,"D8":8,"D9":9,"D10":10,"Dj":10,
        "Dq":10,"Dk":10,"Da":11}


cardlist = []

for key in cards.keys():
    cardlist.append(key)

shuffle(cardlist)

class Player():
    
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        
    def win(self):
        self.credit += bet
        
    def lose(self):
    	self.credit -= bet

def player_info():
	#Spør spilleren om info som navn og hvor mye credits de vil starte med.
    global spiller_name, start_credit
    spiller_name = str(input("Vennlist skriv inn navnet ditt: "))

    start_credit_ask = int(input("Hvor mye penger vil du starte med? "))
    
    start_credit = start_credit_ask


def start_bet():
	#Spør spilleren hvor mye de vil satse.
    global bet
    while True:
        try:
            bet = int(input("Hvor mye vil du satse? "))
        except:
            print("Det var ikke et tall! Vennligst skriv inn en tallverdi.")
            continue
        else:
            print("\n"*2)
            if bet < spiller.credit:
            	print("Takk, du har satset {}".format(bet))
            else:
                bet = spiller.credit
                print("Du har ikke nok penger, satser maksimalt for deg, som er {}".format(spiller.credit))
            break

def del_ut_kort_forste_gang():
	#Deler ut kort første gang, først en til spilleren, så en til dealer, så en til til spilleren og et siste til dealer.
    global player_hand, dealer_hand, dealer_second_card, popped_cards_player,popped_cards_dealer
    player_hand = 0
    dealer_hand = 0
    popped_cards_player = []
    popped_cards_dealer = []
    
    print("{}, dine to første kort er {} og {}".format(spiller_name, cardlist[0], cardlist[2]))
    player_hand += cards[cardlist[0]] + cards[cardlist[2]]
    popped_cards_player.append(cardlist[0])
    cardlist.pop(0)
    popped_cards_player.append(cardlist[1])
    cardlist.pop(1)
    
    print("Dealer sitt først kort er {}, det andre kortet er snudd opp-ned.".format(cardlist[0]))
    dealer_hand += cards[cardlist[0]] + cards[cardlist[1]]
    popped_cards_dealer.append(cardlist[0])
    cardlist.pop(0)
    popped_cards_dealer.append(cardlist[0])
    dealer_second_card = cardlist[0]
    cardlist.pop(0)
    print("\n"*1)


def win_condition():
	#Sjekker forskjellige win conditions for å kalle på enten spiller.win() eller spiller.lose()
    playerpoints = 21 - player_hand
    dealerpoints = 21 - dealer_hand

    
    if playerpoints == 0 and dealerpoints != 0:
        spiller.win()
        print("Gratulerer, du fikk 21 poeng, dealer gjorde det ikke, og du vant derfor {}!".format(bet * 2))
        print("\n"*1)
        time.sleep(2.0)
    elif playerpoints >= 0 and dealerpoints < 0:
        spiller.win()
        print("Gratulerer, dealer gikk over 21, du vant {}!".format(bet * 2))
        print("\n"*1)
        time.sleep(2.0)
    elif playerpoints >= 0 and playerpoints < dealerpoints:
        spiller.win()
        print("Gratulerer, du fikk fler poeng enn dealer, og vant {}!".format(bet * 2))
        print("\n"*1)
        time.sleep(2.0)
    else:
        spiller.lose()	
        print("Du tapte desverre denne runden.")
        print("\n"*1)
        time.sleep(2.0)


def more_player_cards():
	#Spør spilleren om han eller hun vil ha fler kort.
    global player_hand
    ask_for_cards = True
    while ask_for_cards == True:

        if player_hand > 21 and "Ha" in popped_cards_player:
            player_hand -= 10
            print("Trekker fra 10 poeng fra dine sine poeng siden summer er over 21 og du har et ess")
        elif player_hand > 21 and "Ca" in popped_cards_player:
            player_hand -= 10
            print("Trekker fra 10 poeng fra dine sine poeng siden summer er over 21 og du har et ess")
        elif player_hand > 21 and "Da" in popped_cards_player:
            player_hand -= 10
            print("Trekker fra 10 poeng fra dine sine poeng siden summer er over 21 og du har et ess")
        elif player_hand > 21 and "Sa" in popped_cards_player:
            player_hand -= 10
            print("Trekker fra 10 poeng fra dine sine poeng siden summer er over 21 og du har et ess")


        try:
            fler_kort = str(input("Ønsker du fler kort? Svar ja eller nei: "))
        except:
            print("Vennligst svar ja eller nei. ")
            continue
        else:
            if fler_kort.lower() == "ja" and player_hand < 21:
                player_hand += cards[cardlist[0]]
                print("Takk, ditt nye kort er {}, du er derfor på {} poeng".format(cardlist[0], player_hand))
                time.sleep(1.0)
                popped_cards_player.append(cardlist[0])
                cardlist.pop(0)
            elif fler_kort.lower() == "nei":
                print("Den er god, dealer sin tur.")
                time.sleep(2.0)
                ask_for_cards = False
            elif player_hand >= 21:
                print("Du er over eller på 21 poeng, og kan derfor ikke trekke flere kort")
                time.sleep(1.0)
                ask_for_cards = False
            



def dealer_pick_cards():
    global dealer_hand, popped_cards_dealer, popped_cards_player 

    print("Dealer sitt andre kort var {}, som gjør at dealer er på {} poeng.".format(dealer_second_card, dealer_hand))
    time.sleep(4.0)

    while dealer_hand <= 16:
        dealer_hand += cards[cardlist[0]]
        print ("Dealer har under 16 poeng og må trekke et kort.\nDealer fikk {} og har nå {} poeng".format(cardlist[0], dealer_hand))
        time.sleep(4.0)
        popped_cards_dealer.append(cardlist[0])
        cardlist.pop(0)
        if dealer_hand > 21 and "Ha" in popped_cards_dealer:
            dealer_hand -= 10
            print("Trekker fra 10 poeng fra dealer sine poeng siden summer er over 21 og dealer har et ess")
        elif dealer_hand > 21 and "Ca" in popped_cards_dealer:
            dealer_hand -= 10
            print("Trekker fra 10 poeng fra dealer sine poeng siden summer er over 21 og dealer har et ess")
        elif dealer_hand > 21 and "Da" in popped_cards_dealer:
            dealer_hand -= 10
            print("Trekker fra 10 poeng fra dealer sine poeng siden summer er over 21 og dealer har et ess")
        elif dealer_hand > 21 and "Sa" in popped_cards_dealer:
            dealer_hand -= 10
            print("Trekker fra 10 poeng fra dealer sine poeng siden summer er over 21 og dealer har et ess")
    else:
        print("\n"*1)
        print("{}, du har {} poeng".format(spiller.name, player_hand))
        print("Dealer har {} poeng".format(dealer_hand))


def spill():
    print("Velkommen til Black Jack!")
    player_info()
    
    
def gameplay():
    
        print("Du har {} credits igjen".format(spiller.credit))
        start_bet()
        if spiller.credit <= 0:
            print("Du har ikke credits igjen, takk for at du spilte Black Jack!")
        else:
            del_ut_kort_forste_gang()
            more_player_cards()
            dealer_pick_cards()
            print("\n"*1)
            win_condition()

if __name__ == '__main__':
	spill()
	spiller = Player(spiller_name, start_credit)
	while spiller.credit > 0:
		gameplay()
		popped_cards_dealer = []
		popped_cards_player = []
	else:
		print("Du har ikke penger igjen, takk for at du spilte Black Jack!")

	

