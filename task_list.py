tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#1
print("1-------")
def uncompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task["description"])
uncompleted_tasks()

print(" ")

#2
print("2-------")
def completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task["description"])
completed_tasks()   

print(" ")

#3
print("3-------")
def all_task_descriptions():
    for task in tasks:
        print(task["description"])
all_task_descriptions()    

print(" ")

#4
print("4-------")
def timed_tasks():
    for task in tasks:
        if task["time_taken"] > 10:
            print(task["description"])
timed_tasks()

print(" ")

#4.1
print("4.1-------")
def timed_task(mins):
    for task in tasks:
        if task["time_taken"] >= mins:
            print(task["description"])
timed_task(50)            

print(" ")

#5
print("5-------")
def given_description(a):
    for task in tasks:
        if task["description"] == a:
            print(task)
given_description("Walk Dog")


print(" ")

#6
print("6-------")
def mark_completed(a):
    for task in tasks:
        if a == task["description"]:
            task["completed"] = True
            

mark_completed("Feed Cat")
print(tasks)

print(" ")

#7
print("7-------")
def add_new_task(task, status, time):
    tasks.append({"description" : task, "completed" : status, "time_taken" : time})
    print(tasks)

add_new_task("gym", False, 60)    




# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Which Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")