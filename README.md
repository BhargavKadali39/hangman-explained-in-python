
# hangman-explained-in-python
Detailed explanation of hangman using python and snippets

<h1>UNDER WORK</h1>

## Table of contents
* [About-Hangman](#about-hangman) <!-- done -->
* [creating-xlsx-file](#creating-xlsx-file) <!-- done -->
* [input-for-adding-words](#input-for-adding-words) <!-- done -->
* [to-and-fro-in-xlsx](#to-and-fro-in-xlsx)
* [choosing-random-word](#choosing-random-word)   <!-- done -->
* [trial-and-errors](#trial-and-errors)
* [unveiling-word](#unveiling-word)  <!-- done -->
* [result-prediction](#result-prediction)
* [summary](#summary)

## about-hangman
Hangman is a popular word prediction game in which the player tries to piece together a missing word <br>one letter at a time.<br>The game ends after a specific amount of incorrect assumptions are made, and the player loses.<BR>Meanwhile when the player correctly identifies all of the letters of the lost word, the game is likewise over. 

## creating-xlsx-file
  Here I used ___xlsxwriter___ module to create a xlsx file, which takes input from the user to create a file.
  ___xlrd___ module is used to read the words from the file so user have multiple options for inputs.
  commands to install the module are below
  
    pip install xlsxwriter
    pip install xlrd 
  
## input-for-adding-words
  Now comes the tricky part if you're a beginner and struggling with syntatical errors like giving wrong parameters etc.
  Below line is the only script used to take input from user.
  
    b = list(map(str, input("Enter the words in a single go: ").strip().split()))[:n]
  
  let's divide it into 5 part's to avoid confusion
  >list():  
  
  The list function is used to convert other datatype to list which was clearly stated by me in one of my [REPO](https://github.com/BhargavKadali39/Python_Data_Structure_Cheat_Sheet)
  >map():
  
  We can pass multiple iterable arguments to the map () function. In that case, the specified function must have that many arguments. The function will be applied to these iterable elements in parallel. With multiple iterable arguments, the map iterator stops when the shortest iterable is exhausted.
  >strip():
  
  The strip function removes whitespace's that are present at the beginning and at the ending of the string.
  >split():
  
  This divides a given sentence into words the default parameter for it is whitespace but anything can be given otherthan that.
  >[:n]
  
  The slice operator reduces the amount of given value into certain index value. ":" colon is also known as slice operator in python.
  Here the n is no.of inserting elements and the slice operator is given n as end value as it's after the operator.
  the slice operater make sure to remove exceeding amount of words than given with the help of indexing.

  ## choosing-random-word
  Here for chooisng random word we used python random module which is a inbuilt so installation is required.
  
    import random  
    a = ['Gas', 'Food', 'Gym', 'Health']  
    word = random.choice(a)  
    print(word)  
  
  choice command in random modules chooses any one of the given data and return it to the respective variable. 
  
  ## to-and-fro-in-xlsx
  In the module 'xlsxwriter' we have a function called write() which takes parameter's as row, col ,item
  Here item refers to the element that needs to be inserted into the sheet
  Loop it up and you are all good to go
  
      worksheet = workbook.add_worksheet()
      worksheet.write(row, col, item)
  
  ## trial-and-errors
  These are nothing but bunch of if and else conditions shown below.
  
    guess = input("\nguess a character:")
      your_guess += guess
      if guess not in word:
          turns -= 1
          print("\nWrong")
          print("\nYou have", + turns, 'more guesses')
          if turns == 0:
              print("\nYou Lose")
  
  Firstly it takes input from the user and adds it the total guesses.  
  if the current guess is not present in the random word then one point is reduced and warning statement's are shown.
  The other way it ignores as my crush did and continues to loop unitll you have 0 turns left or you've won the game.

  ## unveiling-word
  
    for char in word:
        if char in your_guess:
            print(char, end="")
        else:
            print("_", end="")
  The above loop will be insides another while loop, so in consideration for it the for loop decides to show the true characters you've entered.
  if block shows the char if you've entered it previously or the else block comes into action and provides empty blank space for it.
