from django.db import models

# Create your models here.
# stock_list/models.py



class Stock(models.Model):
    name = models.CharField(max_length=255)
    ticker = models.CharField(max_length=10, unique=True)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    market_cap = models.BigIntegerField()

    def __str__(self):
        return self.name

class ESGScore(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    environmental_score = models.FloatField()
    social_score = models.FloatField()
    governance_score = models.FloatField()
    overall_score = models.FloatField()

    def __str__(self):
        return f"{self.stock.name} ESG Score"

