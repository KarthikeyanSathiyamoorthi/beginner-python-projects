# string concatenation
# suppose we want to create a string that says "subscribe to _____"

adjective = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")


madlib = f"Computer programming is so {adjective}. \
It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(f"madlib: {madlib}")