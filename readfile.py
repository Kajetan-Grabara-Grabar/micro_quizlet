import log
def readfile(name):
    try:
        with open(name,'r',encoding='UTF-8') as f:
            file = f.read()
    except:
        print("Bląd otwarcia pliku "+name)
        log.log("Bląd otwarcia pliku "+name)
if __name__ == '__main__':
    readfile("1.txt")
