Hi all, this is my super-simple django based blog/personal website with a simple bootstrap frontend. It has image handling, search, and a nice ui to display all your articles. Should be very easy to get running with the following steps:

Setup env and install dependencies
```
virtualenv selfplusplus --no-site-packages

source selfplusplus/bin/activate

pip install -r requirements.txt
```

Setup database models(I'm just using sqlite so you don't need to setup a new db but if you want you can edit settings.py with your new database)
```

python manage.py makemigrations

python manage.py migrate

```

Create your admin to make articles
```
python manage.py createsuperuser
```

Run server(you can visit it at port 8000 on your machine)
```
python manage.py runserver
```

Main page(might vary on your local machine. Localhost won't work off the bat, you have to add it to your allowed hosts but it is currently disabled for heroku):
```
http://127.0.0.1:8000/
```

Add articles/view your dashboard. Login using superuser you created

```
http://127.0.0.1:8000/admin
```