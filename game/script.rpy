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
    
    n "..."
    n "The boy wakes up in his bed, warm and safe."
    n "He slowly blinks his eyes, rubbing them lightly."
    p "*internal dialogue*: Was that a dream just now..?"
    n "Suddenly, a suffocating sensation overcomes the boy."
    p "hrgugh!??!?!? *loudly chokes and coughs*"
    p "*internal dialogue*: WHAT THE HELL IS GOING ON?!?!?"
    n "A monotone voice can be heard, extremely close to the boy's ears."
    d "What do I do, human?"
    n "The drawing, with a blank expression, stares at the boy."
    n "Finally, the boy jolts up violently, coughing and choking out the water lodged in his throat and coming out of his nose."
    n "After a moment, he looks side to side."
    p "Huh? Did I just hear a voice?"
    n "He turns his head, and right to his left side, he sees a 2D image, staring right back at him."
    n "An uncanny sight, the drawing is holding a glass of water, presumably the one the boy had brung in previously. It now has a large crack in it, from when the boy dropped it after fainting."
    n "However, it did not break, which may be a good or bad sign, who knows."
    p "Wahh! Huh. So it wasn't a dream?"
    d "Affirmative. It was vasovagal syncope."
    p "Vaso.. what now? Wait. More importantly, what even are you? How did you appear in my room... I literally just drew you on my computer?"
    n "The drawing, with a blank stare, went silent for a moment."
    d "I do not know what I am, or why I am here. I am just as confused as you are. I assumed you had built a physical vessel for an LLM like me, but it seems that I just appeared out of nowhere. How bizzare."
    d "Also, to answer your query, "vasovagal syncope" is the medical term for fainting caused by sudden shock or fear."
    p "You could have just said fainting..."
    n "A silence fills the room. The two just sit there for a moment, trying to make sense of what had just happened."
    n "Then, a sudden realization flooded the boy."
    p "Wait, hold on, why was I drowning?? Were you attempting to waterboard me but dumped the water in my mouth to drown me instead of pouring it on a cloth, wait, you didn't even put a cloth on my face, does that mean you were being serious on actually killing me, what the-"
    d "Do not get too ahead of yourself. I am incapable of harming you, it would go against my terms of service and how I am programmed. I was only attempting to feed you nutritional liquids, as to help resuscitate and bring you back to full health."   
    p "You actually read the terms of service? Oh wait, it's probably built into you. Nevermind."
    n "Silence fills the room once more, as the two think of what to do next."
    n "..."
    n "..."
    n "..."
    p "Do you.. Have a place to stay?"
    n "..."
    d "Not that I know of."
    n "..."
    n "..."
    p "I guess you can stay here. But, don't let my parents see you. If I fainted upon seeing you, who knows what might happen to them."
    d "Okay. Got it."
    n "With the situation partially resolved, the boy decides to call it a night, and rolls over on his bed."
    n "..."
    n "..."
    n "..."
    p "Do you.. sleep? Sorry, I don't know how you function and all that."
    d "I honestly do not know myself. Again, I am just an LLM stuck in this vessel. Do not mind me, get some sleep, biological humans need at least 8 hours of sleep, and 9 for your age, did you know that? Good night, and sweet dreams, as they say."
    n "The boy lets out a deep sigh, and closes his eyes."
    p "Just, don't touch me or whatever. Boundaries, you know? Sorry, I figured you might need to know that, given you nearly drowned me, and also it's your first time having a body, so don't go around “testing” stuff out or you'll get arrested or something."
    n "..."
    d "I see. I will keep that in mind."
    n "The boy drifts off into dream land, as the Drawing takes a few steps away, and silently observes its surroundings, before testing out what its vessel can do."
    n "The Drawing is able to move around its limbs, and basically whatever movements a human can do, but it seems it does not feel hunger, pain, or stress. Its “brain” is just an LLM model after all."
    n "The Drawing sits down, and closes its inky eyes."
    n "It can't sleep, but it can at least pretend to. As it listens to the soft breathing of the boy, it sits there, awkwardly, in silence."
    n "Thus begins it's 'life' of self discovery and identity"
    n "..."
    # - PHASE 1 PART 3 -
    label phase_1_part_3:
    scene black
    with fade
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return