#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


PLACEHOLDER = '[name]'
with open('./Input/Names/invited_names.txt') as names:
    names = names.readlines()


with open('./Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

    for name in names:
        striped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, striped_name)
        with open(f'./Output/ReadyToSend/Letter_for_{striped_name}', 'w') as complete_letter:
            complete_letter.write(new_letter)
        