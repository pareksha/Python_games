def hangman(number):
    if(number == 0):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 1):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 2):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 3):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|   |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 4):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('|'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 5):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('/    |'.rjust(10))
        print('|'.rjust(10))
        print('='*15)
    if(number == 6):
        print('+---+'.rjust(10))
        print('|   |'.rjust(10))
        print('O   |'.rjust(10))
        print('/|\  |'.rjust(10))
        print('/ \  |'.rjust(10))
        print('|'.rjust(10))
        print('='*15)

import random

list_of_strings = ['ABRUPTLY','ABSURD','ABYSS','AFFIX','ASKEW','AVENUE','AWKWARD','AXIOM','AZURE','BAGPIPES','BANDWAGON','BANJO','BAYOU','BEEKEEPER','BIKINI','BLITZ','BLIZZARD','BOGGLE','BOOKWORM','BOXCAR','BOXFUL','BUCKAROO','BUFFALO','BUFFOON','BUXOM','BUZZARD','BUZZING','BUZZWORDS','CALIPH','COBWEB','COCKINESS','CROQUET','CRYPT','CURACAO','CYCLE','DAIQUIRI','DIRNDL','DISAVOW','DIZZYING','DUPLEX','DWARVES','EMBEZZLE','EQUIP','ESPIONAGE','EUOUAE','EXODUS','FAKING','FISHHOOK','FIXABLE','FJORD','FLAPJACK','FLOPPING','FLUFFINESS','FLYBY','FOXGLOVE','FRAZZLED','FRIZZLED','FUCHSIA','FUNNY','GABBY','GALAXY','GALVANIZE','GAZEBO','GIAOUR','GIZMO','GLOWWORM','GLYPH','GNARLY','GNOSTIC','GOSSIP','GROGGINESS','HAIKU','HAPHAZARD','HYPHEN','IATROGENIC','ICEBOX','INJURY','IVORY','IVY','JACKPOT','JAUNDICE','JAWBREAKER','JAYWALK','JAZZIEST','JAZZY','JELLY','JIGSAW','JINX','JIUJITSU','JOCKEY','JOGGING','JOKING','JOVIAL','JOYFUL','JUICY','JUKEBOX','JUMBO','KAYAK','KAZOO','KEYHOLE','KHAKI','KILOBYTE','KIOSK','KITSCH','KIWIFRUIT','KLUTZ','KNAPSACK','LARYNX','LENGTHS','LUCKY','LUXURY','LYMPH','MARQUIS','MATRIX','MEGAHERTZ','MICROWAVE','MNEMONIC','MYSTIFY','NAPHTHA','NIGHTCLUB','NOWADAYS','NUMBSKULL','NYMPH','ONYX','OVARY','OXIDIZE','OXYGEN','PAJAMA','PEEKABOO','PHLEGM','PIXEL','PIZAZZ','PNEUMONIA','POLKA','PSHAW','PSYCHE','PUPPY','PUZZLING','QUARTZ','QUEUE','QUIPS','QUIXOTIC','QUIZ','QUIZZES','QUORUM','RAZZMATAZZ','RHUBARB','RHYTHM','RICKSHAW','SCHNAPPS','SCRATCH','SHIV','SNAZZY','SPHINX','SPRITZ','SQUAWK','STAFF','STRENGTH','STRENGTHS','STRETCH','STRONGHOLD','STYMIED','SUBWAY','SWIVEL','SYNDROME','THRIFTLESS','THUMBSCREW','TOPAZ','TRANSCRIPT','TRANSGRESS','TRANSPLANT','TRIPHTHONG','TWELFTH','TWELFTHS','UNKNOWN','UNWORTHY','UNZIP','UPTOWN','VAPORIZE','VIXEN','VODKA','VOODOO','VORTEX','VOYEURISM','WALKWAY','WALTZ','WAVE','WAVY','WAXY','WELLSPRING','WHEEZY','WHISKEY','WHIZZING','WHOMEVER','WIMPY','WITCHCRAFT','WIZARD','WOOZY','WRISTWATCH','WYVERN','XYLOPHONE','YACHTSMAN','YIPPEE','YOKED','YOUTHFUL','YUMMY','ZEPHYR','ZIGZAG','ZIGZAGGING','ZILCH','ZIPPER','ZODIAC','ZOMBIE']
string = random.choice(list_of_strings)

x = 0

list_ = [string[i] for i in range(len(string))]
blank_list = ['_' for i in range(len(string))]

hangman(0)
print(' '.join(blank_list))

while(x<6):
    print("\nGuess an alphabet")
    guess = (input()).upper()
    if guess in blank_list:
        print('You already guessed the letter..!!')
    for i in range(len(list_)):
        if(guess == list_[i]):
            blank_list[i] = list_[i]
    if guess not in list_:
        x+=1
    if '_' not in blank_list:
        print('You won')
        break
    else:
        pass
    hangman(x)
    print(' '.join(blank_list))

if(x==6):
    print('You lost..!!')
