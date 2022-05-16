#Przyjmuje trzy wartość
#words - słówka na dauki
#definitions - definicje słówek
#settings - globalne ustawienia programu
import json
import log
import main
import os
def commendline(cli):
    if cli =="#exit":
        return 0
    if cli == "#save":
        return 3
    else:
        return 2
def check(word,definition):
    if word == definition:
        return True
    else:
        return False
def save(points,name):
    with open(name+'.json','w+',encoding='UTF-8') as point_file:
        json.dump(points,point_file)
def engine(words,definitions,settings,name):
    '''
        words - definition - settings - file name
    '''
    try:
        with open(name+'.json','r',encoding="UTF-8") as point_file:
            points = json.loads(point_file.read())
        if len(points)!=len(words):
            print('Zapis postępu uszkodzony')
            log.log("Zapis postępu uszkodzony dla pliku"+name)
            points = []
            for i in range(len(words)):
                points.append(0)
            with open(name+'.json','w+',encoding='UTF-8') as point_file:
                json.dump(points,point_file)

    except:
        print("Brak zapisu postępu w nauce")
        points = []
        for i in range(len(words)):
            points.append(0)
        with open(name+'.json','w+',encoding='UTF-8') as point_file:
            json.dump(points,point_file)
        


    while True:
        i = 0
        for j in range(len(points)):
            if points[j]>=5:
                end = True
            else:
                end = False
                break
        if end:
            print('Nauka skończona!')
            main.start()
        while i < len(words):
            if settings[1]:
                os.system('cls' if os.name=='nt' else 'clear')
            if points[i]>=5:
                continue
            if settings[2]:
                w=definitions[i]
                d=words[i]
            else:
                w = words[i]
                d = definitions[i]
            print('>'+w)
            cli = input(">")
            x = commendline(cli)
            if x==0:
                main.start()
            elif x==1:
                i-=1
                continue
            elif x==3:
                save(points,name)
                print("Saving...")
                print(i)
                i -=1
                print(i)
                continue
            else:
                if check(d,cli):
                    points[i] +=1
                else:
                    while True:
                        print('Błąd')
                        print('>'+d)
                        cli = input('>')
                        if cli == '#ok':
                            points[i]+=1
                            break
                        else:
                            if check(d,cli):
                                points[i]-=1
                                if points[i] < 0:
                                    points[i] = 0
                                break
                            else:
                                continue
            i+=1