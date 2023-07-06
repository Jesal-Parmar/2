def select_team_players():
    available_players = [
        "Lionel Messi",
        "Cristiano Ronaldo",
        "Neymar Jr.",
        "Kevin De Bruyne",
        "Virgil van Dijk",
        "Kylian Mbappe",
        "Robert Lewandowski",
        "Luka Modric",
        "Sergio Ramos",
        "Mohamed Salah"
    ]

    selected_players = []

    print("Welcome to the FIFA Team Player Selection Program!")
    print("Please select 5 players from the list below:")

    for i, player in enumerate(available_players):
        print(f"{i+1}. {player}")

    while len(selected_players) < 5:
        selection = input("Enter the number corresponding to the player you want to select (or 'q' to quit): ")

        if selection.lower() == 'q':
            break

        try:
            index = int(selection) - 1
            if 0 <= index < len(available_players):
                player = available_players[index]
                if player not in selected_players:
                    selected_players.append(player)
                    print(f"{player} has been selected!")
                else:
                    print("This player has already been selected. Please choose another player.")
            else:
                print("Invalid input. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number from the list.")

    print("Selected players:")
    for i, player in enumerate(selected_players):
        print(f"{i+1}. {player}")


select_team_players()
