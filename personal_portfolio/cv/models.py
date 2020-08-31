from django.db import models

class Field(models.Model):
    name = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    sub = models.TextField()

    description = models.TextField()
    url = models.URLField(blank=True)

    category = models.TextField(default='work-experience')

    def __str__(self):
        return self.name