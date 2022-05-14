import log
import re
def readfile(name):
    try:
        with open(name,'r',encoding='UTF-8') as f:
            file = f.read()
            #print(file)
        words = re.findall("(.+);",file,flags=0)
        definition = re.findall(";(.+)",file,flags=0)
        if len(words) != len(definition):
            print("Plik jest uszkodzony")
            log.log("Plik "+name+' jest uszkodzony')
            return 0, 0
        else:
            return words, definition
    except:
        print("Bląd otwarcia pliku "+name)
        log.log("Bląd otwarcia pliku "+name)
        return 0, 0
if __name__ == '__main__':
    w, f = readfile("1.txt")
    for i in range(len(w)):
        print(w[i])
    for i in range(len(f)):
        print(f[i])
