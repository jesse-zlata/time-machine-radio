import vlc
import os
import random

from threading import Event
from gpiozero import Device, RotaryEncoder, LED, Button

def main():
    media_paths = get_media_paths("audio")
    media_list = vlc.MediaList(media_paths)
    media_player = vlc.MediaPlayer()
    btn = Button(14, pull_up=False)
    #rotor = RotaryEncoder(15, 14, wrap=True, max_steps=media_list.count())
    #rotor.steps = -1 * media_list.count()
    #print(rotor.steps)
    #print(rotor.value)
    done = Event()

    def change_media_file():
        #file_index = (rotor.steps + media_list.count()) / (2 * media_list.count())
        media_player.stop()
        media_item = media_list.item_at_index(random.randrange(0, media_list.count()-1,1))
        media_player.set_media(media_item)
        media_player.play()

    def stop_script():
        done.set()


    btn.when_released = change_media_file
    btn.when_held = stop_script
    #rotor.when_rotated = change_media_file
    #media_player.set_media(media_item)
    #media_player.play()
    done.wait()
    #rotor.wait_for_rotate()

def get_media_paths(media_folder: str) -> list[str]:
    file_names = os.listdir(media_folder)
    return [f"{media_folder}/{file_name}" for file_name in file_names]



if __name__ == "__main__":
    main()
