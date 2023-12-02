from aw_client import ActivityWatchClient
import socket

import datetime



def get_time_spent(name_app)->str:

    # Connect to the local ActivityWatch server
    client = ActivityWatchClient(client_name="test-client", host="localhost", port=5600)

    # Get the events for Visual Studio Code
    bucket_id = f"aw-watcher-window_{socket.gethostname()}"
    events = client.get_events(bucket_id = bucket_id)

    # Calculate the total time spent on app
    time_spent = 0.0

    for event in events:
        if event['data']['app'] == get_process_name(name_app):
            time_spent += event["duration"].total_seconds()

    return str(datetime.timedelta(seconds=time_spent))


def get_last_time_on(name_app:str)->str:

    # Connect to the local ActivityWatch server
    client = ActivityWatchClient(client_name="test-client", host="localhost", port=5600)

    # Get the events for Visual Studio Code
    bucket_id = f"aw-watcher-window_{socket.gethostname()}"
    events = client.get_events(bucket_id = bucket_id)

    timestamps = []

    #last time on name_app (events are in order)
    for event in events:
        if event['data']['app'] == get_process_name(name_app):

            timestamps.append(event['timestamp'])
    
    if (len(timestamps) > 0):
        
        last_time = max(timestamps)
        return str((datetime.datetime.now(datetime.timezone.utc) - last_time))
    else:
        return "No use of " + name_app + " since you turned your computer on"
    


def get_computer_name()->str:
    return socket.gethostname()


def get_process_name(name_app)->str:

    if name_app == 'vscode':
        return  "devenv.exe"
    elif name_app == 'vscode_studio':
        return "Code.exe"
    elif name_app == "thunderbird_mail":
        return "thunderbird.exe"
 

 