from gameplay_utils.components import Color

def challenge_brahma(player):
    riddles = [
        {
            "text": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "echo",
            "hints": ["I'm not a creature, but I follow you like a shadow.", "I'm a type of sound.", "You hear me when you talk to mountains."],
            "atmosphere": "The air around you and Brahma suddenly becomes very still. You can hear the soft rustling of leaves in the distance, as if nature itself is whispering the answer to you."
        },
        {
            "text": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "answer": "pencil lead",
            "hints": ["I'm an integral part of a common tool.", "I leave a mark when I'm used.", "I'm used for writing."],
            "atmosphere": "The surroundings change, and you feel as though you are deep inside the earth. The smell of damp soil fills your nostrils, and you can hear a faint, rhythmic chipping sound."
        },
        {
            "text": "I fly without wings, I cry without eyes. Wherever I go, darkness follows me. What am I?",
            "answer": "cloud",
            "hints": ["I'm found in the sky.", "I can cover the sun.", "I'm associated with rain."],
            "atmosphere": "Suddenly, you feel a cool breeze against your skin. You look up to see the sky is overcast, and a single drop of rain lands on your cheek."
        },
        # Add more riddles as dictionaries here...
    ]

    for riddle in riddles:
        print(f"{Color.PURPLE}{riddle['atmosphere']}{Color.END}")
        print(f"{Color.PURPLE}{riddle['text']}{Color.END}")
        for i in range(3):
            answer = input("Your answer: ")
            if answer.lower() == riddle['answer']:
                print(f"\nYou have answered correctly!")
                break  # Breaks the inner loop and moves to the next riddle
            else:
                if i < 2:
                    print(f"\nYou have answered incorrectly. Brahma gives you a hint: {riddle['hints'][i]}")
                else:
                    print("\nBrahma seems disappointed as you failed to solve his riddle. He vanishes, and you are left alone in the forest.")
                    return False  # Ends the challenge if the player fails to solve a riddle

    player.gain_wisdom(10)  # Reward player only if they solved all riddles
    print(f"\nImpressed by your wisdom, Brahma disappears, leaving you with a sense of enlightenment. Your wisdom increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
    return True


def challenge_vishnu(player):
    print(f"{Color.PURPLE}The beast is terrorizing the villagers. You decide to face the beast. You need to be quick and courageous. Do you want to attack the beast or devise a plan to trap it?{Color.END}")
    answer = input("Your choice (attack/trap): ")

    if answer.lower() == 'trap':
        print(f"\nYou decide to trap the beast. After observing the beast, you notice that it is attracted to a certain fruit that grows in the village. You decide to use this fruit as bait.")
        print(f"{Color.PURPLE}First, you need to collect the fruit. But the fruit is located high up in the tree. Do you climb the tree or shake the tree to get the fruit?{Color.END}")
        answer = input("Your choice (climb/shake): ")

        if answer.lower() == 'climb':
            print("\nYou skillfully climb the tree and collect the fruit.")
            print(f"{Color.PURPLE}Next, you need to set the trap. There's a large pit nearby that could serve as a trap. Do you cover the pit with leaves or try to lure the beast into the pit directly?{Color.END}")
            answer = input("Your choice (leaves/lure): ")

            if answer.lower() == 'leaves':
                print("\nYou cover the pit with leaves and place the fruit on top. The beast, attracted by the fruit, steps onto the leaves and falls into the pit. The villagers cheer as they see the beast trapped.")
                player.gain_courage(10)
                print(f"\nYour plan worked perfectly! The beast is trapped and the villagers are safe. Your courage increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
                return True
            else:
                print("\nYou try to lure the beast into the pit directly. However, the beast is too clever and avoids the pit. The villagers continue to live in fear.")
                return False
        else:
            print("\nYou shake the tree but the fruit doesn't fall. The beast continues to terrorize the village.")
            return False
    else:
        print("\nYou attack the beast but it's too strong. The beast escapes your attack. The villagers continue to live in fear.")
        return False


def challenge_shiva(player):
    print(f"{Color.PURPLE}You sit down to meditate. The cold is unbearable but you must persevere. You start to feel your inner demons surfacing. Do you confront them or suppress them?{Color.END}")
    answer = input("Your choice (confront/suppress): ")
    if answer.lower() == 'confront':
        print("\nYou decide to confront your inner demons. As you delve deeper into your meditation, you start to see visions...")
        
        # First vision
        print(f"{Color.PURPLE}You see yourself standing at a crossroads. One path is strewn with gold and jewels but is guarded by a fierce dragon. The other path is simple and unguarded but requires a steep climb over a mountain. Which path do you choose?{Color.END}")
        path_choice = input("Your choice (gold/mountain): ")
        if path_choice.lower() == 'mountain':
            print("\nYou choose the mountain path, valuing the peace of the journey over material wealth. Your wisdom grows.")
            player.gain_wisdom(5)

        # Second vision
        print(f"{Color.PURPLE}Next, you see a vision of a man attacking a defenseless creature. Do you intervene to save the creature, or do you believe in the law of the jungle, where the strong dominate the weak?{Color.END}")
        intervene_choice = input("Your choice (intervene/jungle): ")
        if intervene_choice.lower() == 'intervene':
            print("\nYou intervene to save the creature, showing your courage and kindness. Your courage grows.")
            player.gain_courage(5)

        # Third vision
        print(f"{Color.PURPLE}You see a vision of a beggar and a king. The beggar offers you his only piece of bread, while the king offers you a position of power and wealth. Whose offer do you accept?{Color.END}")
        offer_choice = input("Your choice (beggar/king): ")
        if offer_choice.lower() == 'beggar':
            print("\nYou accept the beggar's offer, showing your humility and selflessness. Your selflessness grows.")
            player.gain_selflessness(5)

        # Fourth vision
        print(f"{Color.PURPLE}In another vision, you find yourself in a burning village. You have the power to either save the village library full of ancient wisdom or a young child who is trapped. Who do you save?{Color.END}")
        save_choice = input("Your choice (library/child): ")
        if save_choice.lower() == 'child':
            print("\nYou choose to save the child, valuing life over knowledge. Your compassion grows.")
            player.gain_selflessness(5)

        # Fifth vision
        print(f"{Color.PURPLE}Finally, you see a vision of yourself standing before a great army. You can either lead the army into a battle for a just cause, knowing many will die, or you can try to negotiate peace, even if it means compromising on your values. What do you do?{Color.END}")
        lead_choice = input("Your choice (lead/negotiate): ")
        if lead_choice.lower() == 'lead':
            print("\nYou choose to lead the army, valuing justice over peace. Your courage grows.")
            player.gain_courage(5)

        print(f"\nAfter confronting these visions, you come out of your meditation. You feel a change within you. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
        return True
    else:
        print("\nYou try to suppress your inner demons but they resist. The meditation fails and you gain nothing.")
        return False


def challenge_asura(player):
    print(f"{Color.PURPLE}The Asura warriors are attacking your village. You decide to defend it. Do you fight them head-on or devise a strategy to outsmart them?{Color.END}")
    answer = input("Your choice (fight/strategy): ")

    if answer.lower() == 'strategy':
        print("\nChoosing the path of strategy, you gather your village's wise men and women to devise a plan. The night is spent in deep discussion, analyzing the Asuras' attack patterns and identifying their weaknesses.")
        print("You notice that the Asuras, while formidable in a frontal assault, have a vulnerability at the back due to less armor.")
        print("Do you plan to attack from the front, leveraging your village's fortifications, or devise a risky strategy to attack them from behind?")
        attack_plan = input("Your choice (front/behind): ")
        
        if attack_plan.lower() == 'front':
            print("\nBravely, you decide to face the Asuras head-on. The villagers fortify the front, preparing for the assault. The Asuras charge, their roars filling the night.")
            print("Despite your best efforts, the Asura warriors' heavy front armor proves too robust to breach. They break through your fortifications, and the village suffers heavy losses. Strategy is not always about confronting danger head-on.")
            return False
        else:
            print("\nYou decide on a daring plan to flank the Asuras and attack from behind. However, this requires stealth and a significant diversion. A decision needs to be made.")
            print("You consider setting a large bonfire at the village front to distract the Asuras, but it risks significant damage to the village. Alternatively, a group of brave villagers volunteer to lure the Asuras away from the village, risking their lives.")
            distraction = input("Your choice (fire/volunteers): ")
            
            if distraction.lower() == 'fire':
                print("\nWith a heavy heart, you decide to start a fire at the front of the village. As the flames rise high, the Asuras are drawn towards the spectacle.")
                print("Using this distraction, your warriors launch a surprise attack from behind, catching the Asuras off guard. Despite the damage to the village, the strategy is a success! The Asura warriors retreat.")
                player.gain_strength(10)
                print(f"\nYour strength increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
                
                print("\nWith the Asura warriors in disarray, now is the time to strike. Do you lead the charge, or do you send your best warriors?")
                charge = input("Your choice (lead/send): ")
                if charge.lower() == 'lead':
                    print("\nWith a rallying cry, you lead the charge against the confused Asuras. Inspired by your courage, the villagers follow, pushing the Asuras back.")
                    print("The strategy was a success! The Asura warriors retreat.")
                    player.gain_strength(10)
                    print(f"\nYour strength increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
                    return True
                else:
                    print("\nYou send your best warriors to attack the Asuras. However, without your leadership, they falter. The Asuras regroup and launch a counterattack. The village suffers heavy losses.")
                    return False
            else:
                print("\nThe brave volunteers set out, risking their lives to lure the Asuras away from the village. Their courage touches your heart.")
                print("Unfortunately, the Asuras see through the ruse and the element of surprise is lost. The village suffers heavy losses. Sometimes, the best laid plans fail to bear fruit.")
                return False

    else:
        print("\nChoosing the path of direct confrontation, you rally your warriors and prepare to meet the Asuras head-on. The village blacksmith works tirelessly, forging weapons for the upcoming fight.")
        print("The Asura warriors are numerous and well-trained. You need to find a way to thin their numbers. Do you target their leaders in the hope of disarraying their ranks, or focus on disrupting their formations to sow confusion?")
        fight_choice = input("Your choice (leaders/formations): ")
        
        if fight_choice.lower() == 'leaders':
            print("\nDeciding to cut the head off the snake, you target the Asura leaders. You stealthily make your way through the battlefield, your target in sight.")
            print("A fierce fight ensues, the outcome hanging in balance. Finally, with a mighty effort, you manage to defeat the Asura leader.")
            print("Seeing their leader fall, confusion spreads among the Asura ranks. Sensing the opportunity, your warriors charge, routing the Asuras. The day is won!")
            player.gain_strength(10)
            print(f"\nYour strength increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
            
            print("\nWith the Asura leader defeated, the Asuras are in disarray. Now is the time to strike. Do you chase the retreating Asuras, or do you regroup and fortify the village?")
            next_step = input("Your choice (chase/regroup): ")
            if next_step.lower() == 'chase':
                print("\nYou decide to chase the retreating Asuras. However, they were feigning retreat and launch a surprise attack. You suffer heavy losses.")
                return False
            else:
                print("\nYou decide to regroup and fortify the village. The Asuras, seeing your defenses, decide not to attack again. The village is safe!")
                player.gain_strength(10)
                print(f"\nYour strength increases. Your current powers are: Wisdom {player.wisdom}, Courage {player.courage}, Selflessness {player.selflessness}, Strength {player.strength}.\n")
                return True
        else:
            print("\nChoosing to disrupt their formations, you lead a small group of warriors into the thick of the Asura ranks.")
            print("Despite your valiant efforts, the Asuras regroup quickly, their disciplined ranks proving too difficult to disrupt. They launch a counterattack, and the village suffers heavy losses. Even the mightiest of warriors need a good strategy.")
            return False

############################################### Final Battle #################################################################
def wisdom_challenge(player, boss):
    print("\nMahakala begins the battle by testing your wisdom. He conjures an illusion of an unsolvable labyrinth around you. In the center of the labyrinth, a flame burns brightly - the answer to a riddle. Mahakala smirks as he speaks, 'I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?'")
    answer = input("Your answer: ")
    if answer.lower() == 'fire':
        print("\nAs you say the answer aloud, the illusionary walls of the labyrinth crumble. The flame in the center flares up, blinding Mahakala momentarily. Using your wisdom, you've managed to reduce his strength.")
        boss.strength -= player.wisdom
    else:
        print("\nThe labyrinth around you tightens, its walls closing in. You've answered incorrectly. Mahakala smirks as he prepares his next challenge.")

def courage_challenge(player, boss):
    print("\nMahakala summons a horde of Asura warriors to test your courage. They surround you, their weapons glinting in the demonic light. Will you fight them head-on or retreat to strategize?")
    answer = input("Your choice (fight/strategize): ")
    if answer.lower() == 'fight':
        print("\nWith a courageous roar, you charge into the horde of Asuras. Each Asura warrior you fell, each blow you withstand, saps the strength from Mahakala.")
        boss.strength -= player.courage
    else:
        print("\nYou retreat to strategize, but the Asuras take advantage of your hesitation and launch an attack. Mahakala grins as he prepares his next challenge.")

def selflessness_challenge(player, boss):
    print("\nMahakala captures some villagers and threatens to harm them unless you surrender. The innocent faces of the villagers fill you with determination. Will you sacrifice yourself to save them?")
    answer = input("Your choice (yes/no): ")
    if answer.lower() == 'yes':
        print("\nWith a selfless heart, you offer yourself in exchange for the villagers. Mahakala, surprised by your selflessness, falters. This momentary lapse allows the villagers to escape and weakens Mahakala.")
        boss.strength -= player.selflessness
    else:
        print("\nYou decide not to surrender. As Mahakala cackles and the villagers cry out, you realize the importance of selflessness.")

def strength_challenge(player, boss):
    print("\nFinally, Mahakala challenges you to a duel to test your strength. The ground beneath you rumbles as Mahakala charges. Will you meet his charge head-on, or will you attempt to evade and counter?")
    answer = input("Your choice (charge/evade): ")
    if answer.lower() == 'charge':
        print("\nWith all your strength, you charge at Mahakala. The impact of the clash reverberates through the realm. Mahakala staggers back, weakened.")
        boss.strength -= player.strength
    else:
        print("\nYou attempt to evade Mahakala's charge. However, he anticipates your move and strikes. You barely manage to block his attack but suffer a heavy blow. Your strength wasn't enough.")


def fight_boss(player, boss):
    print(f"{Color.RED}\nYour journey culminates in the Asura realm, where {boss.name} awaits. The final battle is fierce and grueling.{Color.END}")

    wisdom_challenge(player, boss)
    courage_challenge(player, boss)
    selflessness_challenge(player, boss)
    strength_challenge(player, boss)

    # Check if player has defeated boss
    if boss.strength <= 0:
        print(f"\nYou have defeated {boss.name}! The cosmos is saved, and balance is restored! Your journey as the Veer Purusha has been successful.")
        return True
    else:
        print(f"\nDespite your best efforts, {boss.name} is too powerful. The cosmos is plunged into chaos as you vow to come back stronger.")
        return False