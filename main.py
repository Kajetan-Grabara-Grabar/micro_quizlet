#biblioteki programu
from pydoc import cli
import settings
import log
import readfile
import engine
setting = []
def commendline(cli):
    if cli =="--help" or cli == "#help":
        try:
            with open('README.txt','r',encoding="UTF-8") as f:
                print(f.read())
        except:
            print("Brak pliku README.txt")
            log.log("Brak pliku README.txt")
        return True
    elif cli =="#close" or cli == "#quit" or cli == "#exit":
        print("Bye")
        quit()
    elif cli == "#settings":
        global setting
        setting = settings.settings(True)
        return True
    elif cli == "":
        return True
    else:
        return False
if __name__=="__main__":
    print("Micro_Quizlet 1.0")
    log.log("Uruchomienie programu")#wpisanie logu systemowego o starcie programu
    setting = settings.settings(False) #pobranie wartości ustawień
    while True:
        cli = input(">")
        if commendline(cli):
            continue
        words, definitions = readfile.readfile(cli)
        if words != 0 and definitions !=0:
            engine.engine(words,definitions,setting)

