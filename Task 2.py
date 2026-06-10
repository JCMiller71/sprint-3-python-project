game_name = video_game_sales[4][NAME]
print(game_name[:7])

for i in messy_names:
    print(i.lower().strip())

name = video_game_sales[0][1]
year = video_game_sales[0][3]
global_sales = video_game_sales[0][9]
print(f"#1 Best Seller: {name} ({year}) - ${global_sales}M global sales")