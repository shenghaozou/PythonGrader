# -*- coding: utf-8 -*- 
#My Name: Kolbe Short
#Partner: Aman Adukoorie

def most_repeated_letters(word):
  '''This function is taking the number of letters of the most repeated letter in the word'''
  list = []
  word = str.lower(word)
  for element in word:
    x =word.count(element, 0, len(word))
    list.append(x)
  return max(list)

def has_equal_letters(word):
  '''This function is checking if the word has an equal number of vowels and consonants '''
  vowels=("a","e","i","o","u")
  consanants=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
  vowel_count=0
  consanants_count=0
  word = str.lower(word)
  for element in word:
    if element in vowels:
      vowel_count=vowel_count+1
  for element in word:
    if element in consanants:
      consanants_count=consanants_count+1
  return consanants_count == vowel_count

def is_palindrome(word):
  '''This function is checking if the word is a palindrome (or is the same forward and backwards)'''
  word= str.lower(word)
  list =[]
  list_rev= []
  count2=0
  count=1
  while count2 <len(word):
    forward=word[count2]
    list.append(forward)
    count2 = count2+1 
  while count -1 <len(word):
    palindrome=word[-(count)]
    list_rev.append(palindrome)
    count=count+1
  return list_rev == list

def total_points(word):
  '''This function pulls from the past functions to calculate the total amount of points achieved by a word'''
  word = str.lower(word)
  points=len(word)
  points_repeated = most_repeated_letters(word)
  if points_repeated >= 3:
    points=int(points/3)
  elif points_repeated ==2:
    points=2*points
  points_equal_letters= has_equal_letters(word)
  if points_equal_letters ==True:
    points=points*2
  points_palindrome = is_palindrome(word)
  if points_palindrome == True:
    points= points*5
  return points 
  
def is_trick_round(word5, word6):
  '''This function is checking if the number of total y's in the two words combine to an even or odd number  '''
  y_count1=0
  y_count2=0
  word5 = str.lower(word5)
  word6 = str.lower(word6)
  for element in word5:
    if element == 'y':
      y_count1=y_count1+1
  for element in word6:
    if element == 'y':
      y_count2=y_count2+1
  y_total=y_count1+y_count2
  return y_total%2==0

#quit()
