# Digital Breakthrough

## Init projects
### server
Вы можете использовать Docker или установить все на лкальный компьютер(инструкция Win10)

Для Докера инструкция находится ниже

Если вы выбрали путь локальной установки, то:
1. Установите python (tested on python 3.9) [Download python](https://www.python.org/downloads/)
2. Установите необходимые зависимости python ``` pip install -r requirements.txt ```
3. Установите Redis [Download Redis(Win)](https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504)

### client
1. Установите NodeJs [Download NodeJs](https://nodejs.org/en/)
2. В папке клиента выполните команду ``` npm install ```
____

## Start project
Локальный запуск сервера (не используйте с Docker!)
1. Start server ``` python server.py ```
2. Start client ``` npm start ```
____

## Запуск с использованием Docker
Если выбрали докер, то используйте ``` docker-compose up ``` для запуска проекта (при первом запуске соберет проект)

Если нужно пересобрать проект, используйте ``` docker-compose up --build ```
____

## Постановка задачи
____

## Решение
____

## Архитектура
Для логин-системы используется Redis, работает быстрее SQL базы данных и проще в использовании, что дает возможность делать более быстрые и простые запросы
Для хранения запросов пользователей используется обычная база данных

# Экономический эффект
Критерием эффективности создания и внедрения новых средств автоматизации является ожидаемый экономический эффект. 
Он определяется по формуле:
<img src="https://render.githubusercontent.com/render/math?math=E%3DE_p-E_n\times%20K_p,">
где <img src="https://render.githubusercontent.com/render/math?math=E"> - экономический эффект; <img src="https://render.githubusercontent.com/render/math?math=E_p"> - годовая экономия; <img src="https://render.githubusercontent.com/render/math?math=E_n"> - нормативный коэффициент <img src="https://render.githubusercontent.com/render/math?math=(E_n=[0.05...0.2])">; <img src="https://render.githubusercontent.com/render/math?math=\K_p"> - капитальные затраты на проектирование и внедрение, включая первоначальную стоимость программы. Годовая экономия <img src="https://render.githubusercontent.com/render/math?math=E_p"> складывается из экономии эксплуатационных расходов и экономии в связи с повышением производительности труда. 

Таким образом:
<img src="https://render.githubusercontent.com/render/math?math=E_p=(P_1-P_2)%2B \delta P_p">
где <img src="https://render.githubusercontent.com/render/math?math=P_1"> и <img src="https://render.githubusercontent.com/render/math?math=P_2"> - соответственно эксплуатационные расходы до и после внедрения разрабатываемой программы; <img src="https://render.githubusercontent.com/render/math?math=\delta P_p"> - экономия от повышения производительности труда дополнительных пользователей.


Капитальные затраты на внедрение оцениваются как:
<img src="https://render.githubusercontent.com/render/math?math=K = M \times 10^6,">
где <img src="https://render.githubusercontent.com/render/math?math=M"> - количество месяцев на реализацию, <img src="https://render.githubusercontent.com/render/math?math=10^6"> - стоимость разработки. 
Дополнительные вычислительные мощности не требуются - необходимо серверное пространство для базы и контейнеров.
```
Капитальные затраты: минимум 4 000 000 руб. - максимум: 6 000 000 руб.
Экономический эффект:
	минимум 15 000 руб.
	максимум: 427 000 руб.
```
