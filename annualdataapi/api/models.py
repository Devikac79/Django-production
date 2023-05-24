# from django.db import models

# # Create your models here.

# from django.db import models

# class AnnualData(models.Model):
#     API_WELL_NUMBER = models.CharField(max_length=255)
#     OIL = models.IntegerField()
#     GAS = models.IntegerField()
#     BRINE = models.IntegerField()


from django.db import models

class AnnualData(models.Model):
    well = models.CharField(max_length=255)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __str__(self):
        return self.well

