#make a list of people attending game night
gamers = []
#populate the gamers list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Incorrect data, must include keys name and availability")
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#create a frequency table which correlates day of the week w/ gamer availability in gamers list
def build_daily_frequency_table():
    build_daily_frequency_table_dict = {
        "Monday": 0, 
        "Tuesday": 0, 
        "Wednesday": 0, 
        "Thursday": 0, 
        "Friday": 0, 
        "Saturday": 0, 
        "Sunday": 0
    }
    return build_daily_frequency_table_dict
count_availability = build_daily_frequency_table()

#available_frequency is a frequency table
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1
calculate_availability(gamers, count_availability)
print(count_availability)
#prints {'Monday': 5, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 6, 'Friday': 3, 'Saturday': 4, 'Sunday': 3}
#best day is Thursday

#availability_table must be a dictionary
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_availability = availability
            best_day = day
    return best_day
game_night = find_best_night(count_availability)
print(game_night)
#should print Thursday

#make a list of the people available on a given night
def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer["availability"]]
        
attending_game_night = available_on_night(gamers, "Thursday")
print(attending_game_night)

#generate form email text alerting gamers of game night
form_email = """
Dear {name}:

The best comic & gaming store in town, the Sorcery Society, is holding a weekly game night! Based on everyone's preferences, we've decided on {day_of_week}. This week, we will be playing "{game}", so get excited!

Be there or be square, losers.
- The Sorcery Society
"""
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer["name"], day_of_week = day, game = game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")
#should email Thomas, Michelle, Stephen, Joanne, Crystal, and James

#we're gonna try to have a second game night of the week
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]
print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)
print(second_night)
#should print Monday
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")
#should email Kimberly, Joyce, Joanne, Latasha, and Michel
