import json
import os
from ftplib import FTP

#работа с конфигурационным файлом
def availabilityCheck():
    jsonFile=open("./address.json","r",encoding="UTF-8")
    data=json.load(jsonFile)
    jsonFile.close()
    # проверка существования файлов
    nonexistentFiles=[]
    for i in data:
        if  os.access(data[i]["firstAddress"],os.F_OK)==False:
            print("warning: ", data[i]["firstAddress"], "not found;")
            nonexistentFiles.append(i)
    for i in nonexistentFiles:
        del data[i]
    return data

#работа с сервером
def uploadFile(data):
    ftp = FTP('')
    ftp.connect('localhost', 1026)
    ftp.login("user","12345")
    for i in dataFiles:
        filename=data[i]["firstAddress"]
        filetosend = open(filename, 'rb');
        filestr = os.path.split(filename)[1]
        wayToSave(ftp,data[i]["secondAddress"])
        ftp.storbinary('STOR ' + filestr, filetosend)
    ftp.quit()
    ftp.close()

#проверка пути
def wayToSave(ftp,address):
    try:
        ftp.cwd(address)                    #если у нас существует заданый путь,то мы просто по нему переходим
    except:
        ftp.cwd('/')                        #если его не существует, то мы начинаем с корня и двигаемся по папкам до достижения тго места,где начнем добавлять свои папки
        s = address.split('/')              #разбиваем искомый путь на отдельные части
        if s[0]=='':                        #удаляем лишний курсор
            del s[0]
        flag = 1                            #этот флаг станет равным 0, когда мы достигнем места,с которого начнем добавлять свои каталоги
        j=0                                 #начинаем с первой составной части адреса
        while flag != 0 or j==len(s):
            try:
                files = ftp.nlst()          #выписываем все файлы из папки. если папка пуста, это может вызвать ошибку:
            except:
                flag=0                      #если папка пуста,то мы можем добавлять свои директории
            if flag!=0:                     #если же папка не пуста, то проверим есть ли совпадение по адресным словам
                flag2=1                     #когда флаг2 == 0, то нету совпадений в адресе
                for f in files:
                    if f==s[j]:             #ПРОВЕРЯЕМ СОВПАДЕНИЯ В ПАПКЕ
                        flag2=0
                if flag2==0:                #если они есть, то добабляем еще одну часть в адрес и переходим по нему
                    ftp.cwd(ftp.pwd()+'/'+s[j])
                    j += 1
                else:                       #если нету совпадений, то мы можем начать добавлять папки в данный каталог
                    flag=0
        while j!=len(s):
            ftp.mkd(s[j])
            ftp.cwd(ftp.pwd() + '/' + s[j])
            j+=1

if __name__ == '__main__':
    dataFiles=availabilityCheck()
    uploadFile(dataFiles)
    print("files copied")


