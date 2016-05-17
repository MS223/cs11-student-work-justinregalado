text_input = raw_input("Paste your text here")
text_input=text_input.lower().replace("."," ")#here im revoming the spaces and peorids and also it will not brake when it comes acorss a upercase 
text_input=text_input.split()#here im removing the spaces and stuff
my_dictionary={}
for x in text_input:
    my_dictionary[x]=my_dictionary.pop(x,0)+1#tnh idk wat i did here it was hard work
print my_dictionary
key_word= raw_input("what word do you want to look for?")
print my_dictionary[key_word]
