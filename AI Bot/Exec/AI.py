goodwords = ["hi", "cool", "nice", "good", "perfect", "achievement", "bigger", "biggest", "goodest", "coolest", "hello", "nicest", "lovely", "cute", "cutest", "thank", "thanks", "helped", "qpr", "advice", "wise", "wish", "wished", "wisdom", "acquintance", "enjoy", "happy", "happiness", "kind"]
pronouns = ["I", "you", "he", "she", "they", "them", "we"]
badwords = ["no", "ugh", "bad", "weird", "bad", "horrible", "terrible", "weirdest", "baddest", "scared", "closeted", "scare", "love", "procrastination", "trauma", "stranger", "flirt", "romance", "alone", "killer", "dead", "deadly", "audacity",]

mood = 0
while True:
    usersaid = input("Text: ").lower()


    lenght = len(usersaid)
    word = 0

    for word in goodwords:
     if word in usersaid:
            mood = mood + 1

    for word in badwords:
        if word in usersaid:
            mood = mood - 1

    print(mood)
