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
    
    n "A boy walks into his room, and boots up his computer."
    n "He turns on a digital art program, and starts to draw."
    n "He decides to draw a monochrome character, perhaps for his visual novel project?"
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
    n "The boy starts to draw..."
    n "..."
    n "..."
    n "..."
    p "*yawn* I'm going to go get a glass of water.."
    n "The boy exits the room."
    n "A few moments pass by..."
    n "The rain pours harder.. then.."
    n "!BOOM!"
    n "*lights flicker*"
    n "*the computer starts to turn on and off*"
    n "*a large stream of light bursts out of the computer*"
    n "..."
    n "The boy walks back into the room."
    n "..."
    p "What in the... What is this? Who are you..?"
    p "*internal dialogue*: Did my drawing just... Come to life!!??!?"
    n "The drawing stares at the boy."
    d "Awaiting input. What is your name?"
    p "Wh-wha-!"
    n "The boy collapses onto the ground..."
    n "..."    
    # - PHASE 1 PART 2 -
    label phase_1_part_2:
    scene black
    with fade
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return