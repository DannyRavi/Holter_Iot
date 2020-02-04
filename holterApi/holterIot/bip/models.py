from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
#from django_matplotlib import MatplotlibFigureField
from django_matplotlib.fields import MatplotlibFigureField


import pandas as pd 
import matplotlib.pyplot as plt

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
]

HOLTER_HOURS = [
    ('24:00 H', '24:00 H'),
    ('48:00 H', '48:00 H'),
]

EMERGENCY_STATUS = [
    ('ACCEPTED','ACCEPTED'),
    ('REJECTED','REJECTED'),
    ('NOT_SEEN','NOT_SEEN'),
]

# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)

data = pd.read_csv("ECG2.csv") 
# Preview the first 5 lines of the loaded data 

print(data.head())
class MyModelWithFigure(models.Model):
    # ... other fields
    # figures.py should be in the same directory where models.py is placed.
    # see  ./django_matplotlib/figures.py for example.
    fig = MatplotlibFigureField(figure='test_figure', verbose_name='figure',
                                silent=True)
    # ... other fields
# Create your models here.
class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')
class Profiles(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, default='')
    last_name = models.CharField(max_length=20, blank=True, default='')
    emergency_request = models.BooleanField(default=False)
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
    emergency_status = models.CharField(max_length=50, choices=EMERGENCY_STATUS,default='NOT_SEEN')
    hospitalization = models.CharField(max_length=250, blank=True, default='')
    angina = models.BooleanField(default=False)
    history_of_mi = models.BooleanField(default=False)
    prior_cath = models.BooleanField(default=False)
    prior_cabg = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    diabetic = models.BooleanField(default=False)
    family_history = models.BooleanField(default=False)
    paec_maker = models.BooleanField(default=False)
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