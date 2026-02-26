#!/usr/bin/env python3
import argparse
import sys
import yaml
from datetime import datetime


def load_tasks(path="tasks.yaml"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            return data
    except FileNotFoundError:
        return {}


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for key, val in tasks.items():
        name = val.get("name", key)
        desc = val.get("description", "")
        if desc:
            print(f"- {key}: {name} — {desc}")
        else:
            print(f"- {key}: {name}")


def run_task(name, tasks):
    if name not in tasks:
        print(f"Task '{name}' not found.")
        return 1
    t = tasks[name]
    action = t.get("action", "echo")
    if action == "echo":
        print(t.get("message", f"Running {name}"))
    elif action == "time":
        print(datetime.now().isoformat())
    elif action == "shell":
        import subprocess
        cmd = t.get("cmd")
        if cmd:
            subprocess.run(cmd, shell=True)
        else:
            print("No cmd specified.")
            return 2
    else:
        print("Unknown action.")
    return 0


def main():
    parser = argparse.ArgumentParser(prog="boss-task")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list", help="List available tasks")
    p_run = sub.add_parser("run", help="Run a task")
    p_run.add_argument("task_name", help="Name of the task to run")

    args = parser.parse_args()

    tasks = load_tasks()

    if args.cmd == "list":
        list_tasks(tasks)
    elif args.cmd == "run":
        rc = run_task(args.task_name, tasks)
        sys.exit(rc)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
