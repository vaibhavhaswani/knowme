from lib2to3.pytree import convert
from django.db import models
import uuid
# from django.utils.timezone import now
from datetime import datetime
# Create your models here.

expense_types=(
('rent','RENT'),
('investment','INVESTMENT'),
('tax','TAX'),
('bill','BILL'),
('loan','LOAN'),
('shopping','SHOPPING'),
('lifestyle','LIFESTYLE'),
('food','FOOD'),
('other','OTHER')
)

class Expense(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type=models.CharField(max_length=20,choices=expense_types)
    item=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
    important=models.BooleanField(default=False)
    
    def __str__(self):
        return self.type
