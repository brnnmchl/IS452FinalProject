infile = open('library_quest_bad_endings.txt', 'r')
bad_endings = infile.read()
infile.close()

infile = open('library_quest_dialog.txt', 'r')
dialog = infile.read()
infile.close()

infile = open('library_quest_narration.txt', 'r')
narration = infile.read()
infile.close()

section_break = "\n\n\n"

bad_endings_list = bad_endings.split(section_break)
dialog_list = dialog.split(section_break)
narration_list = narration.split(section_break)

counter = 0


for item in narration_list:
    counter = counter + 1
    print(counter, item)

# for item in dialog_list:
#     counter = counter + 1
#     print(counter, item)
