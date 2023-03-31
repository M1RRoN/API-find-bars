from django.db import models
from django.contrib.auth.models import User

from establishments.models import Place


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
