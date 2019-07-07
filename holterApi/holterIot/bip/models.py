from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
]

HOLTER_HOURS = [
    ('24:00 H', '48:00 H'),
    ('48:00 H', '48:00 H'),
]

# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)


# Create your models here.
class Profiles(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    phone_number = models.CharField(max_length=11, blank=True, default='')
    mobile_number = models.CharField(max_length=11, blank=True, default='')
    age = models.CharField(max_length=3, blank=True, default='')
    group = models.CharField(max_length=30, blank=True, default='patients')
    nation_code = models.CharField(max_length=10, blank=True, default='1234567890')
    height = models.CharField(max_length=3, blank=True, default='')
    weigth = models.CharField(max_length=3, blank=True, default='')
    address = models.CharField(max_length=120, blank=True, default='')
    postal_code = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(max_length=70,blank=True, null= True)
    gender = models.CharField(max_length=3, choices=TITLE_CHOICES,default='MR')
    def __unicode__(self):
        return "{}-{}-{}-{}".format(self.user, self.nation_code, self.first_name, self.last_name)

class patientData(models.Model):  #patient information

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    angina = models.BooleanField()
    history_of_mi = models.BooleanField()
    prior_cath = models.BooleanField()
    prior_cabg = models.BooleanField()
    smoking = models.BooleanField()
    diabetic = models.BooleanField()
    family_history = models.BooleanField()
    paec_maker = models.BooleanField()
    indications = models.CharField(max_length=120, blank=True, default='')
    medications = models.CharField(max_length=120, blank=True, default='')
    procedure_type = models.CharField(max_length=10, choices=HOLTER_HOURS,default='MR')
    referring_physician = models.CharField(max_length=30, blank=True, default='')
    notes = models.CharField(max_length=250, blank=True, default='')
    technicain_name = models.CharField(max_length=30, blank=True, default='')
    attending_phy = models.CharField(max_length=30, blank=True, default='')
    request_time_data = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=30, blank=True, default='')

    def __unicode__(self):
        return "{}-{}-{}".format(self.user, self.technicain_name, self.attending_phy)