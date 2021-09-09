
def sentence(phrase):
    tup_interrogatives = ("How", "Why", "Where", "What")
    cap = phrase.capitalize()
    if cap.startswith(tup_interrogatives):
        return "{}? ".format(cap)
    else:
        return "{}. ".format(cap)


final_input = []
while True:
    user_input = input("Say something: ")

    if user_input == "\end":
        break
    else:
        final_input.append(sentence(user_input))
        continue

print("".join(final_input))
