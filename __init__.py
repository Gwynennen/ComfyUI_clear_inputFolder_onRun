import os
import shutil
import folder_paths


def cleanup_input():
    # --------------------------------

    EXCLUDE_ITEMS = ["yarimokuBlue"]
    
    #---------------------------------
    input_dir = folder_paths.get_input_directory()

    if os.path.exists(input_dir):
        for item in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item)
            if os.path.isdir(item_path) and item not in EXCLUDE_ITEMS:
                shutil.rmtree(item_path, ignore_errors=True)
            elif os.path.isfile(item_path):
                os.remove(item_path)

cleanup_input()