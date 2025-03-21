import sys
import os
import pickle

CWD = os.getcwd()
PITFOLDER = ".pit"

if len(sys.argv) < 2:
    sys.exit(1)


match sys.argv[1]:
    case "init":
        try:
            os.makedirs(os.path.join(CWD, PITFOLDER))
            with open(os.path.join(CWD, ".pit/tasks"), "wb") as file:
                pickle.dump([], file)
            print("pip initialized empty repo")
        except Exception as e:
            print("Error while init : " + str(e))
    case "task":
        if len(sys.argv) == 2:
            with open(os.path.join(CWD, ".pit/tasks"), "rb") as file:
                tasks = pickle.load(file)
                print(tasks)
                sys.exit(0)
        match sys.argv[2]:
            case "add":
                if len(sys.argv) < 3:
                    sys.exit(1)
                task_name = sys.argv[2]
                tasks = []
                with open(os.path.join(CWD, ".pit/tasks"), "rb") as file:
                    tasks = pickle.load(file)
                tasks.append(sys.argv[3])
                with open(os.path.join(CWD, ".pit/tasks"), "wb+") as file:
                    pickle.dump(tasks, file)
