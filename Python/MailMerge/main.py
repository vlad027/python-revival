#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    stripped_name = name.strip()
    personalized_letter = letter_template.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output_file:
        output_file.write(personalized_letter)