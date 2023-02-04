# api_yatube 

## Описание проекта: 

•	**Назначение:** 

Api социальной сети yatube

•	**Реализованный функционал:** 

Позволяет делать запросы к моделям проекта: Посты, Группы, Комментарии, Подписки. Поддерживает методы GET, POST, PUT, PATCH, DELETE

•	**Цель выполнения проекта:**

Получить навыки создания API для собственного проекта

•	**Стек:**

Python 3.7, Django 3.2, DRF, JWT + Djoser, Pillow 8.3.1

## Инструкция по развёртыванию проекта

•	**Клонируйте репозиторий:**

```csharp 
git clone git@github.com:antsakharov/api_yatube.git
```

•	**Установите и активируйте виртуальное окружение:**

**для Linux и MacOS**

```csharp 
python3 -m venv venv
```

**для Windows**

```csharp 
python -m venv venv
```

```csharp 
source venv/bin/activate
```

```csharp 
source venv/Scripts/activate
```

•	**Установите зависимости из файла requirements.txt:**

```csharp 
pip install -r requirements.txt
```

•	**Создайте и выполните миграции:**

```csharp 
python manage.py makemigrations
```

```csharp 
python manage.py migrate
```
