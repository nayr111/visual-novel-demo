# --- CHARACTER DEFINITIONS ---
define p = Character('Protagonist', color="#3e54e8")
define d = Character('The Drawing', color="#e1e4e6")
define n = Character(None) # Internal narrator, no name displayed

# -- SENSORY ADAPTATION STATE (Second-Time Rule) ---
# Exposure counts track iterative emergence (0 = unformed, 1 = raw input, 2+ = conscious processing)
default sound_exposure = 0
default touch_exposure = 0
default sight_exposure = 0
default smell_exposure = 0
default taste_exposure = 0

# --- MAIN STORY START ---
label start:
    # - PHASE 1 PART 1 -
    label phase_1_part_1:
    scene black
    with fade
    
    n "A character walks into their room, and boots up their computer."
    n "They turn on a digital art program, and start to draw."
    n "They decide to draw a monochrome character, perhaps for their visual novel project?"
    # - CHOICE 1: LOOK -
    n "CHOOSE YOUR LOOK:"
    menu:
        "FUNNY":
            pass
        "COOL":
            pass
        "NEUTRAL":
            pass
    # - CHOICE 2: PERSONALITY -
    n "CHOOSE YOUR PERSONALITY:"
    menu:
        "TALKGPT":
            pass
        "LIBRA":
            pass
        "MONET":
            pass
    # - CHOICE 3: CONFIRMATION -
    n "ARE YOU SURE?"
    menu:
        "YES":
            pass
        "NO":
            pass
    n "The character starts to draw..."


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return