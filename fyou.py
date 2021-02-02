import os
import random

short_description = {
"1":"",
"2":"Two for you",
"3":"Three for me",
"4":"Four to the floor",
"5":"Five for the guys",
"6":"Six for the chicks",
"7":"Seven to heaven",
"8":"Eight pick a date",
"9":"",
"10":"",
"11":"",
"12":"",
"13":"",
}

long_description = {

}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

card_deck = {}
for i in range(13):
    card_deck.update({str(i+1):4})

while(1):
    junk = input("Appuyer sur enter pour la prochaine carte")
    keepLooking = True
    while(keepLooking):
        card = random.randint(1,13)
        if card_deck[str(card)] != 0:
            card_deck.update({str(card):card_deck[str(card)]-1})
            keepLooking = False
    if card == 1:
        print("