players = [
    ("Alice", 850), ("Bob", 1200), ("Charlie", 450),
    ("Diana", 990), ("Eve", 1200), ("Frank", 750)
]
sort=sorted(players,key=lambda x:x[1], reverse=True)
print("    LEADERBOARD")
for i,(name,score) in enumerate(sort,start=1):
    print(f"{i}. {name:<10} {score}")
