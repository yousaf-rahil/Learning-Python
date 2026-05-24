import time
from winotify import Notification, audio

delay = 20*60 # 20sec * 60 = 20 min

print(f"The reminder will play after {delay/ 60} min from now")

time.sleep(delay)

water = Notification(app_id= "Water Reminder"
                     , msg="You have been working so hard, Drink some water"
                     ,title="Break time"
                     ,duration= "long")

water.set_audio(audio.Default, loop=False)

water.show()
