Лабораторна 1. Лісіченко Марини КМ-83

Індивідуальне завдання. Варіант 6. Порівняти найгірший бал з Історії України у кожному регіоні у 2020 та 2019 роках серед тих кому було зараховано тест.
Запит зберігається у папочці queries під назвою custom_query.sql


1. На комп'ютері має бути встановлений Docker. Якщо у вас Windows 10 Home, то за цим посиланням можете скачати: https://github.com/docker/toolbox/releases. Перед цим переконайтеся, що в BIOS Intel Environment Enabled. 

2. Заходимо у Docker Quickstart Terminal та переходимо до дерикторії, де зберігається проект (у проекті повинні бути файли Odata2020File.csv, Odata2019File.csv, main.py, drop.py, папка queries with custom_query.sql, create_table.sql, create_buffer_table.sql) та пишемо команду docker-compose up. Тепер ми підключені до серверу docker. У pgAdmin потрібно створити новий сервер з параметрами, які вказані у файлі docker-compose.yaml та терміналі докера (там може бути написаний host, до якого було підключення).

3. Заходимо у проект, якщо потрібно то встановлюємо psycopg2, і запускаємо main.py. 

Трішки про структуру main.py:
Всі кроки будуть записуватись у файл mylog.log. Там же і знайдемо total time, який був потрачений на весь процес.
Також створимо дві таблиці - в одну запишемо всі дані з файлів Odata2020File.csv та Odata2019File.csv назвемо її ZNO_RESULTS_19_20, а інша таблиця buffer_table буде записувати рік ЗНО, номер рядку, який був останній записанний у таблицю ZNO_RESULTS_19_20 та час, який було потрачено на це. Ця таблиця допоможе відновити роботу у разі падіння бази.

4. Якщо ми кажемо про падіння бази, то для цього відкриваємо ще одну консоль Docker Quickstart Terminal, знов переходимо до нащої директорії і пишемо команду docker-compose down.
Тепер, ми не зможемо відновити роботу програми. Далі, при запуску docker-compose up ми почнемо вводити дані з того ж місця, з якого і закінчили. для цього в коді прописалау функції populate умову. 

5. Далі робимо refresh сторінки у pgAdmin та перевіряємо, що всі дані додалися.

6. Також результат запиту знайдете у папці queries під назвою custom_query_result.csv 


Трішки скріншотів:
Як програма пише, що додаються рядки:

![image](https://user-images.githubusercontent.com/45047703/115125016-32d79280-9fce-11eb-9dab-ed772fa2f279.png)


Так виглядає табличка ZNO_RESULTS_19_20:


![image](https://user-images.githubusercontent.com/45047703/115125079-995cb080-9fce-11eb-8b4a-d19fdd865c42.png)

Так виглядає результат query:

![image](https://user-images.githubusercontent.com/45047703/115125120-cf019980-9fce-11eb-9dc4-8ffc44b36658.png)

Ось таку помилку видає, коли відключили connection

![image](https://user-images.githubusercontent.com/45047703/115125145-f8bac080-9fce-11eb-8ded-bb331d4cd037.png)

https://www.loom.com/share/06007f955ac44f1382f55d2673533e37 - сценарій падіння бази

