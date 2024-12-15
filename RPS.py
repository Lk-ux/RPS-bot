import itertools

def player(prev_opponent_play,
          opponent_history=[],
          play_order=[{}]):  # Initialize as an empty dictionary

    if not play_order[0]:  # Check if play_order is empty
        # Generate all combinations of 5 moves and add to play_order
        for combination in itertools.product('RPS', repeat=5):
            play_order[0]["".join(combination)] = 0

    if not prev_opponent_play:
        prev_opponent_play = 'S'
    opponent_history.append(prev_opponent_play)

    last_five = "".join(opponent_history[-5:])  # Consider last 5 moves
    if len(last_five) == 5:
        play_order[0][last_five] += 1  

    last_four = "".join(opponent_history[-4:])
    potential_plays = [
        last_four + "R", 
        last_four + "P",
        last_four + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    if sub_order:  
        prediction = max(sub_order, key=sub_order.get)[-1:]
    else:
        prediction = 'R'  

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
