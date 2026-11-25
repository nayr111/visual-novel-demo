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

    scene black
    with fade
    #testing dialogue
    n "Hi, I'm the narrator"
    d "Hi, I'm drawing"
    p "Hi, I'm protagonist"

    return