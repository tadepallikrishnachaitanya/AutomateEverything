# [] -> array

usernames = ['admin', 'manager', 'qa']

for  name in usernames:
    print("Names:", name)


projectTypes = ["HRMS", "IT", "Banking", "Finance"]
dummy = []

for project in projectTypes:
    if project == "Banking":
        continue
    else:
        print(f"Developing Project {project}")
    dummy.append("Banking")
    print(f"Developed: {dummy}")
