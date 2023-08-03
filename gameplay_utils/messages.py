from gameplay_utils.components import Color

class Message:
    def __init__(self) -> None:
        pass
    def initial_message(self):
        print(f"{Color.GREEN}The cosmos is in peril. The balance between good and evil, which has been maintained for eons, has been disrupted. The mighty Asura King, Mahakala, has obtained a powerful boon from Lord Brahma. Now, he seeks to overthrow the cosmic order, plunging all realms - Swargaloka (heaven), Prithvi (earth), and Patala (underworld) - into chaos. The gods are losing their powers, unable to stop the reign of the Asura King.{Color.END}")
        print()
        print(f"{Color.GREEN}You are an ordinary human, chosen by destiny, named Vijay. A secret prophecy has indicated that a human, the Veer Purusha, will rise to restore balance. After an encounter with an ethereal sage, you are bestowed with the Divya Jyoti, a divine flame that embodies the combined strengths of the Trimurti - Brahma, Vishnu, and Shiva. The flame is a guide and source of power but needs to be nurtured by acquiring spiritual, mental, and physical prowess.{Color.END}")
        print()
        print(f"{Color.GREEN}Embark on a spiritual journey through various realms of Hindu mythology, from the sacred peaks of Kailash to the depths of Patala. Along your journey, you will encounter various challenges, puzzles, mythical creatures, and deities. You will need to make decisions based on morality, courage, wisdom, and selflessness. Each decision you make will determine the strength of your Divya Jyoti.{Color.END}")
        print()
    def describe_bramha_quest(self):
        print(f"You have travelled to sacred ashrams hidden in the dense forests of {Color.GREEN}Dandakaranya{Color.END} to learn the Vedas' wisdom. It is the test of your knowledge and wisdom where ancient rishis and scholars pose puzzles and riddles in your path to achieve enlightement.")
        print()
        print(f"{Color.DARKCYAN}You sit with Bramha and the test begins...{Color.END}")
        print()

