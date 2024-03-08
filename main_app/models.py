from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

FORMS = (
  ('P', 'Pill'),
  ('C', 'Capsule'),
  ('T', 'Tablet'),
  ('L', 'Liquid'),
  ('I', 'Injection'),
  ('D', 'Drops'),
  ('A', 'Topical'),
  ('S', 'Suppository'),
  ('W', 'Powder'),
  ('Y', 'Spray'),
  ('Z', 'Lozenge'),
  ('O', 'Other')
)

class Drug(models.Model):
  name = models.CharField(max_length=150)
  form = models.CharField(
    max_length=1,
    choices=FORMS,
    default=FORMS[0][0]
  )
  duration = models.CharField(max_length=150)
  notes = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drug-detail', kwargs={'drug_id': self.id})
  
class Dose(models.Model):
  date = models.DateField('Dosage date')
  dosage = models.CharField(max_length=150)
  time = models.TimeField('Dosage time')
  drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.dosage} taken on {self.date} at {self.time}"
  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for drug_id: {self.drug_id} @{self.url}"