
# The check_horse_winner function returns the following:
#
# - If only one player is left with fewer than 5 letters,
#   return "Player X wins!", where X is the index of the
#   player in the list (which could be 0).
# - If more than one player has fewer than 5 letters,
#   return "Players X, Y: keep playing!", where X, Y, and
#   potentially more numbers are the indices of all players
#   who have not yet been eliminated.
# - If no player has 5 letters, return "Everyone: keep
#   playing!"

def check_horse_winner(players):
        alive = [str(i) for (i, x) in enumerate(players) if len(x) != 5]
        if len(alive) == len(players):
                return 'Everyone: keep playing!'
        if len(alive) == 1:
                return 'Player ' + alive[0] + ' wins!'

        return 'Players ' + ', '.join(alive) + ': keep playing!'



print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))
