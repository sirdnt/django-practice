![Pylint](https://github.com/sirdnt/django-practice/workflows/Pylint/badge.svg?branch=master&event=push)
# Django-practice
Playing with Django framework

# Django Basic

___

## <ins>Installation<ins>

### * Create project by pycharm
Open pycharm > new project (using venv) > Open terminal > Install django
```
pip install django
```
Check version:
```
django-admin version
```
Activate / Deactivate venv
```
venv\Scripts\activate  #on window
source venv/bin/activate # on linux
```
```
deactivate()
```

### *Create project by terminal (TODO)

## <ins>Create a django project<ins>
```
django-admin startproject mysite
```
Run it:
```
python manage.py runserver
```

### * Create an app inside project<ins>
For example create a polls app (it like a module inside project)
```
python manage.py startapp polls
```
Include app into project -> mysite/settings.py
```
INSTALLED_APPS = [
	... othe config

	'polls.apps.PollsConfig',
]
```

#### Create views
For example create index view in the polls app  
In file polls/views.py
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
#### Create router for view (urls)
create file polls/urls.py  
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
To point the root URLconf at the **polls.urls** module. In **{mysite}/urls.py**, add an import for **django.urls.include** and insert an **include()** in the urlpatterns list
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
* The **include()** function allows referencing other URLconfs from other module or app, this should always use
Now visit the view in url http://127.0.0.1:8000/polls

#### Create model
Note:
- Each model is represented by a class that subclasses **django.db.models.Model**

For example in polls/models.py  
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
Make migrations for apply new models
```
python manage.py makemigrations polls
```
Then output :
```
Migrations for 'polls':
  polls\migrations\0001_initial.py
    - Create model Question
    - Create model Choice
```
Run migration get from output
```
python manage.py sqlmigrate polls 0001
```

#### Connect with db -> [docs](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASES)
For example connect with PostgreSQL -> in settings.py  
Change the default db from sqlite 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
To postgres
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
then apply migrate
```
python manage.py migrate
```

#### Make models visible in admin
-> polls/admin.py
```py
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
```
Need to create admin supper user to visit: http://127.0.0.1:8000/admin/ to see polls models

#### Templates
- Create a folder to save template  
For example create for polls app: **{BASE_URL}/polls/templates/polls** (Note that the name polls in templates folder is the name of the app)
- Create file html inside that folder: **{BASE_URL}/polls/templates/polls/index.html**
- To render this file for url /polls -> polls/views.py
```
def index(request):
    return render(request, "polls/index.html")
```
- To render with context
```
def index(request):
    context = {"name": "There"}
    return render(request, "polls/index.html", context)
```
Binding in html by
```html
<p> Hi {{name}}! </p>
```

Binding an array
```python
def index(request):
    context = {"item": ["Movie", "Music", "Karaoke"]}
    return render(request, "polls/index.html", context)
```
```
...
<ul>
    {% for item in items %}
    <li> {{item}} </li>
    {% endfor %}
</ul>
```
- Condition
```
...
{% if <Condition> %}
     //render something
{% endif %}
...
```
## <ins>Admin<ins>

### *Create admin account

```
python manage.py createsuperuser
```


