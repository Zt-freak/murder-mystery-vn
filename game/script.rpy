# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define z = Character("???")

label start:
# The game starts here.
    call prologue_start from prologue
    call chapter1_start from chapter1
    # This ends the game.

    return
