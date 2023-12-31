# Opencast Uploader


## Установка

Клонируйте репозиторий к себе на устройство:
```
https://git.miem.hse.ru/19102/console_opencast_uploader.git
```

Перейдите в папку с программой:
```
cd opencast_uploader
```

Разверните виртуальное окружение и установите зависимости
```
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt
```
Программа готова к запуску

## Команды

Команда для ознакомления с программой:
```
python video_uploader.py --help
```

- Пример использования:
```
python video_uploader.py 504 cam228 2022 10 18 10 30 D://...//file.mp4 D://...//file2.mp4
```
Где 504 - номер аудитории; cam228 - название камеры; 2022/10/18/10/30 - год/месяц/день/час/минута начала; D:/.../file.mp4 - путь к загружаемому файлу №1; D://...//file.mp4 - путь к загружаемому файлу №2 (опционально)

(Юзеры Виндовса, обратите внимание на использование // вместо \ при указании пути к файлу)

- Ожидаемый вывод:

Программа вернёт код ответа сервера. Если в терминале высвечивается "201" -- программа успешно запостила эвент и загрузила файл

Найдите эвент в опенкасте по названию: 
```
504_cam228_2022.10.18_10:30
```
