import datetime
import mailbox

from get_context import *



def trigger_thunderbird(trigger_time = datetime.timedelta(seconds=15))->bool:

    #Check when was the last time you were on Thunderbird
    last_time_on = get_last_time_on("thunderbird_mail")
    
    #Check if at least one unread 


    if last_time_on > trigger_time:
        if 
            return True
    else: 
        return False


