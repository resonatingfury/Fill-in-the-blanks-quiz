questionList = [["easy", "one + one = ____", "Follow along! A, B, C, ____, ____.", "Follow along! One, two, four, eight, ____, ____, ____.", "This quiz was ____."],
                ["medium", "There are ____ states in the United States of America.", "____ J. ____ is the 45th president of the United States of America",
                 "The three American branches of government are: j____, e____, and l____.", "This quiz was ____."],
                ["hard", "The square root of six hundred and seventy six is ____.", "Pi to the seventh decimal is ____.", "My three favorite foods are ____, ____, and ____.",
                 "This quiz was ____."]]

answerKey = [["easy", "one + one = two", "Follow along! A, B, C, D, E.", "Follow along! One, two, four, eight, sixteen, thirty two, sixty four.", "This quiz was easy."],
             ["medium", "There are fifty states in the United States of America.", "Donald J. Trump is the 45th president of the United States of America",
              "The three American branches of government are: judicial, executive, and legislative.", "This quiz was medium."],
             ["hard", "The square root of six hundred and seventy six is twenty six.", "Pi to the seventh decimal is 3.1415926.", "My three favorite foods are ramen, ramen, and ramen.",
              "This quiz was hard."]]

digitKey = [["50", "fifty"], ["2", "two"], ["16", "sixteen"], ["26", "twenty six"], ["32", "thirty two"], ["64", "sixty four"]]

# Welcome to the quiz. First, the parameters for our quiz's toughness.

#Behavior: recursive function that asks the user to input a valid difficulty level
#Inputs: none
#Outputs: string difficulty as 'easy', 'medium', or 'hard'
def getDifficulty():
    while True:
        difficulty = raw_input("What difficulty would you like to play on? Type easy, medium or hard.")
        if difficulty in ('easy', 'medium', 'hard'):
            break
        else:
            print "Sorry, please try again, and type 'easy', 'medium' or 'hard' exactly."
    return difficulty

#Behavior: recursive function that asks the user to input how many tries per question they'd like to have, converting the input to an integer
#Inputs: none
#Outputs: int numberOfTries
def getTries():
    tryMinimum = 1
    while True:
        numberOfTriesInitial = raw_input("How many attempts would you like to have for each question before failing the quiz?")
        if numberOfTriesInitial.isdigit() and int(numberOfTriesInitial) >= tryMinimum:
            print "Great, " + numberOfTriesInitial + " tries."
            numberOfTries = int(numberOfTriesInitial)
            break
        else:
            print "Since you're a sassy one and tried to break my code, you only get 1 try. Good luck!"
            numberOfTries = 1
            break
    return numberOfTries
# Great! Now, even a complete moron can't ruin it.

#Behavior: returns the appropriate question or answer string based on difficulty/what stage the user is on
#Inputs: difficulty setting, what question the user is on, and what list to search
#Outputs: the question/answer the user is currently on
def getSentence(diff, place, array):
    for diffBlock in array:
        for determineDiff in diffBlock:
            if determineDiff == diff:
                return diffBlock[place]
            else:
                break

#Behavior: runs the current question using the allotted amount of tries and returns True for completion, False for failure
#Inputs: difficulty setting, what question the user is on, and the number of tries the user has
#Outputs: True if the question was answered correctly, False if not
def runQuestion(diff, place, tries):
    question = getSentence(diff, place, questionList)
    tryTotal = 0
    while tryTotal < tries:
        tryTotal += 1
        answer = raw_input("Question " + str(place) + ": " + question)
        answerList = answer.split(',')
        if isCorrect(answerList, question, place, diff):
            return True
        else:
            print "Oh, no! That's incorrect. You have " + str(tries - tryTotal) + " tries left."
    return False

#Behavior: replaces an integer number with its whole word
#Inputs: the user answer currently being checked
#Outputs: the word version of the number, or the original string if a number was not input
def numToWord(userNumber):
    for section in digitKey:
        for digit in section:
            if digit == userNumber:
                # finds a digit that is available in digitKey and replaces it with the corresponding word
                return section[1]
    return userNumber

#Behavior: replaces the blanks in questions with the user's answers both for comparison and printing
#Inputs: a list of the user's answers, the question being answered
#Outputs: the question with all blanks filled with user answers
def completeSentence(answerList, question):
    # keeps track of what word in the question we are at
    questionIndex = 0
    # keeps track of which of the user's answers we are currently using
    answerIndex = 0
    questionBreakdown = question.split(" ")
    for x in questionBreakdown:
        if '____' in x:
            try:
                questionBreakdown[questionIndex] = x.replace('____', answerList[answerIndex])
                answerIndex += 1
            except:
                break
        questionIndex+=1

    return " ".join(questionBreakdown)

#Behavior: checks to see if the user's answers are correct by filling the blanks and comparing it with the answer key
#Inputs: a list of the user's answers, the question being answered, what question number the user is on, and the difficulty level
#Outputs: True if the answers were correct, False if not
def isCorrect(answerList, question, place, diff):
    # quickly strips the list contents of extra spaces and replaces numbers with words if necessary
    answerList = [x.strip() for x in answerList]
    answerList = [numToWord(x) for x in answerList]

    # pulls the compiled sentence replacing blanks with user input
    finalAnswer = completeSentence(answerList, question)
    print 'Your answer, "' + finalAnswer + '", is...'
    if finalAnswer.lower() == getSentence(diff, place, answerKey).lower():
        return True
    else:
        return False

#Behavior: this is a main container that holds the parameters for the game, including the wincon, progression through questions and a losecon
#Inputs: what question number the user is on, which will always be one at the time of calling
#Outputs: none
def runGame(currentQuestion):
    questionMax = 4

    print "Fill in all the blanks in order, delimiting answers with commas(ie: orange, pythons are cool, Udacity)."
    while currentQuestion <= questionMax:
        if currentQuestion == 1:
            difficulty = getDifficulty()
            numberOfTries = getTries()

        result = runQuestion(difficulty, currentQuestion, numberOfTries)
        if result:
            # win condition
            if currentQuestion == questionMax:
                print "Correct! Congrats, you answered all questions correctly! This game will now close."
                break
            else:
                print "Correct! Good job, you get to advance to the next question!"
                currentQuestion += 1
        else:
            print "Womp womp. You could not answer question " + str(currentQuestion) + " correctly, so you lose. Better luck next time!"
            break

#Behavior: allows the user to decide whether or not they'd like to play again
#Inputs: none
#Outputs: True if the user wants to, False if not
def tryAgain():
    # user has the option to play again if they lost
    refresh = raw_input("Would you like to try again? 'yes, please' for yes, anything else for no.")
    if refresh.lower() == 'yes, please':
        print "Alrighty! Hope you do better this time."
        return True
    elif refresh.lower() in ('yes', 'y'):
        print "Not good enough. Go away."
        return False
    else:
        print "Bye, Felicia."
        return False

# simple loop that runs the program itself for as long as the user would like, breaking when the user quits
def shell():
    while True:
        currentQuestion = 1
        runGame(currentQuestion)
        if tryAgain() == False:
            break

shell()
