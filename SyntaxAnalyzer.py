# A syntax analyzer, using a top-down parser

class SyntaxAnalyzer:
    # Constructor function, that takes in a lexeme anf its token in order to syntactically analyze
    def __init__(self, lexeme, tokenType, prev='none'):
        self.lexeme = lexeme
        self.token = tokenType
        # The rules that have been assigned to the specific lexeme
        self.rules = []
        self.previous = prev
        # The table of possible rules
        # Sets up the table of rules, in a dictionary format
        self.ruleset = {
            "a": "Statement",
            "b": "Term",
            "c": "Factor",
            "d": "Prime",
            1: "<Statement> -> <Declarative>",
            2: "<Statement List> -> <Statement> | <Statement> <Statement List>",
            3: "<Statement> -> <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>",
            4: "<MoreStatements> -> ; <Statement> <MoreStatements>| <empty>",
            5: "<Declarative> -> <Type> <id>",
            6: "<Declarative> -> <Type> <ID> <MoreIds>; | <empty>",
            7: "<Declarative> -> <Type> <ID> <MoreIds>; | <empty>",
            8: "<ID> -> id",
            9: "<MoreIds> -> , <ID> <MoreIds>| <empty>",
            10: "<Expression> -> <Term> <Expression Prime>",
            11: "<ExpressionPrime> -> + <Term> <ExpressionPrime> | - <Term> <ExpressionPrime> | <Empty> ",
            12: "<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>",
            13: "<Term> -> <Factor> <Term Prime>",
            14: "<Type> -> int | float | bool",
            15: "<Type> -> int | float | bool",
            16: "<Factor> -> - <Primary> | <Primary>",
            17: "<TermPrime> -> * <Factor> <TermPrime> | / <Factor> <TermPrime> | <Empty>",
            18: "<Primary> -> <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false",
            19: "<Assign> -> <ID> = <Expression>;",
            20: "<Conditional> -> <Expression> <Relop> <Expression>| <Expression>",
            21: "<Empty> -> Epsilon"
        }
    #Does the actual analyzing of the each lexeme with considering what the previous lexeme was
    def analyse(self):

        if self.lexeme == '=':
            return []
        if self.previous == "none" and self.token == "IDENTIFIER ":
            self.rules.append(self.ruleset[2])
            self.rules.append(self.ruleset["a"])
        elif self.token == "IDENTIFIER ":
            self.rules.append(self.ruleset["b"])
        if "Statement" in self.rules or self.previous == ';':
            self.rules.append(self.ruleset[3])
            self.rules.append(self.ruleset[19])
            if "Statement" in self.rules:
                self.rules.remove("Statement")
        if self.previous == "=" and "Term" in self.rules:
            self.rules.append(self.ruleset[10])
        if "Term" in self.rules:
            self.rules.remove(self.ruleset["b"])
            self.rules.append(self.ruleset[13])
            self.rules.append(self.ruleset[16])
            self.rules.append(self.ruleset[18])
        if self.token == "OPERATOR   " or self.token == "SEPARATOR  ":
            self.rules.append(self.ruleset[21])
            self.rules.append(self.ruleset[17])
            self.rules.append(self.ruleset[21])
            self.rules.append(self.ruleset[11])
            if self.lexeme == ";":
                self.rules.append(self.ruleset[21])

        return self.rules
