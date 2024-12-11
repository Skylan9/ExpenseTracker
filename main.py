import time
import json
from pynput import keyboard
import sys

# task properties id, description, status(todo, in-progress, done), createdAt, updatedAt

# Open the file ----------------------------------------------------------------------------------------------------------------------------
def return_file():
    try:
        with open("tasks.json", "r") as task_file:
            content = task_file.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: invalid JSON format")
        return []
# ------------------------------------------------------------------------------------------------------------------------------------------
# Add a task to the list -------------------------------------------------------------------------------------------------------------------
def addTask():
    try:
        
        if userInput[3].isspace() :
            data = return_file()
            lines = len(data)
            for i in data:
                if data[i]["id"] == lines:
                    lines +=1
            if lines == 0:
                lines = 1
            tasksInput = {
                "task{id}".format(id = lines): 
                {
                    "id" : lines,
                    "description": userInput[3:],
                    "status" : "toDo",
                    "createdAt" : time.strftime("%D %T"),
                    "updatedAt" : None
                }
            }
            tasksOutput =  data | tasksInput

            with open("tasks.json", "w") as outfile:
                json.dump(tasksOutput, outfile, indent= 4)
                outfile.close()
            print("---")
            print("Task added successfully! -- {newTask}".format(newTask = userInput[3:]))
            print("---")
        else:
            
            print("invalid task name")
    except: 
        print("Something went wrong, sending you back to the main screen")
    return startScreen()
# ------------------------------------------------------------------------------------------------------------------------------------------
# Update a task ----------------------------------------------------------------------------------------------------------------------------
def updateTask():
    try:
        task_id = int(userInput[7])
        task_description = userInput[9:]
        data = return_file()

        for i in data:
            if data[i]["id"] == task_id:
                oldDescription = data[i]["description"]
                data[i]["description"] = task_description
                data[i]["updatedAt"] = time.strftime("%D %T")
                print(F'The description has been changed from,{oldDescription} to {data[i]["description"]}')

        with open("tasks.json", "w") as outfile:
            json.dump(data, outfile, indent= 4)
    except:
         print("Something went wrong, sending you back to the main screen")
    return startScreen()
# ------------------------------------------------------------------------------------------------------------------------------------------
# Delete a task ----------------------------------------------------------------------------------------------------------------------------
def deleteTask():
    try:
        task_id = int(userInput[7:])
        data = return_file()
        for i in data:
            if data[i]["id"] == task_id:
                    description = data[i]["description"]
                    dataToDelete = i   
        data.pop(dataToDelete)
        with open("tasks.json", "w") as outfile:
            json.dump(data, outfile, indent= 4)
            outfile.close()
    except:
         print("An error occured!")
    else: 
         print(F'Task {task_id} with description: {description} is deleted')

    return startScreen()

def markingTask():
    try:
        data = return_file()
        if userInput[0:16] == "mark-in-progress":
            task_id = int(userInput[17:])

            for i in data:
                if data[i]["id"] == task_id:
                    if data[i]["status"] != "in-progress":
                        data[i]["status"] = "in-progress"
                    else:
                        print("Task is already marked as in-progress")

            with open("tasks.json", "w") as outfile:
                json.dump(data, outfile, indent= 4)

        if userInput[0:9] == "mark-done":
            task_id = int(userInput[10:])
            for i in data:
                if data[i]["id"] == task_id:
                    if data[i]["status"] != "done":
                        data[i]["status"] = "done"
                    else:
                        print("Task is already marked as done")
            with open("tasks.json", "w") as outfile:
                json.dump(data, outfile, indent= 4)
        return startScreen()
    except:
        print("error occurred")
        return startScreen()

# ------------------------------------------------------------------------------------------------------------------------------------------
# Showing a list of all the tasks ----------------------------------------------------------------------------------------------------------
def listTask():
    data = return_file() 
    try:
        if userInput == "list":
            for key, value in data.items():
                print(f"{key}: {value}")
        elif userInput == "list done":     
            for i in data:
                if data[i]["status"] == "done":
                    print(data[i])
        elif userInput == "list todo":
            for i in data:
                if data[i]["status"] == "toDo":
                    print(data[i])
        elif userInput == "list in-progress":
            for i in data:
                if data[i]["status"] == "in-progress":
                    print(data[i])
        return startScreen()
    except:
        print("error occurred")
        return startScreen()
# ------------------------------------------------------------------------------------------------------------------------------------------
def startScreen():                    
    global userInput
    userInput = input("This is your task list! \nUse 'add','update','delete','list','mark-in-progress' or 'mark-done' with corresponding task \nFor help type 'help'\n")
    if userInput.startswith("add"):
        addTask()
    elif userInput.startswith("update"):
        updateTask()
    elif userInput.startswith("delete"):
        deleteTask()
    elif userInput.startswith("list"):
        listTask()
    elif userInput.startswith("mark-in-progress") or userInput.startswith("mark-done"):
        markingTask()

startScreen()






