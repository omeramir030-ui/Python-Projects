text = "Can you survive a zombie apocalypse? Test your skills and see if you have what it takes to make it through the undead nightmare. From scavenging for supplies to defending yourself against hordes of zombies, every decision counts. Are you ready to face the challenge?"

askuser = input("Do you want to take the challenge? (yes/no): ")
if askuser.lower() == "yes":
    print("Great! Let's begin your journey through the zombie apocalypse.")
elif askuser.lower() == "no":
    print("Maybe next time!")
    raise SystemExit

q1 = input("What do you know about zombies? (a) They are slow and easy to outrun, (b) They are fast and relentless, (c) They can be cured with medicine: ")
if q1.lower() == "a":
    print("Correct! Zombies are often depicted as slow-moving creatures, but they can still be dangerous in large numbers.")
elif q1.lower() == "b":
    print("Incorrect. While some zombies are portrayed as fast, the classic depiction is that they are slow and can be outrun.")
elif q1.lower() == "c":
    print("Incorrect. There is currently no known cure for zombies in popular culture.")

q2 = input("What is the best way to defend yourself against zombies? (a) Use a weapon, (b) Run away, (c) Hide and wait for help: ")
if q2.lower() == "a":
    print("Correct! Using a weapon is often the most effective way to defend yourself against zombies.")
elif q2.lower() == "b":
    print("Incorrect. Running away might work in some situations, but it's not always a viable option.")
elif q2.lower() == "c":
    print("Incorrect. Hiding and waiting for help is not a reliable strategy against zombies.")

q3 = input("What is most effective place to hit zombies? (a) Head, (b) Arms, (c) Legs: ")
if q3.lower() == "a":
    print("Correct! The head is the most effective place to hit zombies, as it is often depicted as the only way to stop them.")
elif q3.lower() == "b":
    print("Incorrect. Hitting zombies in the arms is not as effective as targeting their head.")
elif q3.lower() == "c":
    print("Incorrect. Hitting zombies in the legs is not as effective as targeting their head.")