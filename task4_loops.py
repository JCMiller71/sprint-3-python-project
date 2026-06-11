for i in range(len(video_game_sales)):
    if video_game_sales[i][GLOBAL_SALES] > 25:
        print(f"{video_game_sales[i][NAME]},{video_game_sales[i][GLOBAL_SALES]}")

pre_2000_count=0
for game in video_game_sales:
    if game[YEAR]< 2000:
        pre_2000_count=pre_2000_count+1        
print(pre_2000_count)

na_total=0
jp_total=0
for sale in video_game_sales:
    na_total=na_total + sale[NA_SALES]
    jp_total=jp_total + sale[JP_SALES]
print(f"North America: {na_total}, Japan: {jp_total}")
if na_total > jp_total:
    print("North America had higher sales.")
elif na_total == jp_total:
    print("North America and Japan had equal sales.")
else:
    print("Japan had higher sales.")

nintendo_games=[]
for nin in video_game_sales:
    if nin[PUBLISHER] == 'Nintendo':
        nintendo_games.append(nin[NAME])
print(nintendo_games)
print (len(nintendo_games))
