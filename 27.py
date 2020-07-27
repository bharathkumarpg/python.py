names = []
for i in range(10):
    name = input("enter the name")
    if name not in names:
        names.append(name)
    else:
        print("please enter unique name")

print(names)








