vowels = ['a','e','i','o','u']
sen= raw_input("give me a sentence")
for x in sen:
    if x.lower() in vowels:
        sen=sen.replace(x,"")
print sen
