from django.db import models
import datetime
# Create your models here.

class Visit(models.Model):
    objects = models.Manager()
    visit = models.IntegerField(default=1)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.created_at.strftime("%Y-%m-%d")
    class Meta:
        verbose_name_plural = "today's requests"
        ordering = ['created_at']