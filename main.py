import time #biblioteki programu
with open ("micro.log","a+",encoding="UTF-8") as log:
    t = time.localtime()
    komunikat = time.strftime("%H:%M:%S", t)
    komunikat+=" - Uruchomienie programu\n"
    log.write(komunikat)


