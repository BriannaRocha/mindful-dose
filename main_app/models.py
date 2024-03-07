from django.db import models

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

  def __str__(self):
    return self.name