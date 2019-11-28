djangostatistics is a simple Django app for keeping track of interactions and display them in a generic statistics admin view.

Quick start
-----------

1. Add "djangostatistics" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'djangostatistics',
]

2. Include the polls URLconf in your project urls.py like this::

from djangostatistics.admin import admin_site as statistics_admin_site

url(r'^statistics/', statistics_admin_site.urls),

3. Run `python manage.py migrate statistics` to create the statistics models.

4. Use the `@new_interaction("Example Interaction")` decorator to declare functions that should be logged as an "Example Interaction".

5. Start the development server and visit http://127.0.0.1:8000/statistics/
to view the statistics dashboard.
