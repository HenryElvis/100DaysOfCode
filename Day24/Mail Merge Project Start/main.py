names = []

with open("Input/Names/invited_names.txt") as name:
    content = name.readlines()

for name in content:
    name = name.strip("\n")
    names.append(name)

with open("Input/Letters/starting_letter.txt") as lt:
    letter = lt.read()

for name in names:
    new_letter = letter
    new_letter = new_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_ready_{name}.txt", mode="w") as lt:
        lt.write(new_letter)