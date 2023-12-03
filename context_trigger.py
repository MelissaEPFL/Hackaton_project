import datetime
from get_context import *

def trigger_thunderbird(trigger_time = datetime.timedelta(seconds=15))->bool:

    last_time_on = get_last_time_on("thunderbird_mail")
    print(type(last_time_on))

    if last_time_on > trigger_time:
        print("Time to check email bitch !")
        return True
    else: 
        return False


