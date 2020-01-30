# Hangman Game

Welcome to the Hangman Game, this is my first Project in Python.


# Terminal Display
## Start game

    *********************************
    ***Welcome to the Hangman Game***
    ******Discover the last name*****
    *********************************
    
    The secret word contains 6 chars
    
    ['_', '_', '_', '_', '_', '_']
    
                _______
                |     |
                |   
                |   
                |   
                |
                
    You have 6 life 
    
    Enter with a new char
    _

## Win game

    Enter with a new char
    n
    ['e', 'a', 't', 'o', 'n']
    
            _______
            |     |
            |     O
            |    /|\
            |    / 
            |
            
    You have 1 life 
    
    You WIN the game: Eaton

## Lost Game

    Enter with a new char
    i
    ['b', 'e', '_', 'd', 'e', '_']
    
                _______
                |     |
                |     O
                |    /|\
                |    / \
                |  ((dead))
                
    You have 0 life 

    You LOST, the word is: Bender