import os
import subprocess

def run_command(command):
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

run_command("pip install -r requirements.txt")

# Применение миграций
run_command("python manage.py migrate")

# Сбор статики
run_command("python manage.py collectstatic --noinput")
