import random

'''def player(prev_opponent_play,
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
    return ideal_response[prediction]'''
def player(prev_opponent_play,
          history=[],  # Single history list
          play_order=[{'RRRRRR': 0, 'RRRRRP': 0, 'RRRRRS': 0, 'RRRRPR': 0, 'RRRRPP': 0, 'RRRRPS': 0, 'RRRRSR': 0, 'RRRRSP': 0, 'RRRRSS': 0, 'RRRPRR': 0, 'RRRPRP': 0, 'RRRPRS': 0, 'RRRPPR': 0, 'RRRPPP': 0, 'RRRPPS': 0, 'RRRPSR': 0, 'RRRPSP': 0, 'RRRPSS': 0, 'RRRSRR': 0, 'RRRSRP': 0, 'RRRSRS': 0, 'RRRSPR': 0, 'RRRSPP': 0, 'RRRSPS': 0, 'RRRSSR': 0, 'RRRSSP': 0, 'RRRSSS': 0, 'RRPRRR': 0, 'RRPRRP': 0, 'RRPRRS': 0, 'RRPRPR': 0, 'RRPRPP': 0, 'RRPRPS': 0, 'RRPRSR': 0, 'RRPRSP': 0, 'RRPRSS': 0, 'RRPPRR': 0, 'RRPPRP': 0, 'RRPPRS': 0, 'RRPPPR': 0, 'RRPPPP': 0, 'RRPPPS': 0, 'RRPPSR': 0, 'RRPPSP': 0, 'RRPPSS': 0, 'RRPSRR': 0, 'RRPSRP': 0, 'RRPSRS': 0, 'RRPSPR': 0, 'RRPSPP': 0, 'RRPSPS': 0, 'RRPSSR': 0, 'RRPSSP': 0, 'RRPSSS': 0, 'RRSRRR': 0, 'RRSRRP': 0, 'RRSRRS': 0, 'RRSRPR': 0, 'RRSRPP': 0, 'RRSRPS': 0, 'RRSRSR': 0, 'RRSRSP': 0, 'RRSRSS': 0, 'RRSPRR': 0, 'RRSPRP': 0, 'RRSPRS': 0, 'RRSPPR': 0, 'RRSPPP': 0, 'RRSPPS': 0, 'RRSPSR': 0, 'RRSPSP': 0, 'RRSPSS': 0, 'RRSSRR': 0, 'RRSSRP': 0, 'RRSSRS': 0, 'RRSSPR': 0, 'RRSSPP': 0, 'RRSSPS': 0, 'RRSSSR': 0, 'RRSSSP': 0, 'RRSSSS': 0, 'RPRRRR': 0, 'RPRRRP': 0, 'RPRRRS': 0, 'RPRRPR': 0, 'RPRRPP': 0, 'RPRRPS': 0, 'RPRRSR': 0, 'RPRRSP': 0, 'RPRRSS': 0, 'RPRPRR': 0, 'RPRPRP': 0, 'RPRPRS': 0, 'RPRPPR': 0, 'RPRPPP': 0, 'RPRPPS': 0, 'RPRPSR': 0, 'RPRPSP': 0, 'RPRPSS': 0, 'RPRSRR': 0, 'RPRSRP': 0, 'RPRSRS': 0, 'RPRSPR': 0, 'RPRSPP': 0, 'RPRSPS': 0, 'RPRSSR': 0, 'RPRSSP': 0, 'RPRSSS': 0, 'RPPRRR': 0, 'RPPRRP': 0, 'RPPRRS': 0, 'RPPRPR': 0, 'RPPRPP': 0, 'RPPRPS': 0, 'RPPRSR': 0, 'RPPRSP': 0, 'RPPRSS': 0, 'RPPPRR': 0, 'RPPPRP': 0, 'RPPPRS': 0, 'RPPPPR': 0, 'RPPPPP': 0, 'RPPPPS': 0, 'RPPPSR': 0, 'RPPPSP': 0, 'RPPPSS': 0, 'RPPSRR': 0, 'RPPSRP': 0, 'RPPSRS': 0, 'RPPSPR': 0, 'RPPSPP': 0, 'RPPSPS': 0, 'RPPSSR': 0, 'RPPSSP': 0, 'RPPSSS': 0, 'RPSRRR': 0, 'RPSRRP': 0, 'RPSRRS': 0, 'RPSRPR': 0, 'RPSRPP': 0, 'RPSRPS': 0, 'RPSRSR': 0, 'RPSRSP': 0, 'RPSRSS': 0, 'RPSPRR': 0, 'RPSPRP': 0, 'RPSPRS': 0, 'RPSPPR': 0, 'RPSPPP': 0, 'RPSPPS': 0, 'RPSPSR': 0, 'RPSPSP': 0, 'RPSPSS': 0, 'RPSSRR': 0, 'RPSSRP': 0, 'RPSSRS': 0, 'RPSSPR': 0, 'RPSSPP': 0, 'RPSSPS': 0, 'RPSSSR': 0, 'RPSSSP': 0, 'RPSSSS': 0, 'RSRRRR': 0, 'RSRRRP': 0, 'RSRRRS': 0, 'RSRRPR': 0, 'RSRRPP': 0, 'RSRRPS': 0, 'RSRRSR': 0, 'RSRRSP': 0, 'RSRRSS': 0, 'RSRPRR': 0, 'RSRPRP': 0, 'RSRPRS': 0, 'RSRPPR': 0, 'RSRPPP': 0, 'RSRPPS': 0, 'RSRPSR': 0, 'RSRPSP': 0, 'RSRPSS': 0, 'RSRSRR': 0, 'RSRSRP': 0, 'RSRSRS': 0, 'RSRSPR': 0, 'RSRSPP': 0, 'RSRSPS': 0, 'RSRSSR': 0, 'RSRSSP': 0, 'RSRSSS': 0, 'RSPRRR': 0, 'RSPRRP': 0, 'RSPRRS': 0, 'RSPRPR': 0, 'RSPRPP': 0, 'RSPRPS': 0, 'RSPRSR': 0, 'RSPRSP': 0, 'RSPRSS': 0, 'RSPPRR': 0, 'RSPPRP': 0, 'RSPPRS': 0, 'RSPPPR': 0, 'RSPPPP': 0, 'RSPPPS': 0, 'RSPPSR': 0, 'RSPPSP': 0, 'RSPPSS': 0, 'RSPSRR': 0, 'RSPSRP': 0, 'RSPSRS': 0, 'RSPSPR': 0, 'RSPSPP': 0, 'RSPSPS': 0, 'RSPSSR': 0, 'RSPSSP': 0, 'RSPSSS': 0, 'RSSRRR': 0, 'RSSRRP': 0, 'RSSRRS': 0, 'RSSRPR': 0, 'RSSRPP': 0, 'RSSRPS': 0, 'RSSRSR': 0, 'RSSRSP': 0, 'RSSRSS': 0, 'RSSPRR': 0, 'RSSPRP': 0, 'RSSPRS': 0, 'RSSPPR': 0, 'RSSPPP': 0, 'RSSPPS': 0, 'RSSPSR': 0, 'RSSPSP': 0, 'RSSPSS': 0, 'RSSSRR': 0, 'RSSSRP': 0, 'RSSSRS': 0, 'RSSSPR': 0, 'RSSSPP': 0, 'RSSSPS': 0, 'RSSSSR': 0, 'RSSSSP': 0, 'RSSSSS': 0, 'PRRRRR': 0, 'PRRRRP': 0, 'PRRRRS': 0, 'PRRRPR': 0, 'PRRRPP': 0, 'PRRRPS': 0, 'PRRRSR': 0, 'PRRRSP': 0, 'PRRRSS': 0, 'PRRPRR': 0, 'PRRPRP': 0, 'PRRPRS': 0, 'PRRPPR': 0, 'PRRPPP': 0, 'PRRPPS': 0, 'PRRPSR': 0, 'PRRPSP': 0, 'PRRPSS': 0, 'PRRSRR': 0, 'PRRSRP': 0, 'PRRSRS': 0, 'PRRSPR': 0, 'PRRSPP': 0, 'PRRSPS': 0, 'PRRSSR': 0, 'PRRSSP': 0, 'PRRSSS': 0, 'PRPRRR': 0, 'PRPRRP': 0, 'PRPRRS': 0, 'PRPRPR': 0, 'PRPRPP': 0, 'PRPRPS': 0, 'PRPRSR': 0, 'PRPRSP': 0, 'PRPRSS': 0, 'PRPPRR': 0, 'PRPPRP': 0, 'PRPPRS': 0, 'PRPPPR': 0, 'PRPPPP': 0, 'PRPPPS': 0, 'PRPPSR': 0, 'PRPPSP': 0, 'PRPPSS': 0, 'PRPSRR': 0, 'PRPSRP': 0, 'PRPSRS': 0, 'PRPSPR': 0, 'PRPSPP': 0, 'PRPSPS': 0, 'PRPSSR': 0, 'PRPSSP': 0, 'PRPSSS': 0, 'PRSRRR': 0, 'PRSRRP': 0, 'PRSRRS': 0, 'PRSRPR': 0, 'PRSRPP': 0, 'PRSRPS': 0, 'PRSRSR': 0, 'PRSRSP': 0, 'PRSRSS': 0, 'PRSPRR': 0, 'PRSPRP': 0, 'PRSPRS': 0, 'PRSPPR': 0, 'PRSPPP': 0, 'PRSPPS': 0, 'PRSPSR': 0, 'PRSPSP': 0, 'PRSPSS': 0, 'PRSSRR': 0, 'PRSSRP': 0, 'PRSSRS': 0, 'PRSSPR': 0, 'PRSSPP': 0, 'PRSSPS': 0, 'PRSSSR': 0, 'PRSSSP': 0, 'PRSSSS': 0, 'PPRRRR': 0, 'PPRRRP': 0, 'PPRRRS': 0, 'PPRRPR': 0, 'PPRRPP': 0, 'PPRRPS': 0, 'PPRRSR': 0, 'PPRRSP': 0, 'PPRRSS': 0, 'PPRPRR': 0, 'PPRPRP': 0, 'PPRPRS': 0, 'PPRPPR': 0, 'PPRPPP': 0, 'PPRPPS': 0, 'PPRPSR': 0, 'PPRPSP': 0, 'PPRPSS': 0, 'PPRSRR': 0, 'PPRSRP': 0, 'PPRSRS': 0, 'PPRSPR': 0, 'PPRSPP': 0, 'PPRSPS': 0, 'PPRSSR': 0, 'PPRSSP': 0, 'PPRSSS': 0, 'PPPRRR': 0, 'PPPRRP': 0, 'PPPRRS': 0, 'PPPRPR': 0, 'PPPRPP': 0, 'PPPRPS': 0, 'PPPRSR': 0, 'PPPRSP': 0, 'PPPRSS': 0, 'PPPPRR': 0, 'PPPPRP': 0, 'PPPPRS': 0, 'PPPPPR': 0, 'PPPPPP': 0, 'PPPPPS': 0, 'PPPPSR': 0, 'PPPPSP': 0, 'PPPPSS': 0, 'PPPSRR': 0, 'PPPSRP': 0, 'PPPSRS': 0, 'PPPSPR': 0, 'PPPSPP': 0, 'PPPSPS': 0, 'PPPSSR': 0, 'PPPSSP': 0, 'PPPSSS': 0, 'PPSRRR': 0, 'PPSRRP': 0, 'PPSRRS': 0, 'PPSRPR': 0, 'PPSRPP': 0, 'PPSRPS': 0, 'PPSRSR': 0, 'PPSRSP': 0, 'PPSRSS': 0, 'PPSPRR': 0, 'PPSPRP': 0, 'PPSPRS': 0, 'PPSPPR': 0, 'PPSPPP': 0, 'PPSPPS': 0, 'PPSPSR': 0, 'PPSPSP': 0, 'PPSPSS': 0, 'PPSSRR': 0, 'PPSSRP': 0, 'PPSSRS': 0, 'PPSSPR': 0, 'PPSSPP': 0, 'PPSSPS': 0, 'PPSSSR': 0, 'PPSSSP': 0, 'PPSSSS': 0, 'PSRRRR': 0, 'PSRRRP': 0, 'PSRRRS': 0, 'PSRRPR': 0, 'PSRRPP': 0, 'PSRRPS': 0, 'PSRRSR': 0, 'PSRRSP': 0, 'PSRRSS': 0, 'PSRPRR': 0, 'PSRPRP': 0, 'PSRPRS': 0, 'PSRPPR': 0, 'PSRPPP': 0, 'PSRPPS': 0, 'PSRPSR': 0, 'PSRPSP': 0, 'PSRPSS': 0, 'PSRSRR': 0, 'PSRSRP': 0, 'PSRSRS': 0, 'PSRSPR': 0, 'PSRSPP': 0, 'PSRSPS': 0, 'PSRSSR': 0, 'PSRSSP': 0, 'PSRSSS': 0, 'PSPRRR': 0, 'PSPRRP': 0, 'PSPRRS': 0, 'PSPRPR': 0, 'PSPRPP': 0, 'PSPRPS': 0, 'PSPRSR': 0, 'PSPRSP': 0, 'PSPRSS': 0, 'PSPPRR': 0, 'PSPPRP': 0, 'PSPPRS': 0, 'PSPPPR': 0, 'PSPPPP': 0, 'PSPPPS': 0, 'PSPPSR': 0, 'PSPPSP': 0, 'PSPPSS': 0, 'PSPSRR': 0, 'PSPSRP': 0, 'PSPSRS': 0, 'PSPSPR': 0, 'PSPSPP': 0, 'PSPSPS': 0, 'PSPSSR': 0, 'PSPSSP': 0, 'PSPSSS': 0, 'PSSRRR': 0, 'PSSRRP': 0, 'PSSRRS': 0, 'PSSRPR': 0, 'PSSRPP': 0, 'PSSRPS': 0, 'PSSRSR': 0, 'PSSRSP': 0, 'PSSRSS': 0, 'PSSPRR': 0, 'PSSPRP': 0, 'PSSPRS': 0, 'PSSPPR': 0, 'PSSPPP': 0, 'PSSPPS': 0, 'PSSPSR': 0, 'PSSPSP': 0, 'PSSPSS': 0, 'PSSSRR': 0, 'PSSSRP': 0, 'PSSSRS': 0, 'PSSSPR': 0, 'PSSSPP': 0, 'PSSSPS': 0, 'PSSSSR': 0, 'PSSSSP': 0, 'PSSSSS': 0, 'SRRRRR': 0, 'SRRRRP': 0, 'SRRRRS': 0, 'SRRRPR': 0, 'SRRRPP': 0, 'SRRRPS': 0, 'SRRRSR': 0, 'SRRRSP': 0, 'SRRRSS': 0, 'SRRPRR': 0, 'SRRPRP': 0, 'SRRPRS': 0, 'SRRPPR': 0, 'SRRPPP': 0, 'SRRPPS': 0, 'SRRPSR': 0, 'SRRPSP': 0, 'SRRPSS': 0, 'SRRSRR': 0, 'SRRSRP': 0, 'SRRSRS': 0, 'SRRSPR': 0, 'SRRSPP': 0, 'SRRSPS': 0, 'SRRSSR': 0, 'SRRSSP': 0, 'SRRSSS': 0, 'SRPRRR': 0, 'SRPRRP': 0, 'SRPRRS': 0, 'SRPRPR': 0, 'SRPRPP': 0, 'SRPRPS': 0, 'SRPRSR': 0, 'SRPRSP': 0, 'SRPRSS': 0, 'SRPPRR': 0, 'SRPPRP': 0, 'SRPPRS': 0, 'SRPPPR': 0, 'SRPPPP': 0, 'SRPPPS': 0, 'SRPPSR': 0, 'SRPPSP': 0, 'SRPPSS': 0, 'SRPSRR': 0, 'SRPSRP': 0, 'SRPSRS': 0, 'SRPSPR': 0, 'SRPSPP': 0, 'SRPSPS': 0, 'SRPSSR': 0, 'SRPSSP': 0, 'SRPSSS': 0, 'SRSRRR': 0, 'SRSRRP': 0, 'SRSRRS': 0, 'SRSRPR': 0, 'SRSRPP': 0, 'SRSRPS': 0, 'SRSRSR': 0, 'SRSRSP': 0, 'SRSRSS': 0, 'SRSPRR': 0, 'SRSPRP': 0, 'SRSPRS': 0, 'SRSPPR': 0, 'SRSPPP': 0, 'SRSPPS': 0, 'SRSPSR': 0, 'SRSPSP': 0, 'SRSPSS': 0, 'SRSSRR': 0, 'SRSSRP': 0, 'SRSSRS': 0, 'SRSSPR': 0, 'SRSSPP': 0, 'SRSSPS': 0, 'SRSSSR': 0, 'SRSSSP': 0, 'SRSSSS': 0, 'SPRRRR': 0, 'SPRRRP': 0, 'SPRRRS': 0, 'SPRRPR': 0, 'SPRRPP': 0, 'SPRRPS': 0, 'SPRRSR': 0, 'SPRRSP': 0, 'SPRRSS': 0, 'SPRPRR': 0, 'SPRPRP': 0, 'SPRPRS': 0, 'SPRPPR': 0, 'SPRPPP': 0, 'SPRPPS': 0, 'SPRPSR': 0, 'SPRPSP': 0, 'SPRPSS': 0, 'SPRSRR': 0, 'SPRSRP': 0, 'SPRSRS': 0, 'SPRSPR': 0, 'SPRSPP': 0, 'SPRSPS': 0, 'SPRSSR': 0, 'SPRSSP': 0, 'SPRSSS': 0, 'SPPRRR': 0, 'SPPRRP': 0, 'SPPRRS': 0, 'SPPRPR': 0, 'SPPRPP': 0, 'SPPRPS': 0, 'SPPRSR': 0, 'SPPRSP': 0, 'SPPRSS': 0, 'SPPPRR': 0, 'SPPPRP': 0, 'SPPPRS': 0, 'SPPPPR': 0, 'SPPPPP': 0, 'SPPPPS': 0, 'SPPPSR': 0, 'SPPPSP': 0, 'SPPPSS': 0, 'SPPSRR': 0, 'SPPSRP': 0, 'SPPSRS': 0, 'SPPSPR': 0, 'SPPSPP': 0, 'SPPSPS': 0, 'SPPSSR': 0, 'SPPSSP': 0, 'SPPSSS': 0, 'SPSRRR': 0, 'SPSRRP': 0, 'SPSRRS': 0, 'SPSRPR': 0, 'SPSRPP': 0, 'SPSRPS': 0, 'SPSRSR': 0, 'SPSRSP': 0, 'SPSRSS': 0, 'SPSPRR': 0, 'SPSPRP': 0, 'SPSPRS': 0, 'SPSPPR': 0, 'SPSPPP': 0, 'SPSPPS': 0, 'SPSPSR': 0, 'SPSPSP': 0, 'SPSPSS': 0, 'SPSSRR': 0, 'SPSSRP': 0, 'SPSSRS': 0, 'SPSSPR': 0, 'SPSSPP': 0, 'SPSSPS': 0, 'SPSSSR': 0, 'SPSSSP': 0, 'SPSSSS': 0, 'SSRRRR': 0, 'SSRRRP': 0, 'SSRRRS': 0, 'SSRRPR': 0, 'SSRRPP': 0, 'SSRRPS': 0, 'SSRRSR': 0, 'SSRRSP': 0, 'SSRRSS': 0, 'SSRPRR': 0, 'SSRPRP': 0, 'SSRPRS': 0, 'SSRPPR': 0, 'SSRPPP': 0, 'SSRPPS': 0, 'SSRPSR': 0, 'SSRPSP': 0, 'SSRPSS': 0, 'SSRSRR': 0, 'SSRSRP': 0, 'SSRSRS': 0, 'SSRSPR': 0, 'SSRSPP': 0, 'SSRSPS': 0, 'SSRSSR': 0, 'SSRSSP': 0, 'SSRSSS': 0, 'SSPRRR': 0, 'SSPRRP': 0, 'SSPRRS': 0, 'SSPRPR': 0, 'SSPRPP': 0, 'SSPRPS': 0, 'SSPRSR': 0, 'SSPRSP': 0, 'SSPRSS': 0, 'SSPPRR': 0, 'SSPPRP': 0, 'SSPPRS': 0, 'SSPPPR': 0, 'SSPPPP': 0, 'SSPPPS': 0, 'SSPPSR': 0, 'SSPPSP': 0, 'SSPPSS': 0, 'SSPSRR': 0, 'SSPSRP': 0, 'SSPSRS': 0, 'SSPSPR': 0, 'SSPSPP': 0, 'SSPSPS': 0, 'SSPSSR': 0, 'SSPSSP': 0, 'SSPSSS': 0, 'SSSRRR': 0, 'SSSRRP': 0, 'SSSRRS': 0, 'SSSRPR': 0, 'SSSRPP': 0, 'SSSRPS': 0, 'SSSRSR': 0, 'SSSRSP': 0, 'SSSRSS': 0, 'SSSPRR': 0, 'SSSPRP': 0, 'SSSPRS': 0, 'SSSPPR': 0, 'SSSPPP': 0, 'SSSPPS': 0, 'SSSPSR': 0, 'SSSPSP': 0, 'SSSPSS': 0, 'SSSSRR': 0, 'SSSSRP': 0, 'SSSSRS': 0, 'SSSSPR': 0, 'SSSSPP': 0, 'SSSSPS': 0, 'SSSSSR': 0, 'SSSSSP': 0, 'SSSSSS': 0}
]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    history.append(prev_opponent_play)  # Add opponent's move to history

    # Assume your bot's move is added to history after each round 
    # like this: history.append(my_bot_move)

    last_six = "".join(history[-6:])  # Get the last 4 moves

    if len(last_six) == 6:
        play_order[0][last_six] += 1  # Update 4-move frequency

    potential_plays = [
        "".join(history[-5:]) + "R",  # Potential 4-move
        "".join(history[-5:]) + "P",  # Potential 4-move
        "".join(history[-5:]) + "S",  # Potential 4-move
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get, default='R')[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    move = ideal_response[prediction]
    return move