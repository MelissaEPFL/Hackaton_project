from aw_client import ActivityWatchClient
import socket

import datetime



def get_time_spent(target)->str:

    # Connect to the local ActivityWatch server
    client = ActivityWatchClient(client_name="aw-watcher-window", host="localhost", port=5600)

    # Get the events for Visual Studio Code
    events = client.get_events(bucket_id = "aw-watcher-window_"+get_computer_name())

    # Calculate the total time spent on Visual Studio Code
    time_spent = 0

    for event in events:
        if event["data"]["app"] == get_target_name(target):
            time_spent += event["duration"] / datetime.timedelta(minutes=1)

    return str(time_spent)


def get_computer_name()->str:
    return socket.gethostname()


def get_target_name(name_app:str)->str:

    if name_app == 'vscode':
        return "devenv.exe"
 