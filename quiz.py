correct_answers = 0

score=0

# QUESTION 1
answer1 = input("What is the capital of Queensland? \na.Townsville \nb. Brisbane \nc. Noosa \nAnswer: ")
if answer1 == "b" or answer1 == "Brisbane":
    score += 1
    correct_answers += 1
    print ("Correct!")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! The answer is Brisbane.")
    print("Score: ", score)
    print("\n")




# QUESTION 2
answer2 = input("In which state is Birdsville found? \na. NSW \nb. SA \nc. QLD \nAnswer: ")
if answer2 == "c" or answer2 == "QLD":
    score += 1
    correct_answers += 1
    print ("Correct!")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! The answer is QLD.")
    print("Score: ", score)
    print("\n")



# QUESTION 3
answer3 = input("Capital of New Zealand? \na. Wellington \nb. Washington, D.C. \nc. Canberra \nAnswer: ")
if answer3 == "a" or answer3 == "Wellington":
    score += 1
    correct_answers += 1
    print ("Correct!")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! The answer is Wellington.")
    print("Score: ", score)
    print("\n")




# QUESTION 4
answer4 = input("Tallest building in the world? \na. Shanghai \nb. Burj Khalifa \nc. Lotte \nAnswer: ")
if answer4 == "b" or answer4 == "Burj Khalifa":
    score += 1
    correct_answers += 1
    print ("Correct!")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! The answer is Burj Khalifa.")
    print("Score: ", score)
    print("\n")



# QUESTION 5
answer5 = input("Expensive car in the world? \na. Bugatti Veyron \nb. Ferrari 250 GTO \nc. Rolls-Royce Boat Tail \nAnswer: ")
if answer5 == "c" or answer5 == "Rolls-Royce Boat Tail":
    score += 1
    correct_answers += 1
    print ("Correct!")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! The answer is Burj Khalifa.")
    print("Score: ", score)
    print("\n")    


# QUESTION 6
answer6 = input("What is the age of Earth? \na. 6.127 Billon years \nb. 4.543 Billon years \nc. 7.191 Billon years \nAnswer: ")
if answer6 == "b" or answer6 == "4.543 Billon years":
    score += 1
    correct_answers += 1
    print ("Correct! 4.543 Billon years")
    print("Score:", score)
    print("\n")
else:
    print("Incorrect! .")
    print("Score: ", score)
    print("\n")




print("Score: ", score)
print("correct answers: ", correct_answers)
