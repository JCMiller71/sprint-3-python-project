def calculate_total_sales(game):
    sum_game = game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
    return sum_game
wii_sports = calculate_total_sales(video_game_sales[0])
print(wii_sports)

def filter_by_genre(data, genre='Platform'):
    result = [] 
    for game in data:
        if game[GENRE] == genre:
            result.append(game)
    return result
Racing = filter_by_genre(video_game_sales, 'Racing')
print(Racing)
Platform = filter_by_genre(video_game_sales, )
print(Platform)

def get_summary(game):
    name = game[NAME]
    year = game[YEAR]
    genre = game[GENRE]
    sales = game[GLOBAL_SALES]
    return f"{name} ({year}) - {genre} - ${sales}M"
for x in video_game_sales:
    game_sum = get_summary(x)
    print(game_sum)
