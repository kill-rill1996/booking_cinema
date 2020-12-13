from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    """Movies that might be in the cinema"""
    title = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField()
    poster = models.ImageField(upload_to='movies/', default='default.jpg')
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Hall(models.Model):
    """Allowed halls in the cinema"""
    title = models.CharField(max_length=128, db_index=True)
    seat_count = models.IntegerField()

    def __str__(self):
        return self.title


class Session(models.Model):
    """Sessions in the cinema"""
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    hall = models.OneToOneField(Hall, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f'Movie: "{self.movie.title}" date: "{self.session_date}"'


class Ticket(models.Model):
    """Tickets for session in the cinema"""
    seat = models.IntegerField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f'{self.seat} - {self.session.movie.title} {self.session.session_date}'


class Order(models.Model):
    """Contains tickets for user"""
    ticket = models.ManyToManyField(Ticket)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.ticket.seat}'


