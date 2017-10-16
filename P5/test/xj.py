# -*- coding: utf-8 -*- 
import random

#######################################################
#
# HI 301 STUDENTS! YOUR FUNCTIONS WILL GO UP HERE. :)
#
#######################################################

def most_repeated_letters(word_1):
    Times = 0
    for letter in word_1:
        Times_temp = word_1.count(letter,0,len(word_1))
        if Times_temp >= Times:
            Times = Times_temp
    return Times



def has_equal_letters(word_2):
    vowels_number = 0
    consonants_number = 0
    for letter in word_2:
        if letter in "aeiou":
            vowels_number = vowels_number + 1
        else:
            consonants_number = consonants_number + 1
    if vowels_number == consonants_number:
        return True
    else:
        return False



def is_palindrome(word_3):
    word_inv = word_3[::-1]
    if word_3 == word_inv:
        return True
    else:
        return False

def total_points(word):
    points = len(word)
    letters_repeat = most_repeated_letters(word)
    if letters_repeat >=3:
        points = points/3
    elif letters_repeat == 2:
        points = points * 2
    if has_equal_letters(word):
        points = points * 2
    if is_palindrome(word):
        points = points * 5
    return points


def is_trick_round(p1_word, p2_word):
    pw = p1_word + p2_word
    num = pw.count("y",0,len(pw))
    if num % 2 ==1:
        return True
    else:
        return False



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
