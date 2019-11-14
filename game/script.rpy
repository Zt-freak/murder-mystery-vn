# The script of the game goes in this file.

# Global Ren'Py variables
define z = Character("???")

transform chapter_fade:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        easeout_back 2 alpha 1
        pause 4
        ease 2 alpha 0.0

# The game starts here.
label start:
    # Global python variables
    # python:
    # Story labels
    jump prologue_start
    return # This ends the game.
