#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open( "../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file1:
    file_to_be_edited = file1.read()
    # readlines returns lines of files in list till the bytes given as arguments
    # if -1 is given or nothing is given it returns whole lines of files in the list


with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file2:
    file_lines2 = file2.readlines()
    for lines in file_lines2:
        line = lines.strip("\n")
        temp_file = file_to_be_edited.replace("[name]", line)
        print(temp_file)
         # with open(f"../Mail Merge Project Start/Output/ReadyToSend/To {line}.txt","w") as final_file:
         #     final_file.write(temp_file)


