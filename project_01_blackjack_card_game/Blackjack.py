import random # to shuffle the decker prior to dealing

suits = ['Hearts' , 'Diamonds' , 'Spades' , 'Clubs']
ranks = ['Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Jack' , 'Queen' , 'King' , 'Ace' ]
values = {'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 , 'Six':6 , 'Seven':7 , 'Eight':8 , 'Nine':9 , 'Ten':10 , 'Jack':10 , 'Queen':10 , 'King':10 , 'Ace':11 }

playing = True

# creating card object
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


#creating deck object
class Deck():

    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # build card objects and add them to the list
        
    def __str__(self):

        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
# test_deck = Deck()
# print(test_deck)   

# setting up player's chips
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        

# function to take bets
def take_bet(chips):
    while True:
        try:    
            chips.bet = int(input("what is your bet?"))
        except:
            print("please try again")
        else:
            if chips.bet > chips.total:
                print("sorry, you do not have enough chips! you have: {}".format(chips.total))
            else:
                break

# distributing cards to each player
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # track aces
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

# function to display cards
def show_some(dealer,player):


    # show only one dealer hand
    print("Dealer's hand")
    print("one card hidden")
    print(dealer.cards[1])

    # show both player's cards
    print("Player's hand")
    for card in player.cards:
        print(card)

def show_all(player,dealer):    

    # show all dealer's cards
    print("\n dealer's hand: ")
    for card in dealer.cards:
        print(card)
    # calculate and display value
    print(f"value of dealer's hand is: {dealer.value}")

    # show all players cards
    print("\n player's hand: ")
    for card in player.cards:
        print(card)
    print(f"value of player's hand is: {player.value}")
    

# function for taking hits
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# function for prompting the player to hit or stand
def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("player stands. dealer is playing")

        else:
            print("please try again")
            continue
        break

# fucntions to handle end game scenarios
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    
    
            # Show all cards
            show_all(player_hand,dealer_hand)
        
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break