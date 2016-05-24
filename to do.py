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
def add(action, day):
    list_dictionary[day].append(action)

def get (day):
    print list_dictionary[day]

def choice():
    user_choice=""
    while user_choice!= "exit":
        user_choice= raw_input("how can i help you")
        if user_choice == "get":
            day=raw_input("what day?")
            get(day)
        elif user_choice == "add":
            action=raw_input("what would you like to add?")
            day=raw_input("what day")
            add(action,day)


choice()

