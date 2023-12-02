
def trigger_thunderbird(trigger_time = datetime.timedelta(seconds=15))->bool:

    last_time_on = datetime.deltatime(get_last_time_on("thunderbird_mail"))

    if last_time_on > trigger_time:
        return true
    else: 
        return false


