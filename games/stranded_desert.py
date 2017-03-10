# kids puzzle game

print """You wake up on the side of a road in the desert.
It's very hot and you don't see anyone in sight."""

print "What do you do?"
print "1. Walk alongside the road, looking for help."
print "2. Stay put and wait for help."
print "3. Panick and just start running in any direction."

walk = raw_input("> ")

if walk == "1":
    print "A vehicle in the distance is fast approaching"
    print "What do you do?"
    print "1. Wave them down."
    print "2. Run and hide."

    car = raw_input("> ")
    if car == "1":
        print "The vechile drives even faster and runs you over! You're dead X_X"
    elif car == "2":
        print "They keep driving and you're stuck in the middle of nowhere. Good job."
    else:
        print "Good choice, but why are you even in the desert."

elif walk == "2":
    print "A big vulture flies down and sits right next to you!"
    print "What do you do?"
    print "1. Attack the vulture before it attacks you."
    print "2. Run away from it as fast as you can!"

    vulture = raw_input("> ")
    if vulture == "1":
        print "The vulture flies away in horror."
    elif vulture == "2":
        print "The vulture attacks you and pecks your eyes out \nleaving you blind and helpless. Good job!"
    else:
        print "That's what I would've done, but you're still stuck in the desert."

elif walk == "3":
    print "You fall down from dehydration and exhaustion!"
    print "Really? you were in the desert!"

else:

    print "Please pick an option between 1 and 3."
