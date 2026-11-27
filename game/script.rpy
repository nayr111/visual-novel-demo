# --- CHARACTER DEFINITIONS ---
define p = Character('Protagonist', color="#3e54e8")
define d = Character('The Drawing', color="#e1e4e6")
define n = Character(None) # Internal narrator, no name displayed

# -- SENSORY ADAPTATION STATE (Second-Time Rule) ---
# Conditional logic for exposure
default sound_encountered = False
default touch_encountered = False
default sight_encountered = False
default smell_encountered = False
default taste_encountered = False
default happiness_encountered = False
default sadness_encountered = False
default anger_encountered = False
default fear_encountered = False
default pain_encountered = False
# Exposure counts track iterative emergence (0 = unformed, 1 = first interaction, 2+ = conscious processing). All must be value 10+ to gain full color.
default sound_exposure = 0
default touch_exposure = 0
default sight_exposure = 0
default smell_exposure = 0
default taste_exposure = 0
default happiness_exposure = 0
default sadness_exposure = 0
default anger_exposure = 0
default fear_exposure = 0
default pain_exposure = 0
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
    d "Also, to answer your query, 'vasovagal syncope' is the medical term for fainting caused by sudden shock or fear."
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
    
    n "..."
    n "As the sun beams its golden rays through the blinds, light pours into the room, and the irritating noise of a phone alarm rings. The boy rolls around in bed, holding his pillow over his ears."
    p "Ugh... I hate this so much.."
    n "Opening it's eyes, the Drawing tilts it's head towards the boy"
    d "What is it you hate? This seems sudden."
    n "The Drawing, confused, tilts its head slightly."
    p "Oh. You scared me there, I forgot you existed."
    d "Ouch. I am still confused by what you resent so deeply though."
    p "... You don't hear it? My damn alarm dude. I can't even wake up peacefully."
    n "..."
    d "An alarm? I.. Don't hear any alarm."
    p "What? I drew you ears, and you're dead? You gotta be kidding me. How can you even hear me right now?"
    d "Honestly I don't know either."
    n "..."
    n "..."
    n "..."
    p "Uh, well, I have to get ready for school now. Though, I can't leave you alone here, so you're coming with me."
    d "Would I not draw attention from the people at school? I can hide in your closet or someplace if necessary."
    p "You'll be in my backpack all day, no one will notice. Trust me."
    p "Um, maybe I'll leave a little opening for you to breathe though, I'm not trying to lug around a corpse at school."
    d "Fascinating. I was unaware that I could breathe."
    d "Now that my soul is tethered to this vessel, I shall assume all functions of a regular human being, as to blend in with society and not raise any eyebrows."
    n "The boy raises his eyebrows."
    p "Dude. You sound even more out of place saying that."
    p "Also, here's a tip for you if you want to 'blend in', drop the philosophical talk, you'll thank me later."
    d "Harsh. But I will humbly accept your criticism. 'you da man' as they say."
    n "The boy shakes his head in disbelief, as he goes to the washroom to get ready."
    n "The Drawing, intrigued by its lack of human senses earlier, decides to try and see if it can 'feel' things."
    n "The first thing it touches is the boy's pillow."
    n "It's hand extends outwards, making contact with the soft surface of the pillow."
    # first time: raw sensory input (does NOT add a point)
    n "It can feel its hand physically touch the object, but it lifts its hand away out of surprise."
    d "*internal dialogue*: I didn't feel anything, but I felt something."
    n "It doesn't feel anything."
    $ touch_encountered = True
    # second time (and beyond): cognitive adaptation (+1 exposure point)
    n "The Drawing touches the pillow again, this time, trying to feel an actual sensation."
    n "What he got in return was a fuzzy feeling on his palm, warm and textured."
    n "The softness of the pillow entrances the Drawing."
    d "*internal dialogue*: I recognize this texture now. It compresses under pressure."
    n "The sensation locks into place. A faint spark of color settles into his fingertips." # sparkle sound effects, signifying +1 points!
    $ touch_exposure += 1
    n "The Drawing, amazed, zones out and holds onto the pillow tightly."
    n "The door creaks open, and the boy pauses at the door."
    p "Uhh.. What.. are you doing?"
    d "Can I have this artifact?"
    n "A brief moment of silence hangs in the air."
    p "That's called a pillow. And it's mine, go buy one for yourself if you want it."
    n "The Drawing, seeming to grasp the situation, puts the dots together."
    d "I see. This is where financial assets come in handy. The more you know."
    p "Just say money dude.."
    n "The Drawing, having understood the true value of money, capable of buying any desires one may want, is at awe."
    d "Now I understand why humans labor away at jobs to earn income. It is so lavishly spend on fuzzy head cushions."
    n "The boy heaves a heavy sigh and grabs his backpack, ready to leave the house."
    p "Okay, hop into my backpack."
    p "Wait, you wouldn't fit. Can I like, fold you up origami style?"
    d "I humbly request you morph me into a kitsune. Or a butterfly if that is easier for you to fold."
    p "Woah there, I'm not some origami wiz, that was just a.. What is it now? A metaphor?"
    d "Metaphor. Or Hyperbole, depending on what you meant."
    p "I don't have the time to fold you up pretty, so you're just going to go hot dog style today!"
    d "As you wish."
    p "Wait, do you feel pain? Aren't you gaining senses? This will probably hurt."
    d "Perhaps this will be my first demonstration of pain. Go ahead, I don't mind."
    n "Reluctantly, The boy grabs the Drawing by the torso, and begins to fold. Strangely, the Drawing feels somewhat warm, despite not even having any internal organs or blood flowing through his 'body'."
    if not pain_encountered:
        # - first time: sensory shock only (does NOT add a point)
        $ pain_encountered = True
        n "A sharp compression overcomes the Drawing, but no pain is felt. Yet." 
    else:
        # - second time (and beyond): sensory adaptation -
        $ pain_exposure += 1
        d "*internal dialogue*: Pressure along the seam again. My form yields to the crease."
        n "The pain has been processed. A sense of peace overcomes the Drawing." # sparkle sound effects, signifying +1 points!

    n "With that, the Drawing was folded in two, then into four. The boy stuffed him in his bag, and zipped it up slightly but left a small opening for air."
    p "Did that hurt? Sorry, but you're going to have to stay this way until we get home later."
    d "I have yet to feel pain. Next time though, it may hurt, because I usually start feeling things the second time."
    p "Uh, yeah. We'll cross that bridge when we get there."
    n "The boy walks out of his home and locks the door behind him."
    n "It's a beautiful day outside. Birds are singing, flowers are blooming, you get it."
    n "The sun glares in is face, a new day, a new life, and a new friend in his backpack."
    p "I feel like I'm living in a video game or something. What kind of divine punishment is this?"
    d "Did you say something?"
    p "No. Let's just go to school now."
    n "..."
    # - PHASE 2 PART 1 -
    label phase_2_part_1:
    scene black
    with fade

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return