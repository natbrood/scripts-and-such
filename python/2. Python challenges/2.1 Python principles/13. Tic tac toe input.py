# https://pythonprinciples.com/challenges/Tic-tac-toe-input/

# Version 1
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(tac):
    #This converts the letter to number
    letter = int(''.join(map(str,[ord(char) - 96 for char in tac[:1].lower()])))-1
    number = int(tac[1:])-1
    return (number, letter)

get_row_col("A3")


# Version 2
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

def get_row_col(tac):
    return (int(tac[1:])-1,sum([ord(char) - 96 for char in tac[:1].lower()])-1)

get_row_col("A3")


# Solution from site
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)