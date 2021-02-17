import click, inquirer
from . import theme, questions

from colorama import init, Fore, Style
init()

@click.group()
def cli():
    pass

@click.command()
@click.option('--multiple-choice/--free-response', default=False, type=bool, help='Should the quiz be multiple choice or not.')
def quiz(multiple_choice):
    # Loop 5 times
    quiz_questions=[]
    for i in range(4):
        quiz_questions.append(questions.random_question(multiple_choice))
    
    correct_answers = 0
    for entry in quiz_questions:
        answer = entry['answer']
        submission = inquirer.prompt([entry['question']], theme=theme.theme())
        
        if (submission['input'] == str(answer)): 
            correct_answers += 1
            print(Fore.GREEN + Style.BRIGHT + 'Correct!' + Fore.RESET)
        else:
            print(Fore.RED + Style.BRIGHT + f'Incorrect, the correct answer was {answer}' + Fore.RESET)
        
    print(Fore.RESET+'You scored ' + Fore.GREEN + Style.BRIGHT + str(correct_answers) + '/5')
    

cli.add_command(quiz)

if __name__ == '__main__':
    cli()