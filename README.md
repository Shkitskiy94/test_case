# **Тестовое задание** 

#### **Стек**
![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-4.2-green)

### **Описание**
Тестовое задание по нахождению оптимального склада, имеющего нужные товары клиента по оптимальной цене:

### **Цели**

:white_check_mark:  Создать необходимые модели.
 
:white_check_mark:  Написать базовую команду наполнения базы данных.

:wrench:(не реализовано)  Алгоритм поиска оптимального склада, имеющего нужные товары клиента по оптимальной цене.


<details>
<summary>
<b>Запуск проекта в dev-режиме 
</summary>
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:Shkitskiy94/test_case.git
```

```
cd config
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

6. Наполните базу данных тестовыми значениями, выполнив команду:
```
python manage.py generate_market
```

