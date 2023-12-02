from aw_client import ActivityWatchClient
import socket

import datetime



def get_time_spent(name_app)->str:

    # Connect to the local ActivityWatch server
    client = ActivityWatchClient(client_name="test-client", host="localhost", port=5600)

    # Get the events for Visual Studio Code
    watcher = get_watcher(name_app)
    bucket_id = f"{watcher}_{socket.gethostname()}"
    events = client.get_events(bucket_id = bucket_id)

    # Calculate the total time spent on app
    time_spent = 0

    for event in events:
        time_spent += event["duration"] / datetime.timedelta(seconds=1)

           
    return str(time_spent)


def get_computer_name()->str:
    return socket.gethostname()


def get_watcher(name_app:str)->str:

    if name_app == 'vscode_studio':
        return  "aw-watcher-vscode"
    elif name_app == 'last_pause':
        return "aw_watcher_afk"
 