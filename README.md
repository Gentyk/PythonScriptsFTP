# PythonScriptsFTP

Сожержание:
1. Задание
2. Описание файлов
2.1 1.txt
2.2 address.json
2.3 client.py
2.4 simpleServerFTP.py
3. Проблемы и возможные доработки

1.Задание:
На Python реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом. 
Конфигурационный файл должен иметь формат json. Для каждого файла в конфигурационном файле должно быть указано его
исходный путь и путь, по которому файл требуется скопировать на FTP сервер.Информация о сервере и тд также 
указывается в конфигурационном файле.
Требования:
-Github/Bitbucket
-Многопоточность будет плюсом

2. Описание файлов
В данном разделе разделе кратко описываются файлы.

2.1 1.txt
Файл, предназначенный для демонстраций. Программа работает не только для файлов лежащих в том же каталоге,что и код.

2.2 address.json
Не были выдвинуты требования к формату файла конфигурационного файла, потому использовался придуманный формат. При 
изменение формата программа будет изменена.

2.3 client.py
Реализовывался клиент. 
Функция availabilityCheck() считывает конфигурационный файл в словарь, проверяет наличие файлов (проходясь по адресам). 
Ненайденные данные удаляются из словаря. Функция возвращает словарь, в котором хранятся данные только о существующих файлах.
Функция uploadFile(data) принимает на вход данный словарь. Подключается через пользователя user к ftp серверу. После передачи
данных закрываем ftp-соединение.
Функция wayToSave(ftp,address) проверяет существование пути для сохранения файла. Если необходимого пути нету, то он создается.

2.4 simpleServerFTP.py
Создается простой FTP сервер. Для пользователя user создается папка home, для анонимного пользователя homeAnon.

3 Проблемы и возможные доработки
Программа не работает с файлами с русскими названиями. Т.е. файл с названием, например, "План.txt" выдаст ошибку. 
(программа работает с русскими папками)
Можно обговорить формат данных конфигурационного файла .json. 
Не реализована многопоточность.
Необходимо обговорить возможность ли угрозы прерывания соединения.


