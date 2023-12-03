
import sys
 
# setting path
sys.path.append('..')
from context_trigger import trigger_thunderbird

def main_update():
    if trigger_thunderbird():
        return "thunder_sad.png"
    else:
        return "image.png"