from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
#we are going to create a question class
#we are going to create an array of questions
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]
#now we mist write a function that will write the test

def run_test(questions):
    #we want to loop through each question, ask it to the user, get the answer, and check to see if right
    #we need to keep track of the user score
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)
