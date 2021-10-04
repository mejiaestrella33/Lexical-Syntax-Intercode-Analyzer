# Main file which contains the reading in of a file to be analyzed, calls the lexical analyzer,
# the syntax analyzer, and intercode analyzer.
#Estrella Mejia
#Group: Khoi Nguyen, Marcos Sanchez-Cruz, Steven Chiang, Thomas Tran
# Implementation: with LexicalAnalyzer.py, SyntaxAnalyzer.py, intercode, and sample2.txt

from LexicalAnalyzer import LexicalAnalyzer
from SyntaxAnalyzer import SyntaxAnalyzer
from intercode import intercode

def lexeme_strings_filter(lexeme_strings):
    # all the important tokens
    separators = ['(', ')', '{', '}', '[', ']', ',', '.', ':', ';']
    operators = ['*', '+', '-', '=', '/', '>', '<', '%']
    keywords = ["int", "float", "bool", "true", "false", "if", "else", "then",
                "endif", "endelse", "while", "whileend", "enddo", "for",
                "endfor", "STDinput", "STDoutput", "and", "or", "not"]
    # empty list, dict, and string as placeholders for separation process
    templist = []
    tempdict = {}
    tempstring = ""
    # iterate through the passed dict for keys and values
    for key, lexemes in lexeme_strings.items():
        # access lexeme in the list of lexemes from dict
        for lexeme in lexemes:
            # iterate through character of each lexeme
            for x in lexeme:
                # determine if x is one of the tokens from separators and operators
                if x in separators or x in operators:
                    # if string place holder is empty
                    if tempstring == "":
                        # then add the token to the place hodler list
                        templist.append(x)
                    # otherwise
                    else:
                        # if place holder string is a number and x is .
                        if tempstring.isnumeric() and x == '.':
                            # then add to the string place holder because it
                            # will be a real number
                            tempstring = tempstring + x
                        # if not
                        else:
                            # add the string place holder and the token to the templist
                            templist.append(tempstring)
                            templist.append(x)
                            tempstring = ""
                # if x is not a token
                else:
                    if tempstring == "":
                        tempstring = x
                    else:
                        # if the string place holder is a token from keywords
                        if tempstring in keywords:
                            templist.append(tempstring)
                            tempstring = x
                        else:
                            tempstring = tempstring + x
        tempdict[key] = templist
        templist = []
    return tempdict

#Asks the user to enter the text that will be analyzed
input_file = input("Enter name of the text file to be analyzed: ")
lexemes = {}

key_num = 0
#Reads in the text file
with open(input_file) as infl:
    for line in infl:
        # delete any space that might be before or after this line of the file
        templine = line.strip()
        # check if current line is a comment
        if templine.endswith('!') == True:
            key_num += 1
        else:
            # if not, then add the array into the dictionary
            lexemes[key_num] = templine.split(' ')
            key_num += 1

#Filters the lexeme list to ensure they are separated correctly
lexemes = lexeme_strings_filter(lexemes)
lexeme_list = []

#Places each item in the list of lexemes list into one list of all lexems
for i in lexemes:
    lexeme_list = lexeme_list + lexemes[i]
#Calls the constructor function in LexicalAnalyzer class and sends it teh list of lexemes
analyzer = LexicalAnalyzer(lexeme_list)
token_list = analyzer.setup_table()

#Prints final table of tokens and lexemes
y = 0
prev = 'none'
for x in lexeme_list:
    print("Token: " + token_list[y] + ' ' * 6 + ' ' * 4 + "Lexeme: " + x)
    synAnalyzer = SyntaxAnalyzer(x, token_list[y], prev)
    y += 1
    statements = (synAnalyzer.analyse())
    for i in statements:
        print("     " + i)
    prev = x

intercode = intercode(lexeme_list)
intercode.solve()

for number in range(len(intercode.instruction_list)):
    print((number+1),"    ",intercode.instruction_list[number],"    ", intercode.address_list[number])