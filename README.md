
# hangman-explained-in-python
Detailed explanation of hangman using python 

<h1>UNDER WORK</h1>

## Table of contents
* [About-Hangman](#about-hangman)
* [creating-xlsx-file](#creating-xlsx-file)
* [adding-words-of-choice](#adding-words-of-choice)
* [choosing-random-word](#choosing-random-word)
* [trial-and-errors](#trial-and-errors)
* [unveiling-word](#unveiling-word)
* [result-prediction](#result-prediction)
* [try-again](#try-again)
* [summary](#summary)

## about-hangman
Hangman is a popular word prediction game in which the player tries to piece together a missing word <br>one letter at a time.<br>The game ends after a specific amount of incorrect assumptions are made, and the player loses.<BR>Meanwhile when the player correctly identifies all of the letters of the lost word, the game is likewise over. 

## creating-xlsx-file
  Here I used ___xlsxwriter___ module to create a xlsx file, which takes input from the user to create a file.
  ___xlrd___ module is used to read the words from the file so user have multiple options for inputs.
  commands to install the module are below
   > pip install xlsxwriter
   > pip install xlrd 
## adding-words-of-choice
  Now comes the tricky part if you're a beginner and struggling with syntatical errors like giving wrong parameters etc.
  Below line is the only script used to take input from user.
  > b = list(map(str, input("Enter the words in a single go: ").strip().split()))[:n]
  
  let's divide it into 4 part's to avoid confusion
  + list(): The list function is used to convert other datatype to list which was clearly stated by me in one of my [REPO](https://github.com/BhargavKadali39/Python_Data_Structure_Cheat_Sheet)
  + map(): We can pass multiple iterable arguments to the map () function. In that case, the specified function must have that many arguments. The function will be applied to these iterable elements in parallel. With multiple iterable arguments, the map iterator stops when the shortest iterable is exhausted.
  + strip(): The strip function removes whitespace's that are present at the beginning and at the ending of the string.
  + split(): This divides a given sentence into words the default parameter for it is whitespace but anything can be given otherthan that.
  + [:n] The slice operator reduces the amount of given value into certain amount. ":" colon is also known as slice operator in python.
  Here the n is no.of inserting elements and the slice operator is given n as end value as it's after the operator.
  the slice operater make sure to remove exceeding amount of words than given.

