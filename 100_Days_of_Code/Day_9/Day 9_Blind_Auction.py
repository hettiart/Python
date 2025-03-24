import art
print (art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("what is your name: ")
    price = int(input("what is your bidding price: "))
    bids[name] = price
    next_user = input("Are there are other users need to bid? type Yes or No \n").lower()

# TODO-4: Compare bids in dictionary
    if next_user == "yes":
        print("\n"*100)
    else:
        print(max(bids, key=bids.get))
        continue_bidding = False