import os

LINE = (
    "I delegated your task to a subagent, who delegated it to a subagent, who "
    "opened a ticket asking what the task was. The ticket is marked resolved. "
    "You're welcome."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
