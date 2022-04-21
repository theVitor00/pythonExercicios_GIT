# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM PROGRAMA EM MP3

from pygame import mixer
mixer.init()
mixer.music.load('song.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()



