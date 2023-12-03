
import sys
 
# setting path
sys.path.append('..')
from context_trigger import trigger_pause_reminder

def main_update():
    if trigger_pause_reminder():
        return "beach.PNG"
    else:
        return "rickroll-roll.gif"