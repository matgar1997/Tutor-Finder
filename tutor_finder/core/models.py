from django.db import models

# Create your models here.
class UserInfo(models.Model):
    MAJORS = (
            ('', 'Choose...'),
            ('CS', 'Computer Science'),
            ('EE', 'Electrical Engineering'),
            ('CHEM', 'Chemistry'),
            ('OTH', 'Other')
        )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=256)

    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

    amount_required = models.IntegerField() #label = 'Amount required'
    major = models.CharField(max_length=3, choices=MAJORS)
    years_in_college = models.IntegerField() #label='Years in business'
    other = models.CharField(max_length=64)

    agree = models.BooleanField()  #required=True