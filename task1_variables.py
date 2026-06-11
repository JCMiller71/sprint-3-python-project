total_games = len(video_game_sales)
print(total_games)

sum_glob = 0
for i in video_game_sales:
    sum_glob = sum_glob + i[GLOBAL_SALES]

avg_global_sales = sum_glob / total_games
print(avg_global_sales) # calculates average global sales across all 20 games

top_game_share = 82.74/sum_glob * 100
print(top_game_share)
