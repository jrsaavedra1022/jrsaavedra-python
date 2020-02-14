# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
        'lavadora',
        'secadora',
        'sofa',
        'gobierno',
        'diputado',
        'democracia',
        'computador',
        'teclado'
    ]

def random_word():
    indice = random.randint(0, len(WORDS)-1)
    return WORDS[indice]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- * ---')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input("Escoge una letra: "))
        # verficar si la letra esta la palabra
        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        # varificar los intentos de adivinar letra        
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Lo sentimos, perdiste !!')
                print('La palabra correcta era: {} '.format(word))
                break
        else:
            for i in letter_indexes:
              # llenar la letra
              hidden_word[i] = current_letter
             # vaciar indices 
            letter_indexes = []

        # para saber si ganaste
        try:    
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades !!!')
            print('Ganaste la palabra correcta es: {} '.format(word))
            break    


if __name__ == '__main__':
    print('B I E N V E N I D O S    A   A H O R C A D O S')
    run()