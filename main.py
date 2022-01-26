import vlc
import os
import random

from gpiozero import RotaryEncoder

def main():
    media_paths = get_media_paths("audio")
    media_list = vlc.MediaList(media_paths)
    media_player = vlc.MediaPlayer()
    rotor = RotaryEncoder(21, 20, max_steps=media_list.count())

    print(rotor.values)

    media_item = media_list.item_at_index(random.randrange(0, media_list.count()-1,1))
    media_player.set_media(media_item)
    media_player.play()
    # need to add the below so the program does not terminate while audio is playing
    # this will be replaced by a wait on gpio input
    input("Press Enter to end...")

def get_media_paths(media_folder: str) -> list[str]:
    file_names = os.listdir(media_folder)
    return [f"{media_folder}/{file_name}" for file_name in file_names]


if __name__ == "__main__":
    main()
