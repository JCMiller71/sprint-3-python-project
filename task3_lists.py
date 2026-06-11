game_names = []
for i in range(len(video_game_sales)):
    game_names.append(video_game_sales[i][NAME])
print(game_names)

video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

dataset_info = (21, 10,'Video Game Sales')
print (dataset_info) # metadata is immutable, and cannot be changed, so a tuple is more appropriate because it is also immutable.
