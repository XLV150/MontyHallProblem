def no_switch():
    counter_won = 0
    counter_loss = 0
    for i in range(1, 4):
        prize_door = i
        for x in range(1, 4):
            initial_pick = x
            if prize_door == initial_pick:
                counter_won += 1
            else:
                counter_loss += 1

    print(counter_won, "No switch Wins")
    print(counter_loss, "No switch Losses")

def switch():
    counter_won = 0
    counter_loss = 0
    for i in range(1, 4):
        prize_door = i
        for x in range(1, 4):
            initial_pick = x
            if prize_door == initial_pick:
                initial_pick = prize_door - initial_pick
                counter_loss += 1
            else:
                counter_won += 1
            initial_pick += 1

    print(counter_won, "Switch Wins")
    print(counter_loss, "Switch Losses")

no_switch()
print()
switch()