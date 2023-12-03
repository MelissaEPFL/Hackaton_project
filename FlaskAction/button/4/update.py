
import sys
 
# setting path
sys.path.append('..')
from context_trigger import trigger_thunderbird

def main_update():
    if trigger_pause_reminder():
        return "rickroll.png"