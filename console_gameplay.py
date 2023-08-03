from gameplay_utils.components import *
from gameplay_utils.challenges import *
from gameplay_utils.messages import Message

def game_loop():
    # Instantiate player, quests, locations, and boss
    player = Player("Vijay")
    quest1 = Quest("Divine Wisdom of Brahma", "Before you stands a wise rishi, his eyes twinkling with the knowledge of the cosmos. He challenges you to a contest of wisdom, posing riddles that would baffle even the sharpest minds.", player.gain_wisdom)
    quest2 = Quest("The Blessings of Vishnu", "In the distance, you see a village being attacked by a terrifying mythical beast. The beast's roars echo in your ears as the villagers cower in fear. Will you step forward to protect them?", player.gain_courage)
    quest3 = Quest("The Fury of Shiva", "The icy winds of Mount Kailash whip around you, stinging your skin and chilling your bones. In the face of this relentless cold, you must meditate and conquer your inner demons.", player.gain_selflessness)
    quest4 = Quest("The Asura Invasion", "Suddenly, your peaceful village is invaded by Mahakala's Asura warriors. They tear through the streets, causing chaos and destruction. It's time to put your training to use.", player.gain_strength)

    location1 = Location("Dandakaranya", quest1)
    location2 = Location("Vaikuntha", quest2)
    location3 = Location("Mount Kailash", quest3)
    location4 = Location("Your Village", quest4)
    locations = [location1, location2, location3, location4]

    boss = Boss("Mahakala", 100)
    messages = Message()
    messages.initial_message()

    # Main game loop
    while len(locations):
        print(f"{Color.DARKCYAN}Welcome {player.name}! You are the Veer Purusha, the prophesied hero who will restore balance to the cosmos.{Color.END}")
        print(f"Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")

        # Choose a location
        print("Where does your destiny lead you?")
        for i, location in enumerate(locations, 1):
            print(f"{i}. {location.name}")

        choice = int(input("Enter the number of your chosen destination: "))
        chosen_location = locations[choice-1]

        # Display location and quest
        print(f"\nYour journey brings you to {Color.GREEN}{chosen_location.name}{Color.END}.")

        # Challenge player and check for quest completion
        if chosen_location.name == 'Dandakaranya':
            messages.describe_bramha_quest()
            quest_completed = challenge_brahma(player)
        elif chosen_location.name == 'Vaikuntha':
            quest_completed = challenge_vishnu(player)
        elif chosen_location.name == 'Mount Kailash':
            quest_completed = challenge_shiva(player)
        elif chosen_location.name == 'Your Village':
            quest_completed = challenge_asura(player)

        if quest_completed:
            locations.remove(chosen_location)  # Remove completed location

    # Finally Fight boss
    fight_boss(player, boss)





if __name__ == '__main__':
    game_loop()