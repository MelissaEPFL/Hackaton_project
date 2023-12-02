from aw_client import ActivityWatchClient
import datetime



def get_time_spent(watcher, bucket_id, target)->str:

    # Connect to the local ActivityWatch server
    client = ActivityWatchClient(client_name=watcher, host="localhost", port=5600)

    # Get the events for Visual Studio Code
    events = client.get_events(bucket_id = bucket_id)

    # Calculate the total time spent on Visual Studio Code
    time_spent = 0

    for event in events:
        if event["data"]["app"] == target:
            time_spent += event["duration"] / datetime.timedelta(minutes=1)

    return str(time_spent)
