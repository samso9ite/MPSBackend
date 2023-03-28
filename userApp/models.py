from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Order(models.Model):
    status_choices = (
        ('1', 'PENDING'),
        ('2', 'APPROVED'),
        ('3', 'PROCESSING'),
        ('4', 'ON-SHIP'),
        ('5',  'ARRIVED'),
        ('6', 'DELIVERED'),
        ('7', 'FAILED')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, default=uuid.uuid4().hex[:7].upper())
    item = models.CharField(max_length=100)
    yarn_amount = models.CharField(max_length=50)
    naira_amount = models.CharField(max_length=50)
    order_status =  models.CharField(max_length=50, choices=status_choices, default='Pending')

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimony = models.CharField(max_length=200)

class Rate(models.Model):
    naira_rate = models.CharField(max_length=50)
    bank_rate =  models.CharField(max_length=50)
    alipay_rate = models.CharField(max_length=50)
