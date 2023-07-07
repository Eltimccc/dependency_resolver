from pydantic import BaseSettings
import yaml


class Settings(BaseSettings):
    app_title: str = "Dependency resolver"
    description: str = "Тестовое задание перед собесом"


settings = Settings()

with open("builds/tasks.yaml") as tasks_file:
    tasks = yaml.safe_load(tasks_file)

with open("builds/builds.yaml") as builds_file:
    builds = yaml.safe_load(builds_file)
