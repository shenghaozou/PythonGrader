# -*- coding: utf-8 -*- 
import string

def most_repeated_letters(a):
  '''Return the number of times the most frequent letter repeats.'''
  b=0
  c=0
  while b< len(a):
    c=max(string.count(a,a[b]),c)
    b=b+1
  return c

def has_equal_letters(a):
  '''counting the number of vowels and consonants present,see if they are equal'''
  c=string.count(a,'a')+string.count(a,'e')+string.count(a,'i')+string.count(a,'o')+string.count(a,'u')
  b=len(a)-c
  return b==c
  
def is_palindrome(a):
  '''whether a word reads the same backwards as it does forwards'''
  b=len(a)/2
  if b==1:
    return a[0]==a[-1]
  else:
    return a[0:b-1]==a[len(a)-1:len(a)-b:-1]
  
def total_points(a):
  '''Total word points'''
  letter_count=len(a)
  if most_repeated_letters(a)>2:
    points=letter_count/3 # get 1/3 of the points if it has triple letters
  elif most_repeated_letters(a)==2 :
    points=letter_count*2 # get double points if it has only duplicate letters
  else:
    points=letter_count
  if has_equal_letters(a):
    points*=2 # get double points if it has equal numbers of vowels and consonants
  if is_palindrome(a):
    points*=5 # get 5x points if it is a palindrome
  return points
  
def is_trick_round(a,b):
  '''Count the total number of 'y' characters in both words.
     Return True if that number is odd.'''
  c=string.count(a,'y')+string.count(b,'y')
  return c%2==1
  

import random

#######################################################
#
# HI 301 STUDENTS! YOUR FUNCTIONS WILL GO UP HERE. :)
#
#######################################################



#######################################################
#
# EVERYTHING BELOW THIS IS HOBBES' CODE; MODIFY AT YOUR OWN RISK.
#
#######################################################

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
    print "Game over:",
    if comp_total > user_total:
        print "Computer wins!"
    else:
        print "You win!"

if __name__ == "__main__":
    play_game()
