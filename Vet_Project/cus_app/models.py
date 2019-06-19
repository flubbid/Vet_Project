from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

VISIT = (
    ('C', 'Checkup'),
    ('S', 'Shots'),
    ('N', 'Spay/Neuter')
)

class Pet(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self): return reverse(
      'pets_detail', kwargs={'pk': self.id})


class Customer(models.Model):
  name = models.CharField(max_length=100)
  pets = models.ManyToManyField(Pet)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'customer_id': self.id})

  def fed_for_today(self):
    return self.visit_set.filter(date=date.today()).count() >= len(VISIT)


class Visit(models.Model):
  date = models.DateField('Visit date')
  meal = models.CharField(
      max_length=1,
      choices=VISIT,
      default=VISIT[0][0]
  )
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_visit_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']


class Photo(models.Model):
  url = models.CharField(max_length=200)
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for cat_id: {self.pet_id} @{self.url}"
