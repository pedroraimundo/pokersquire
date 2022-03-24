from django.shortcuts import render, get_object_or_404


def squire(request):

    player_name = request.GET['player_name']

    context = {
        "player_name": player_name
    }
    return render(request, 'squire.html', context)


def settings(request):

    # blind setup functionality
    blind_duration = ""
    small_blind_value = ""
    big_blind_value = ""
    ante_value = ""
    round_number = ""
    total_rounds = ""

    blind_data = {
        "blind_duration": blind_duration,
        "small_blind_value": small_blind_value,
        "big_blind_value": big_blind_value,
        "ante_value": ante_value,
        "round_number": round_number,
        "total_rounds": total_rounds
    }

    # player setup functionality
    player_name = "Pedro"
    total_players = ""

    player_data = {
        "player_name": player_name,
        "total_players": total_players
    }

    # context dictionary to be used to pass data to the settings page
    context = {
        'player_data': player_data,
        "blind_data": blind_data
    }

    return render(request, 'settings.html', context)


def results(request):
    return render(request, 'results.html')
