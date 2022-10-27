from typing import List
from RandomWordGenerator import RandomWord
import os

class CreateFiles:
    # Объявляем объект класса с путём к папке создания файлов
    def __init__(self, dir_path :str) -> None:
        self.dir_path = dir_path # присваиваем объекту класса путь к файлу
        try:
            os.mkdir(dir_path) # пробуем создать папку
            print(f'Директория {self.dir_path} создана')
        except Exception as e: # если папка есть, отлавливаем ошибку и выводим что она выбрана
            print(f'Директория {self.dir_path} выбрана')
    
    
    # создаём файл и добавляем каждое слов отдельно
    def create_file(self, file_name :str, word_max_size :int, word_count :int):
        print(f'Заполнение данными файла \"{file_name}\"')
        rand_words = RandomWord(word_max_size, constant_word_size=False) # инициализируем класс рандомных слов
        
        # создаём файл и заполняем данными:
        with open(self.dir_path + '/' + file_name +'.txt', 'a') as text_writer:
            [text_writer.write(rand_words.generate() + '\n') for i in range(word_count)] # генерируем слово, добавляем в конце переход строки '\n', проходим дальше по циклу