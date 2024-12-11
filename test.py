import json

inputUser = "mark-in-progress 2"

# task_id = int(inputUser[7:])
# with open("tasks.json", "r") as readfile:
#         data = json.load(readfile)
#         # print(data.items())
# for i in data:
#         if data[i]["id"] == task_id:
#                 print(i)
#                 dataToDelete = i
# data.pop(dataToDelete)
# with open("tasks.json", "w") as outfile:
#         json.dump(data, outfile, indent= 4)
#         outfile.close()

try:
        if inputUser[0:16] == "mark-in-progress":
                task_id = int(inputUser[17:])
                with open("tasks.json", "r") as readfile:
                        data = json.load(readfile)
                for i in data:
                        if data[i]["id"] == task_id:
                                if data[i]["status"] != "in-progress":
                                        data[i]["status"] = "in-progress"
                                else:
                                        print("Task is already marked as in-progress")
                readfile.close()
                with open("tasks.json", "w") as outfile:
                        json.dump(data, outfile, indent= 4)
                        outfile.close()

        if inputUser[0:9] == "mark-done":
                task_id = int(inputUser[10:])
                with open("tasks.json", "r") as readfile:
                        data = json.load(readfile)
                for i in data:
                        if data[i]["id"] == task_id:
                                if data[i]["status"] != "done":
                                        data[i]["status"] = "done"
                                else:
                                        print("Task is already marked as done")
                readfile.close()
                with open("tasks.json", "w") as outfile:
                        json.dump(data, outfile, indent= 4)
                        outfile.close()
except:
        print("error occurred")


