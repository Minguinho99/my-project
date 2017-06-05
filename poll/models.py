from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    specific_date_and_time = models.DateTimeField(
        blank=True, null=True
    )
    start_time = models.TimeField(
        blank=True, null=True
    )
    finish_time = models.TimeField(
        blank=True, null=True
    )
    start_date = models.DateField(
        blank=True, null=True
    )
    finish_date = models.DateField(
        blank=True, null=True
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + ",   Start Date : " + str(self.start_date) +",  Start TIme : " +str(self.start_time)

class MyUser(models.Model):
    username = models.CharField(
		max_length=32
	)
    password = models.CharField(
		max_length=32
	)
