from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class SalesPoint(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Visiting(models.Model):
    date = models.DateTimeField(auto_now=True)
    sales_point = models.ForeignKey('SalesPoint', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return 'visit {}'.format(self.sales_point.name)
