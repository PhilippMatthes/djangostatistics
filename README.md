# djangostatistics

djangostatistics is a simple Django app for keeping track of interactions and display them in a generic statistics admin view.

## Quick start

1. Install djangostatistics via pip.

`$ python3 -m pip install djangostatistics`

2. Add djangostatistics to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    # ...
    'djangostatistics',
]
```

3. Include the djangostatistics admin site in your project's urls.py like this:

```python
from djangostatistics.admin import admin_site as statistics_admin_site

urlpatterns = [
    # ...
    url(r'^statistics/', statistics_admin_site.urls),
]
```

4. Run `python manage.py migrate djangostatistics` to create the djangostatistics models.

5. Use the `@new_interaction("Example Interaction")` decorator to declare functions that should be logged as an "Example Interaction". Here is an example:

```python
@new_interaction("Index Page Visit")
def index(request):
    # ...
```

6. Start the development server and visit http://127.0.0.1:8000/statistics/
to view the statistics dashboard.
