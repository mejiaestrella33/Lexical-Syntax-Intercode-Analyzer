#This file contains the Lexical Analyzer function which will help analyze a files content and define each lexemes token.

import string

class LexicalAnalyzer:

#Constructor function, that takes in the list of lexemes to be analyzed
    def __init__(self, lexeme_list):
        self.lexeme_list = lexeme_list

#Creates the list of tokens that will be returned
    def setup_table(self):
        token_list = []
        #Send each lexeme in lexeme_list to the analyze function
        # places the returned token into token_list in the same location as its corresponding lexeme
        for x in self.lexeme_list:
            token = self.analyze(x)
            token_list.append(token)
        return token_list

#Takes in a lexeme to analyze and returns the token of said lexeme
    def analyze(self, lexeme):
        #Lists of the separators, operators, and keyword tokens
        separators = ['(', ')', '{', '}', '[', ']', ',', '.', ':', ';']
        operators = ['*', '+', '-', '=', '/', '>', '<', '%']
        keywords = ["int", "float", "bool", "true", "false", "if", "else", "then", "endif", "endelse", "while", "whileend",
                    "enddo", "for", "endfor", "STDinput", "STDoutput", "and", "or", "not"]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alphabet = string.ascii_letters
        #Dictionary of states which will be assigned to passed in lexeme
        states = {
            1: "Letters    ",
            2: "KEYWORD    ",
            3: "IDENTIFIER ",
            4: "SEPARATOR  ",
            5: "OPERATOR   ",
            6: "Number     ",
            7: "INTEGER    ",
            8: "REAL       ",
            9: "UNKNOWN    "
        }

        #Set lexeme to unknown as default starting state
        lexeme_state = 9
        #Goes through possible states until the correct state is assigned
        if lexeme[0] in alphabet or lexeme[0] == "_":
            lexeme_state = 1
        elif lexeme in separators:
            lexeme_state = 4
        elif lexeme in operators:
            lexeme_state = 5
        elif lexeme[0] in numbers:
            lexeme_state = 6
        else:
            lexeme_state = 9

        #Finds the proper token for those in the letters state
        if lexeme_state == 1:
            temp = lexeme
            if temp.find('$') != -1:
                temp = temp.replace('$', '')
            iden = temp.isidentifier()
            if lexeme in keywords:
                lexeme_state = 2
            elif iden is True:
                lexeme_state = 3

        #Find the proper token for those in the numbers state
        if lexeme_state == 6:
            if '.' in lexeme:
                lexeme_state = 8
            else:
                lexeme_state = 7
        #Returns the found token name
        return states[lexeme_state]

