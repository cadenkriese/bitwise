from random import randrange
import inquirer

def random_question(multiple_choice=False):
    bases = [hex, int, bin, oct]
    
    initial_base = bases.pop(randrange(4))
    final_base = bases[randrange(3)]
    
    return generate_question(initial_base, final_base, multiple_choice)
    
def generate_question(initial, final, multiple_choice=False):
    number = randrange(100)

    initialFormatted = initial(number)
    if (initial != int): initialFormatted = initialFormatted[2:]

    finalFormatted = final(number)
    if (final != int): finalFormatted = finalFormatted[2:]

    if (multiple_choice):
        return {
            "question": inquirer.List('input', 
            message=f'What is {initialFormatted} ({function_to_string(initial)}) in {function_to_string(final)}?', 
            choices=scramble([finalFormatted, random_answer(), random_answer(), random_answer()])
        ),
            "answer": finalFormatted
            }
    else:
        return {
            "question": inquirer.Text('input', message=f'What is {initialFormatted} ({function_to_string(initial)}) in {function_to_string(final)}?'),
            "answer": finalFormatted
            }
        
def random_answer():
    base = [hex, int, bin, oct][randrange(4)]
    answer = base(randrange(100))
    if (base != int): answer = answer[2:]
    return answer
    
def scramble(ordered_list):
    scrambled_list = []

    for i in range(len(ordered_list)):
        scrambled_list.append(ordered_list.pop(randrange(len(ordered_list))))
        
    return scrambled_list
    
def function_to_string(func):
    if (func == hex):
        return "Hexadecimal"
    elif (func == int):
        return "Decimal"
    elif (func == bin):
        return "Binary"
    elif (func == oct):
        return "Octal"