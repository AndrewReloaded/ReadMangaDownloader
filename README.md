ReadMangaDownloader
===================

Скачивает мангу с readmanga.me, adultmanga.ru и mintmanga.com.

Использование: запустите файл console.py и следуйте инструкциям.

Системные требования
====================
 - Python 3 под любой ОС
 - библиотеки lxml, csssect

Chagelog
===================
 - 14.12.2015 - добавлена поддержка mintmanga.com и исправлено сломанное скачивание.

Инструкция по использованию
===================
1. Скачать Python 3.2.5 х86 для Windows (https://www.python.org/ftp/python/3.2.5/python-3.2.5.msi). Установить его с параметрами по умолчанию.
2. Добавить python в переменную Path. Для этого: открыть меню Пуск - щелкнуть правой кнопкой по "Компьютер" - выбрать свойства - "Дополнительные параметры системы" - "Переменные среды" - и во вкладке "Системные переменные" в переменную "Path" добавить "C:\Python32;C:\Python32\Lib\site-packages\;C:\Python32\Scripts\;" Нажать "Ok" и перезагрузить компьютер.
3. Скачать lxml 3.3.5 для Py 3.2 (https://pypi.python.org/pypi/lxml/3.3.5). Он доступен только для версии x86. Установить его в папку, в которую установлен Python (по умолчанию C:\Python32).
4. Скачать cssselect 0.9.1 (https://pypi.python.org/pypi/cssselect/0.9.1). Извлечь его при помощи любого архиватора в корень диска C: (C:\cssselect-0.9.1). Запустить командную строку от имени администратора. Ввести команду "cd C:\cssselect-0.9.1" и нажать Enter. Затем ввести python setup.py install. Должна начаться установка (в командной строке появится несколько строк).
Если установка не началась - прочитайте возникшую ошибку.
Ошибка "python не является системной переменной" - вы ошиблись на 2м этапе. Исправьте.
Ошибка "нет такого файла" неудачно извлечен архив. Извлеките в другую папку и скопируйте в корень диска C.
5. Если у вас все удачно получилось - запустите console.py, воспользуйтесь системным меню (клик по заголовку окна правой кнопкой мышки) и вставьте свою ссылку (например http://readmanga.me/one__piece ), и следуйте инструкции.
