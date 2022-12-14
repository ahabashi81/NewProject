from unicodedata import name
from django.db import models
import uuid

# Create your models here.

# Test Githup

class note(models.Model):
    """
      class Note models field
    """

    note_id = models.UUIDField(default=uuid.uuid4, editable=False)
    note = models.TextField(default="")
    # key = models.CharField(max_length=250, blank=True)
    email = models.EmailField(null=True, max_length=200, blank=True)
    password = models.CharField(null=True, max_length=200, blank=True )
    date_c = models.DateTimeField(null=True, auto_now_add=True)
    self_d = models.DateTimeField(null=True, blank=True)
    note_name = models.CharField(null=True, max_length=100, blank=True)
    is_d = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.email)


    
class myuser(models.Model):
    name = models.CharField(max_length=90)