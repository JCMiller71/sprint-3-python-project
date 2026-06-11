sales_by_genre={}
for sale in video_game_sales:
    if sale[GENRE] in sales_by_genre:
       sales_by_genre[sale[GENRE]] += sales_by_genre[sale[GENRE]]
    else:
        sales_by_genre[sale[GENRE]] = sale[GLOBAL_SALES]
print(sales_by_genre)

games_per_publisher = {}
for game in video_game_sales:
    if game[PUBLISHER] in games_per_publisher:
        games_per_publisher[game[PUBLISHER]]=games_per_publisher[game[PUBLISHER]]+1
    else:
        games_per_publisher[game[PUBLISHER]] = 1
print(games_per_publisher)

top_game={
    'name': video_game_sales[0][NAME],
    'year': video_game_sales[0][YEAR],
    'genre': video_game_sales[0][GENRE],
    'publisher': video_game_sales[0][PUBLISHER],
    'global_sales': video_game_sales[0][GLOBAL_SALES]
}
for key, value in top_game.items():
    print(f"{key}: {value}")
