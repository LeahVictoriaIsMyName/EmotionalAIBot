goodwords = ["hi", "cool", "nice", "good", "perfect", "achievement", "bigger", "biggest", "goodest", "coolest", "hello", "nicest"]
pronouns = ["I", "you", "he", "she", "they", "them", "we"]
badwords = ["no", "ugh", "bad", "weird", "bad", "horrible", "terrible", "weirdest", "baddest"]

mood = 0
usersaid = input("Text: ").lower()


lenght = len(usersaid)
word = 0

for word in goodwords:
    if word in usersaid:
        mood = mood + 1

print(mood)
