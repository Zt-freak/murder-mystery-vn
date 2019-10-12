# The script of the game goes in this file.

# Global variables

define z = Character("???")

transform chapter_fade:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        easeout_back 2 alpha 1
        pause 4
        ease 2 alpha 0.0

label start:
# The game starts here.
    call prologue_start from prologue
    call chapter1_start from chapter1
    # This ends the game.

    return
