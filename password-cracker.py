import os, json, time

def clearScreen(cls, timer, stop):
    time.sleep(timer)
    os.system(cls)

    if stop.lower() == "true":
        os.abort

    else:
        pass

clearScreen("cls", 0.1, "False")
condition = input(str("Type OK if you're ready to start: "))

if condition.lower() == "ok":
    passwordList = input(str("Enter the list's name without specifying the file's extension: ")) + ".txt"
    clearScreen("cls", 1.5, "False")

if os.path.exists(passwordList):
    jsonFile = input(str("File successfully found, specify the file that needs to be compared: ")) + ".json"
    clearScreen("cls", 1.5, "False")

    with open(jsonFile ,"r") as file:
        jsonData = json.load(file)

    # nome_value = jsonData["Password"]
    # print("Password :", nome_value)

    for i in jsonData:
        print(i + " : " + jsonData[i])

    with open(passwordList, "r") as password_file:
        passwords = password_file.read().splitlines()

    if jsonData["Password"] in passwords:
        print("\nPassword successfully found : ", jsonData["Password"])
    else:
        print("Password not found")


    clearScreen("cls", 10, "True")

else:
    print("Wrong file path, if this error keeps showing the file might not exist")