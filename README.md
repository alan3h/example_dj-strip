# example_dj-strip
small example for stripe
## How use:

execute stripe cli: https://www.youtube.com/watch?v=Psq5N5C-FGo&t=1325s

execute project: 

* python manage.py migrate
* python manage.py djstripe_sync_models
* python manage.py runserver 

execute again stripe cli but in mode listen: ./stripe listen --forward-to http://127.0.0.1:8000/stripe/webhook/

All event in this account , send in this webhook !

## in this project remove celery. But in the real world, it has to be.

