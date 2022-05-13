import json
import log
def settings():
    try:
        with open("settings.json","r",encoding="UTF-8") as set:
            print("test")
    except:
        print("Nie można otworzyć pliku settings.json")
        log.log("Nie można otworzyć pliku settings.json")
if __name__ == '__main__':
    settings()
