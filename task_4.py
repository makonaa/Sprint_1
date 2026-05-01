new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# №1 - moved task_005 from new_tasks list to completed_tasks in one line
completed_tasks.append(new_tasks.pop(-1))

# №2 - removed task_007 from the new_tasks list
new_tasks.remove('task_007')

# №3 - displayed the last task from new_tasks list
print(new_tasks[-1])