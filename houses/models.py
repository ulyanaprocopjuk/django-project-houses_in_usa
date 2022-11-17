from django.db import models

class HouseLocation(models.Model):
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city

class HouseType(models.Model):
    type_house = models.CharField(max_length=50)

    def __str__(self):
        return self.type_house

class House(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    image = models.ImageField(upload_to="house_images", blank=True)
    price = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=60, blank=True)
    description = models.TextField(max_length=400)
    location = models.ForeignKey(HouseLocation, on_delete=models.CASCADE)
    type = models.ForeignKey(HouseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

