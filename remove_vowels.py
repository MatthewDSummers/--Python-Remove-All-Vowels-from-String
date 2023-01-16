def remove_vowels(string):
    consonant_list = []
    for char in string:
        if char != chr(97) and char != chr(65) and char != chr(101) and char != chr(69) and char != chr(105) and char != chr(73) and char != chr(111) and char != chr(79) and char != chr(117) and char != chr(85):
            consonant_list.append(char)
    string = ""
    for consonant in consonant_list:
        string += consonant
    return(string)

print(remove_vowels("aAeEiIoOuU No vowels!"))
print(remove_vowels("Let's go ahead and remove all these vowels too, okay?"))