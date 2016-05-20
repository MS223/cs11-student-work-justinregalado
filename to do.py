action=""
day=""
list_dictionary={
    "monday":[],
    "tuesday":[],
    "wednesday":[],
    "thursday":[],
    "friday":[],
    "saturday":[],
    "sunday":[],
}
def add():
    list_dictionary[day].append(action)

while action!= "exit":
    action=raw_input("what would you like to do today ")
    day=raw_input("what day ?")
    add()


print list_dictionary

# i keep on getting error and its acting up like really acting up :'(
