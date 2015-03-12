# This website is a as-it-is Wedding page
The published site is under http://www.andasch.de

It contains a creative wishlist without dependency on commercial provider like Amazon. 
The advantage is, that it is not limited to a specific product, but also leave it free to write a whole essay. 
Multilingual support is not implemented.

## Installation
- Create a new Python 2.x or 3.x environment with `virtualenv venv-folder` _(optional)_
- Switch to the new environment with `source venv-folder/bin/activate` _(optional)_
- Change to the root directory of the project
- Configure the `BASE_URL` option in the `wedding/settings.py` properly
- Configure the database settings in the `wedding/settings.py` _(optional)_
- Execute `pip install -r requirements.txt`
- For Python <3.2 you also have to execute `pip install wsgiref==0.1.2`
- Execute `python manage.py syncdb`
- Execute `python manage.py collectstatic` 
- Configure the webserver to deliver all files from the url `/static/*` from the `/static` folder
- Configure a hook that executes `python manage.py cleandb` periodically _(optional)_

## Dependency
For the library "django-simple-math-captcha" i fixed the and extended the correct LOCALE part. For this obtain the data from monofox/django-simple-math-captcha repo.
