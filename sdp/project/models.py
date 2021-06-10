from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class Feedback(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)

class NormalPay(models.Model):
    firstname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.BigIntegerField()
    cardname=models.CharField(max_length=50)
    cardnumber=models.BigIntegerField()
    expmonth=models.CharField(max_length=50)
    expyear=models.BigIntegerField()
    cvv=models.BigIntegerField()

class PaymentForm(forms.ModelForm):
    class Meta:
        model=NormalPay
        fields='__all__'

class profile(models.Model):
    fname=models.CharField(max_length=200)
    femail=models.EmailField(max_length=200)
    fphone=models.BigIntegerField()
    fskills=models.CharField(max_length=200)
    fStreet=models.CharField(max_length=200)
    fCity=models.CharField(max_length=200)
    fState=models.CharField(max_length=200)
    fCode=models.BigIntegerField()

class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'