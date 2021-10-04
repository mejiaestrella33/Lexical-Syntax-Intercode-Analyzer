import string

class intercode:
    def __init__(self, lexeme_list):
        self.lexeme_list = lexeme_list
        self.address_list = []
        self.instruction_list = []

        self.instruction = { 1:"PUSHI",
        2:"PUSHM",
        3:"POPM",
        4:"STDOUT",
        5:"STDIN",
        6:"ADD",
        7:"SUB",
        8:"MUL",
        9:"DIV",
        10:"GRT",
        11:"LES",
        12:"LES",
        13:"EQU",
        14:"NEQ",
        15:"GEQ",
        16:"LEQ",
        17:"JUMPZ",
        18:"JUMP",
        19:"LABEL"}
        self.address = 5000

    def solve(self):
        for y in range(len(self.lexeme_list)):
            if self.lexeme_list[y] == "=" and self.lexeme_list[y+2] == ";":
                self.instruction_list.append(self.instruction[1])
                self.address_list.append(self.lexeme_list[y+1])
                self.instruction_list.append(self.instruction[2])
                self.address_list.append(self.address)
                self.address += 1
            elif self.lexeme_list[y] == "=" and self.lexeme_list[y+2] == "+":
                self.address = 5000
                self.instruction_list.append(self.instruction[2])
                self.address_list.append(self.address)
                self.address += 1
                self.instruction_list.append(self.instruction[2])
                self.address_list.append(self.address)
                self.address += 1
                self.instruction_list.append(self.instruction[6])
                self.address_list.append("")
                self.instruction_list.append(self.instruction[3])
                self.address_list.append(self.address)
                self.address += 1
            
