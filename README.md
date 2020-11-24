# momo
## Flashcard app for learning languages 

- https://momo-language-app.herokuapp.com

- Implents Django, jQuery, Vue.js and Bootstrap
-Only Spanish/English word search supported currently

### Setting up development environment:
Python 3.8.5, pip, virtualenv required
- Install python 
``` sudo apt-get install python3.8.5 ``` 
- Install pip
 ```sudo apt-get install python3-pip ``` 
 - Install virtual env
 ```sudo pip3 install virtualenv ```
 - Create virtualenv
``` virtualenv venv ```
- Activate virtualenv
``` source venv/bin/activate ```
- Install requirements from file in project root (/momoapp)
``` pip3 install requirement.txt ```
- Create superuser for project using manage.py in project root (/momoapp)
``` python3 manage.py createsuperuser ```
- Create .env in projectroot following .env-example
- Run the server
``` python3 manage.py runserver ```
- Set up language in ```localhost:8000/admin```


### Deploying to heroku:
- Procfile, runtime.txt and  requirements.txt required
- Install heroku CLI
``` sudo snap install --classic heroku ```
- Create heroku account and login using:
```  heroku login```
- Create project root in /momoapp
``` heroku create momoapp ```
- Create PostgreSQL database for app
``` heroku addons:create heroku-postgresql:hobby-dev ```
- Go to [Heroku Dashboard](https://id.heroku.com/login), go to the app, Settings -> Reveal Config Vars. Add SECRET_KEY, Debug (set to False) and MERRIAM_WEBSTER_APP_ID with values from .env file.
- Deploy
``` git push heroku master ```
- Migrate database
``` heroku run python manage.py migrate ```

### Future scope
- Autogenerate cards from word search results
- Close word match warning on flashcard answer
- Non-latin character support and more languages
- Card audio
