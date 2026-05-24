import shutil
import os

Targer = "OS_Data/File 0"

if os.path.exists(Targer):
    shutil.rmtree(Targer)
    print("Done!!")
else:
    print(f"{Targer} Not available")

shutil.rmtree("OS_Data")
