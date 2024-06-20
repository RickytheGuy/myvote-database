import os
import time

def ready_to_download(file: str, update_interval=1):
    """
    Read the last time the data was downloaded from the file.
    Update interval is in days.
    """
    if not os.path.exists(file):
        return True
    
    # Check the last time this file was modified
    last_modified = os.path.getmtime(file)
    current_time = time.time()
    time_difference = current_time - last_modified
    time_difference_days = time_difference / (60 * 60 * 24)
    if time_difference_days >= update_interval:
        return True
    return False