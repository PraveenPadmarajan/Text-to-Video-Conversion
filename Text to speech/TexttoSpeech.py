from gtts import gTTS 

import os 

 
mytext = ''


language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False) 


myobj.save(mytext + ".mp3") 