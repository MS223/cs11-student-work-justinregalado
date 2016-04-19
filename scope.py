a = [1, 2, 4]
b = a
# there aint noting happending here

# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
# it replaced 4 with yo

var_1 = "kittens" #global
var_2 = "cookies" #global
# input: a string
# output: a string
def my_function(my_favorite_things):#global
    song_lyrics = "rain drops on roses,"#local
    combined_song = song_lyrics + my_favorite_things#local
    return combined_song#local
# input: a string
# output: a string
def my_function_2(item, item2):#global
    full_lyrics = item + "on " + item2#local
    full_song = my_function(full_lyrics)#local
    return full_song#local
my_song = my_function_2(var_1, var_2)#global
print my_song#global
# the songs got printed


var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    elif favorite_pet == var_2:
        print("My favorite pet is the dog.")
    var_2 = "cat"#bro i changed the if to elif :)

print_out_my_favorite(var_1)
print(var_2)
