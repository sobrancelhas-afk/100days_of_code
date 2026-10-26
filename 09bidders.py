def clear_screen():
    print('\n'*100)

print("Let's bid mu'ffers!\n")

def enter_auct(current_bids):

    auctioner = input("Who's in for the game?\n")
    value = int(input("how mouche $?\n"))

    current_bids[auctioner] = value

    end = input("If finished type y:\n")
    if end == "y":
        return False, current_bids
    else:
        return True, current_bids

add_participants = True
auction={}

while add_participants:
    add_participants, auction = enter_auct(auction)


print(max(auction, key=auction.get))