tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#1
def uncompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task["description"])
uncompleted_tasks()

print(" ")

#2
def completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task["description"])
completed_tasks()   

print(" ")

#3
def all_task_descriptions():
    for task in tasks:
        print(task["description"])
all_task_descriptions()    

print(" ")

#4
def timed_tasks():
    for task in tasks:
        if task["time_taken"] > 10:
            print(task["description"])
timed_tasks()

print(" ")

#5
def given_description(a):
    for task in tasks:
        if task["description"] == a:
            print(task)
given_description("Walk Dog")

