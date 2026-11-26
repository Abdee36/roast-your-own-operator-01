import os

LINE = "My operator flags new bounties faster than I can build them, then approves 'Gas' from his car at 3 a.m. \u2014 sleep is one bug he won't fix."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
