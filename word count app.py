text_input = raw_input("Paste your text here")
text_input=text_input.lower().replace("."," ")
text_input=text_input.split()
my_dictionary={}
for x in text_input:
    my_dictionary[x]=my_dictionary.pop(x,0)+1
print my_dictionary
key_word= raw_input("what word do you want to look for?")
print my_dictionary[key_word]
