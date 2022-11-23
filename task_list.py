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


print(" ")
#6
def mark_completed(a):
    for task in tasks:
        if a == task["description"]:
            task["compeleted"] = True
            del(task["completed"])

mark_completed("Feed Cat")
print(tasks)

print(" ")

#7
# def adding_new_task(new_task):
#     for task in tasks:
#         task["description"] = new_task
#         print(task)
    

# adding_new_task("gym")
# Add a task to the list


