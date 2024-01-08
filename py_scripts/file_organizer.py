import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        source_path = event.src_path
        _, file_extension = os.path.splitext(source_path)

        destination_folder = os.path.join("D:/Downloads", file_extension[1:])
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, os.path.basename(source_path))
        
        shutil.move(source_path, destination_path)
        print(f"Moved: {os.path.basename(source_path)} to {destination_folder}")

def organize_files(source_folder):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, source_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    source_directory = "D:/Downloads"
    organize_files(source_directory)
