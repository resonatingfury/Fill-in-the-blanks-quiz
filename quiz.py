# currentQuestion is what question the player is currently on
currentQuestion = 1
difficulty = ""
numberOfTries = ""
questionList = [["easy", "There are ____ states in the United States of America.", "____ J. ____ is the 45th president of the United States of America", 
                 "The three American branches of government are: j____, e____, and l____."],
               ["medium", "", "medium2", "medium3"],
               ["hard", "hard1", "hard2", "hard3"]]
answerKey = [["easy", "There are fifty states in the United States of America.", "Donald J. Trump is the 45th president of the United States of America", 
              "The three American branches of government are: judicial, executive, and legislative."],
            ["medium", "medium1", "medium2", "medium3"],
            ["hard", "hard1", "hard2", "hard3"]]
digitKey = [["50", "fifty"]]

# Welcome to the quiz. First, the parameters for our quiz's toughness.
while True:
  difficulty = raw_input("What difficulty would you like to play on? Type easy, medium or hard.")
  if difficulty in ('easy', 'medium', 'hard'):
      break
  else:
      print "Sorry, please try again, and type 'easy', 'medium' or 'hard' exactly."

while True:
    numberOfTries = raw_input("How many attempts would you like to have before failing the quiz?")
    if numberOfTries.isdigit() and int(numberOfTries) > 0:
        if(int(numberOfTries) > 0):
            print "Great, " + numberOfTries + " tries."
            break
    else:
        print "Since you're a sassy one and tried to break my code, you only get 1 try. Good luck!"
        numberOfTries = '1'
        break
# Great! Now, even a complete moron can't ruin it.

# returns the appropriate question or answer string based on difficulty/what stage the user is on
def getSentence(diff, place, array):
    for diffBlock in array:
        for determineDiff in diffBlock:
            if determineDiff == diff:
                return diffBlock[place]
            else:
                break

# runs the current question using the allotted amount of tries and returns True for completion, False for failure
def runQuestion(diff, place):
    question = getSentence(diff, place, questionList)
    tryTotal = 0
    while tryTotal < int(numberOfTries):
        tryTotal += 1
        answer = raw_input("Question " + str(place) + ": " + question)
        answerList = answer.split(',')
        if isCorrect(answerList, question):
                return True
        else:
            print "Oh, no! That's incorrect. You have " + str(int(numberOfTries) - tryTotal) + " tries left."
    return False

# replaces a number with its whole word, if applicable
def numToWord(x):
    for section in digitKey:
        for digit in section:
            if digit == x:
                # finds a digit that is available in digitKey and replaces it with the corresponding word
                return section[1]
    return x

# replaces the blanks in questions with the user's answers both for comparison and printing
def completeSentence(answerList, question):
    # keeps track of what word in the question we are at
    questionIndex = 0
    # keeps track of which of the user's answers we are currently using
    answerIndex = 0
    questionBreakdown = question.split(" ")
    for x in questionBreakdown:
        if x == '____':
            try:
                questionBreakdown[questionIndex] = answerList[answerIndex]
                answerIndex += 1
            except:
                break
        questionIndex+=1

    return " ".join(questionBreakdown)

# checks to see if the user's answers are correct by filling the blanks and comparing it with the answer key
def isCorrect(answerList, question):
    answerList = [x.strip() for x in answerList]
    answerList = [numToWord(x) for x in answerList]

    # pulls the compiled sentence replacing blanks with user input
    finalAnswer = completeSentence(answerList, question)
    print 'Your answer, "' + finalAnswer + '", is...'
    if finalAnswer.lower() == getSentence(difficulty, currentQuestion, answerKey).lower():
        return True
    else:
        return False

# this is the main container, using all parameters and functions to run the quiz
while currentQuestion < 4:
    print "Fill in all the blanks in order, delimiting answers with commas(ie: orange, pythons are cool, Udacity)."
    result = runQuestion(difficulty, currentQuestion)
    if result:
        # win condition
        if currentQuestion == 3:
            print "Correct! Congrats, you answered all questions correctly! This game will now close."
            break
        else:
            print "Correct! Good job, you get to advance to the next question!"
            currentQuestion += 1
    else:
        print "Womp womp. You could not answer question " + str(currentQuestion) + " correctly, so you lose. Better luck next time!"

        # user has the option to play again if they lost
        refresh = raw_input("Would you like to try again(using the same settings)? 'yes, please' for yes, anything else for no.")
        if refresh.lower() == 'yes, please':
            print "Alrighty! Hope you do better this time."
            currentQuestion = 1
        elif refresh.lower() in ('yes', 'y'):
            print "Not good enough. Go away."
            break
        else:
            print "Bye, Felicia."
            break
