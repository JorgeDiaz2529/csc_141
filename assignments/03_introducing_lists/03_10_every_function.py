favorite_games = ["Celeste","Hollow Knight","Ib","Deltarune"]

print(favorite_games)

favorite_games.append("OneShot")
favorite_games.insert(1, "Stardew Valley")
favorite_games.pop()

print(favorite_games)

print(sorted(favorite_games))
print(sorted(favorite_games,reverse=True))
favorite_games.reverse()

favorite_games.sort()
print(favorite_games)
favorite_games.sort(reverse=True)
print(favorite_games)

del favorite_games[0]

print(f"Jorge has {len(favorite_games)} favorite games")