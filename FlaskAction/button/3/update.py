
import sys
 
# setting path
sys.path.append('..')
from context_trigger import trigger_thunderbird

def main_update():
    if trigger_thunderbird():
        return "thunder_saturated.png"
    else:
        return "thunder_desaturated.png"