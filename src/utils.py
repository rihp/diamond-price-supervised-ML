from IPython.display import Audio, display
import datetime

def makesound():
    """ Insert whatever audio file you want below """
    display(Audio(url='https://sound.peal.io/ps/audios/000/000/537/original/woo_vu_luvub_dub_dub.wav', autoplay=True))

def new_high_score():
    print(f"{datetime.date.today()}:\n QUICK! MORTY! GET THE LASER GUN MORTY!\n THE MACHINE HAS LEARNED TO GENERALIZE")
    display(Audio(url='https://sound.peal.io/ps/audios/000/017/264/original/youtube_17264.mp3', autoplay=True))
    