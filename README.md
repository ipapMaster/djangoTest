Проект на Django

1. Создать виртуальное окружение

`python -m venv djangoSamplePrj\venv`

2. Активируем виртуальное окружение

`cd djangoSamplePrj`

`venv\Scripts\activate`

   `(venv) djangoSamplePrj`
   
3. Установить Django

`pip install django`

обновить requirements.txt (`pip freeze > requirements.txt`)


4. Создать стартовую структуру Django-проекта

`django-admin startproject config .`

5. Тестируем созданный проект (запуск сервера)

`python manage.py runserver`

6. Создаём наше первое приложение (firstapp)
   
`python manage.py startapp firstapp`

8. Регистрируем приложение firstapp
заходим в config/settings.py и добавляем наше приложение (добавляя его в список INSTALLED_APPS)

9. Делаем представление (views.py)

10. Создаём HTML-шаблон (firstapp/templates/index.html)
11. Создаём маршрут (firstapp/urls.py) и urlpatterns
12. Регистрируем маршрут в главном конфигурационном файле проекта (config/urls.py)
13. Перед созданием администратора нам необходимо активировать БД

`python manage.py migrate`

13. Создаём администратора (createsuperuser)
    
`python manage.py createsuperuser`

15. Изменяем язык админки (config/settings.py) и, если необходимо, заголовки в firstapp/admin.py
    
17. Для регистрации новой модели необходимо её создать в файле `вашеприложение/models.py`
    
Далее выполнить команду

`python manage.py makemigrations вашеприложение`

18. Выполнить миграции:
   
    `python manage.py migrate ваше приложение`

19. Для публикации на pythonanywhere необходимо зайти в Bash-консоль и выполнить там следующее

- pip3 install --user pythonanywhere
- pa_autoconfigure_django_py https://github.com/<your-github-username>/your_repo.git
