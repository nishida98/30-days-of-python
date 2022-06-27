from formatting import format_msg
from datetime import datetime
import requests
import sys

def send(name, website):
    msg = format_msg(name, website)
    #send the message

    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, "leo.org")
    print(response)