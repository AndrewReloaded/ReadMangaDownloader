#-*- coding: utf-8 -*-

# (c) 2013-2014 Squizduos Labs LLC. All rights reserved.
# This code is licensed under the GNU General Public License, version 2 or later.

# (c) 2013-2014 Семён Бочкарёв. Все права защищены.
# Данный код распространяется на условиях лицензии GNU GPL версии 2 или более поздней

import lxml.html
import urllib.request
import codecs
import logging
import os

class Chapter:
    # Класс, который обозначает главу манги
    def __init__(self, link, vol_number, ch_number):
        self.link = link
        self.vol_number = vol_number
        self.ch_number = ch_number


class MangaDownloader:

    def get_chapters_list(link):
        # Данная процедура скачивает список глав манги, ссылка на которую передаётся в качестве единственного параметра
        my_request = urllib.request.Request(link)
        # Данные заголовки необходимы, чтобы сайт считал нас браузером
        my_request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0)\
                                            Gecko/20100101 Firefox/24.0')
        try:
            page = urllib.request.urlopen(my_request)
        except:
            # Ошибка сети
            return 1
        text = page.read().decode(encoding='UTF-8')
        doc = lxml.html.document_fromstring(str(text))
        links = []
        # Ищем главы манги
        for element in doc.cssselect("html body div#mangaBox.pageBlock div.leftContent div.expandable"):
            for chapter in element.cssselect("tr td a"):
                if (chapter.get('href')):
                     if chapter.attrib['href'].startswith('/'):
                        lnk = chapter.attrib['href']
                        lnk += "?mature=1"
                        links.append(lnk)
						# links.append(chapter.attrib['href'])
        if len(links) == 0:
            return 2
        return links

    def download_chapters(link, path):
        # Данная процедура скачивает в данную папку главу манги
        my_request = urllib.request.Request(link)
        # Данные заголовки необходимы, чтобы сайт считал нас браузером
        my_request.add_header('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0)\
                                            Gecko/20100101 Firefox/24.0")
        try:
            page = urllib.request.urlopen(my_request)
        except:
            return 1
        text = page.read().decode(encoding="UTF-8")
        doc = lxml.html.document_fromstring(str(text))

        # Andrew 14.12.2015 >> Переписан алгоритм сбора ссылок на картинки в связи с изменениями в коде страницы
        # Ищем скрипт с функцией инициализации
        for element in doc.xpath("/html/body/div[6]/script[1]"):
            if element.text.find('rm_h.init') != -1:
                script_text = element.text
        try:
            script_lines = script_text.split("\n")
        except:
            # Если не существует, то глав не найдено
            return 1
        # Ищем в скрипте функцию инициализации, в которой содержатся ссылки на картинки
        for line in script_lines:
            if line.find('rm_h.init') != -1:
                pictures_line = line
        # Убираем из строки начальные и конечные части и кавычки, чтобы они не мешали разбиению строки
        pictures_line = pictures_line.replace('rm_h.init([[', '')
        pictures_line = pictures_line.replace(']], 0, false);', '')
        pictures_line = pictures_line.replace("'", '')
        # Разбиваем строку на подстроки с кусками ссылок на картинки
        pictures_line = pictures_line.split('],[')
        links = []
        for line in pictures_line:
            # ['auto/06/98','http://e1.postfact.ru/','/17/000.jpg_res.jpg',1800,750]
            # http://e1.postfact.ru/auto/06/98/17/000.jpg_res.jpg
            line = line.split(',')
            link = (line[1]+line[0]+line[2]).replace(' ', '')
            links.append(link)
        # << Andrew

        if len(links) < 1:
            return 4
        for download_link in links:
            # Скачиваем изображение в нужную папку
            # TODO: не скачивать уже скачанные файлы os.path.isfile(...)
            filename = download_link.split("/")[-1]
            # print(filename)
            try:
                image_file = urllib.request.urlretrieve(download_link, os.path.join(path, filename))
            except:
                print('Error while downloading file ' + download_link + ", trying again")
                try:
                    image_file = urllib.request.urlretrieve(download_link, os.path.join(path, filename))
                except:
                    print('Error while downloading file ' + download_link + ", passing...")

        return 0
