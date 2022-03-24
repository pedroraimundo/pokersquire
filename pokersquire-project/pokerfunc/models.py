from django.db import models
import math


class Stats(models.Model):
    summary = models.CharField(max_length=200)


# The timer function will take the parameters for the duration of each blind
def timer():
    countdown_timer = ""

    number_of_blinds = int(1)  # value received from game settings
    blinds_dictionary = {"data": []}

    def fill_blind_data():
        for i in range(number_of_blinds):
            each_blind = {}
            each_blind["blind_number"] = i + 1
            each_blind["blind_time"] = 1  # value received from game settings
            each_blind["blind_value"] = 1  # value received from game settings
            add_blinds(each_blind)

    def add_blinds(each_blind):
        blinds_dictionary["data"].append(each_blind)

    fill_blind_data()
    print(blinds_dictionary)

    return countdown_timer


# The timer_controls are responsible to deal with the 'play', 'pause', 'blind forward', 'blind backward'
def timer_controls():
    controls = ""
    return controls


# process_player_data takes care of the array of player data being entered pre-game
def process_player_data():

    player_name = ""
    player_rebuys = ""

    player_data = {
        "name": player_name,
        "rebuys": player_rebuys
    }

    return player_data


# process_game_data processes all the parameters from the game (price of each blind, number of buy-ins, etc.)
def process_game_data():
    game_data = ""
    return game_data


# calculate_payouts calculates the sum of buy-ins + rebuys and calculates payout for top 3 players.
def calculate_payouts():
    prize_pool = int(0)
    custom_ratio_flag = bool(True)

    payout_data = [4, 4, 4, 10, 8]
    helper_list = []
    payout_ratio = [2]

    custom_ratio_1 = 50
    custom_ratio_2 = 30
    custom_ratio_3 = 20

    # checks if there's a custom ratio flag and initializes the ratio split
    if not custom_ratio_flag:
        payout_ratio = [0.6, 0.3, 0.1]
    else:
        custom_ratio_1 *= 0.01
        custom_ratio_2 *= 0.01
        custom_ratio_3 *= 0.01
        payout_ratio = [custom_ratio_1, custom_ratio_2, custom_ratio_3]

    # sums up the total prize pool of all players
    prize_pool = sum(payout_data)

    # calculate prizes based on the ratio provided - numbers are rounded
    first_prize = round((prize_pool * payout_ratio[0]))
    second_prize = round((prize_pool * payout_ratio[1]))
    third_prize = round((prize_pool * payout_ratio[2]))

    return prize_pool, first_prize, second_prize, third_prize
