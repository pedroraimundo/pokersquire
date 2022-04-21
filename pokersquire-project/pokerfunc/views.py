from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def squire(request):

    # defining the POST data gathering on settings.html
    data = request.POST.items()

    # defining the lists and dictionaries to handle the setup data (players, blind, etc)
    context = dict([(key, value) for key, value in data])

    player_name_key = []
    player_name_value = []

    total_rounds = 0
    round_number_key = []
    round_number_value = []

    round_time_duration_key = []
    round_time_duration_value = []

    round_small_blind_key = []
    round_small_blind_value = []

    round_big_blind_key = []
    round_big_blind_value = []

    round_ante_key = []
    round_ante_value = []

    for key, value in context.items():
        if 'blind_duration_round_' in key:
            round_time_duration_key.append(key)
            round_time_duration_value.append(value)

    for key, value in context.items():
        if 'small_blind_value_' in key:
            round_small_blind_key.append(key)
            round_small_blind_value.append(value)

    for key, value in context.items():
        if 'big_blind_value_' in key:
            round_big_blind_key.append(key)
            round_big_blind_value.append(value)

    for key, value in context.items():
        if 'ante_value_' in key:
            round_ante_key.append(key)
            round_ante_value.append(value)

    for key, value in context.items():
        if 'player_name_' in key:
            player_name_key.append(key)
            player_name_value.append(value)

    # creating a dictionary for each property of the round setup
    round_duration_dict = dict(zip(round_time_duration_key, round_time_duration_value))
    round_small_blind_dict = dict(zip(round_small_blind_key, round_small_blind_value))
    round_big_blind_dict = dict(zip(round_big_blind_key, round_big_blind_value))
    round_ante_value_dict = dict(zip(round_ante_key, round_ante_value))
    player_name_dict = dict(zip(player_name_key, player_name_value))

    # determining the number of rounds without relying on context
    total_rounds = (len(round_small_blind_dict))

    # starting loop from 1 instead of 0
    for i in (n + 1 for n in range(total_rounds)):
        round_number_key.append("round_number_" + str(i))
        round_number_value.append(str(i))

    round_number_dict = dict(zip(round_number_key, round_number_value))

    # merging dictionaries to be passed as context
    match_setup_dict = round_number_dict | round_duration_dict | round_small_blind_dict | round_big_blind_dict | round_ante_value_dict | player_name_dict

    for key, value in match_setup_dict.items():
        print(key, ':', value)

    return render(request, 'squire.html', {'match_setup_dict': match_setup_dict})


def settings(request):
    return render(request, 'settings.html')


def results(request):
    return render(request, 'results.html')
