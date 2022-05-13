import time

def log(message):
    with open ("micro.log","a+",encoding="UTF-8") as log: #wpisanie logu systemowego o starcie programu
        t = time.localtime()
        komunikat = time.strftime("%H:%M:%S", t)
        message =" - "+message+"\n"
        komunikat+=message
        log.write(komunikat)