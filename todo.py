tasks = []
print("===== TO-DO LIST =====")
while True:
    task = input("Enter a task (or type 'exit'): ")
    if task.lower() == "exit":
        break
    tasks.append(task)
print("\nYour Tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
print("\nThank you for using the To-Do List!")
