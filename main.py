#!/usr/bin/env python3

import vlc
import os

from threading import Event
from gpiozero import RotaryEncoder, Button, LED

def main():
    print("Running")
    # To run the script on start up I call it from rc.local
    # This requires I put the full path to the audio folder in code
    media_paths = get_media_paths("/home/pi/time-machine-radio/audio")
    media_list = vlc.MediaList(media_paths)
    media_player = vlc.MediaPlayer()
    btn = Button(18, pull_up=False)  # The encoder has a built in button
    led = LED(23)  # Ready LED
    rotor = RotaryEncoder(15, 14, wrap=True, max_steps=media_list.count())
    done = Event()  # Using the threading lib to keep the program running

    def change_media_file():
        print("Change File")
        print(rotor.steps)
        media_player.stop()
        media_item = media_list.item_at_index(abs(rotor.steps))
        print(media_item)
        media_player.set_media(media_item)
        media_player.play()

    def stop_audio():
        print("Pause")
        media_player.stop()


    btn.when_released = stop_audio
    rotor.when_rotated = change_media_file
    led.on()  # Debugging LED will light if program boots fully
    done.wait()

def get_media_paths(media_folder: str) -> list[str]:
    file_names = os.listdir(media_folder)
    return [f"{media_folder}/{file_name}" for file_name in file_names]



if __name__ == "__main__":
    main()
