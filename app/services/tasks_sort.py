def get_sorted_tasks(build_name, tasks, builds):
    sorted_tasks = []

    build = None
    for item in builds["builds"]:
        if item["name"] == build_name:
            build = item
            break
    if build:
        task_list = build.get("tasks", [])
        dependencies_map = {}
        for task_name in task_list:
            task = None
            for item in tasks:
                if item["name"] == task_name:
                    task = item
                    break
            if task:
                dependencies = task.get("dependencies", [])
                dependencies_map[task_name] = dependencies

        for task_name in task_list:
            add_task_with_dependencies(task_name, dependencies_map, sorted_tasks)

    return sorted_tasks


def add_task_with_dependencies(task_name, dependencies_map, sorted_tasks):
    if task_name in dependencies_map:
        dependencies = dependencies_map[task_name]
        for dependency in dependencies:
            add_task_with_dependencies(dependency, dependencies_map, sorted_tasks)
        del dependencies_map[task_name]
    if task_name not in sorted_tasks:
        sorted_tasks.append(task_name)
