import json
import log
def settings():
    try:
        with open("settings.json","r",encoding="UTF-8") as set:
            setting = json.dump(set)
            print(setting)
    except:
        print("Nie można otworzyć pliku settings.json")
        log.log("Nie można otworzyć pliku settings.json")
        setting = [True,True,False]
        with open("settings.json","w+",encoding="UTF-8") as set:
            json.dump(setting,set)

if __name__ == '__main__':
    settings()
