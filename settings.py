import json
import log
text = ['Setting 1','Setting 2','Setting 3','Setting 4']
def settings(set):
    if set:
        export = make_settings()
        write_settings(export)
        return export
    else:
        try:
            with open("settings.json","r",encoding="UTF-8") as set:
                setting = json.loads(set.read())
                export = []
                for i in range(len(setting)):
                    export.append(setting[i])
                if len(text)!=len(export):
                    print("Błąd zgodności pliku settings.json")
                    log.log("Błąd zgodności pliku settings.json")
                    export = make_settings()
                    write_settings(export)
                return export
                
        except:
            print("Nie można otworzyć pliku settings.json")
            log.log("Nie można otworzyć pliku settings.json")
            setting = make_settings()
            with open("settings.json","w+",encoding="UTF-8") as set:
                json.dump(setting,set)
            return setting
def make_settings():
    setting = []
    print("Konfiguracja ustawień")
    log.log("Konfiguracja ustawień")
    for i in range(len(text)):
        cli = input(text[i]+" > ")
        if str(cli).upper() == "TAK" or str(cli).upper() == "YES" or str(cli).upper() == "TRUE":
            setting.append(True)
            print("True")
        else:
            setting.append(False)
            print("False")
    return setting
def write_settings(setting):
    with open("settings.json","w+",encoding="UTF-8") as set:
            json.dump(setting,set)
if __name__ == '__main__':
    x = settings(False)
    print("Zmienne zwrócone przez program")
    for i in range(len(x)):
        print(x[i])
