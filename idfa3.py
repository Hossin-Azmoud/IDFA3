#! /bin/python3
from sys import argv
from os  import system

def execute_command(command):
    print(f"[!] {command}")
    system(command)

def main():
    
    if len(argv) < 2:
        print(f"[SYNTAX] { argv[0] } `commit_msg`")
        exit(1)
    
    msg = argv[1]

    execute_command("git add .")
    execute_command(f"git commit -m \"{ msg }\"")
    execute_command("git push")

if __name__ == "__main__":
    main()
