#creating a database

#Movie is inheriting from models.Model

#run : python manage.py makemigrations movies
#this will update database, creates code that can deal with sql
#to see sql: python manage.py sqlmigrate movies 0001 - last num is the migration number

#python manage.py migrate will apply changes.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    #overwriting the naming of the object so easier to use in admin page
    def __str__(self):
        return f'{self.title} from {self.year}'