# -*- coding: utf-8 -*- 
#My name:Jiyun Chen
#1
def most_repeated_letters(word_1):
  """
  To find the largest number of the repeat characters.
  """
  num=word_1.count(word_1[0])
  for i in range(len(word_1)):
    num_1=word_1.count(word_1[i])
    if(num_1>=num):
      num=num_1;
  return(num)

#2
def has_equal_letters(word_2):
  """
  To check whether the number of vowels is equal to the number of consonants or not .
  """
  n=0
  for i in range(len(word_2)):
    if(word_2[i]=="a" or word_2[i]=="e" or word_2[i]=="i" or word_2[i]=="o" or word_2[i]=="u"):
      n+=1;
  m=len(word_2)-n
  if(m==n):
    return(True)
  else:
    return(False)

#3
def is_palindrome(word_3):
  """
  To check whether the word is the "Palindrome".
  """
  for i in range(len(word_3)):
    if(word_3[i]==word_3[len(word_3)-1-i]):
      return(True)
    else:
      return(False)

#4
def total_points(word):
  """
  To get the total points following the rules.
  """
  points=len(word);
  if(most_repeated_letters(word)>=3):
    points=int(points/3);
  elif(most_repeated_letters(word)==1):
    points=points;
  else:
    points=points*2;
  if(is_palindrome(word)):
    points=points*5;
  else:
    points=points;
  if(has_equal_letters(word)):
    points=points*2;
  else:
    points=points
  return(points)


#5
def is_trick_round(p1_word, p2_word):
  """
  To get the total number of "y" in the two words to decide True or False.
  """
  p=p1_word+p2_word;n=0;
  for i in range(len(p)):
    if(p[i]=="y"):
      n+=1;
  if(n%2==1):
    return(True)
  else:
    return(False)


import random
def get_computer_play():
    """
    Chooses a random word from this list of ridiculous English words and returns it
    """
    return random.choice(['Ailurophile', 'Assemblage', 'Becoming', 'Beleaguer',
                          'Brood', 'Bucolic', 'Bungalow', 'Chatoyant', 'Comely',
                          'Conflate', 'Cynosure', 'Dalliance', 'Demesne', 'Demure',
                          'Denouement', 'Desuetude', 'Desultory', 'Diaphanous',
                          'Dissemble', 'Dulcet', 'Ebullience', 'Effervescent',
                          'Efflorescence', 'Elision', 'Elixir', 'Eloquence',
                          'Embrocation', 'Emollient', 'Ephemeral', 'Epiphany',
                          'Erstwhile', 'Ethereal', 'Evanescent', 'Evocative',
                          'Fetching', 'Felicity', 'Forbearance', 'Fugacious',
                          'Furtive', 'Gambol', 'Glamour', 'Gossamer', 'Halcyon',
                          'Harbinger', 'Imbrication', 'Imbroglio', 'Imbue',
                          'Incipient', 'Ineffable', 'Ingenue', 'Inglenook',
                          'Insouciance', 'Inure', 'Kayak', 'Labyrinthine',
                          'Lagniappe', 'Lagoon', 'Languor', 'Lassitude', 'Leisure',
                          'Lilt', 'Lissome', 'Lithe', 'Love', 'Mellifluous',
                          'Moiety', 'Mondegreen', 'Murmurous', 'Nemesis', 'Numbered',
                          'Offing', 'Onomatopoeia', 'Opulent', 'Palimpsest',
                          'Panacea', 'Panoply', 'Pastiche', 'Penumbra', 'Petrichor',
                          'Plethora', 'Propinquity', 'Pyrrhic', 'Python',
                          'Quintessential', 'Ratatouille', 'Ravel', 'Redolent',
                          'Riparian', 'Ripple', 'Scintilla', 'Sempiternal', 'Seraglio',
                          'Serendipity', 'Summery', 'Sumptuous', 'Surreptitious',
                          'Susquehanna', 'Susurrous', 'Talisman', 'Tintinnabulation',
                          'Umbrella', 'Untoward', 'Vestigial', 'Wafture',
                          'Wherewithal', 'Woebegone'])

def play_game():
    """
    Runs the word game, user vs computer, using your functions.
    Will not work until you have them implemented correctly!
    """
    cutoff = 30       # CHANGE THIS IF YOU WANT A LONGER GAME!
    user_total = 0
    comp_total = 0

    print "First to", cutoff, "points wins!"
    print

    while user_total < cutoff and comp_total < cutoff:

        # get the user and computer words, convert to lower case
        user_word = raw_input("Your play:").lower()
        comp_word = get_computer_play().lower()
        print "Computer played", comp_word

        # calculate user and computer scores
        user_score = total_points(user_word)
        print "User score:", user_score
        comp_score = total_points(comp_word)
        print "Computer score:", comp_score

        # check whether this was a trick round, and score appropriately
        # round winner's score is added, round loser's score is subtracted
        is_trick = is_trick_round(user_word, comp_word)
        if is_trick:
            print "TRICK ROUND!"
        if (is_trick and user_score < comp_score) or (not is_trick and user_score > comp_score):
            print "You win!"
            user_total += user_score
            comp_total -= comp_score
        elif (is_trick and user_score > comp_score) or (not is_trick and user_score < comp_score):
            print "You lose!"
            user_total -= user_score
            comp_total += comp_score
        else:
            print "You tie!"

        # display current score totals
        print "Current scores:"
        print "\tYou:", user_total
        print "\tComputer:", comp_total
        print

    # display overall winner
    print ("Game over:")
    if comp_total > user_total:
        print "Computer wins!"
    else:
        print "You win!"

if __name__ == "__main__":
    play_game()
