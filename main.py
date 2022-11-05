#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


lista = open("Input/Names/invited_names.txt", "r")
attendees_list = lista.readlines()
new_attendees_list = []
for i in attendees_list:
    new_attendees_list.append(i.strip())

def mail_generator():
    for name in new_attendees_list:
        with open("Input/Letters/starting_letter.txt") as file:
            contents = file.read()
            texto = contents.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
            file.write(texto)

mail_generator()





