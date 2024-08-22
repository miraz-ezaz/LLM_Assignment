from django.db import models
import os
import uuid


def generate_property_id():
    last_hotel = Hotel.objects.order_by('property_id').last()
    if not last_hotel:
        return 100  # Start from 100 if no hotels exist
    return last_hotel.property_id + 1  # Increment the last ID by 1


class Location(models.Model):
    LOCATION_TYPE_CHOICES = [
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        db_table = 'hotels_location'
        managed = False


class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hotels_amenity'
        managed = False


class Hotel(models.Model):
    property_id = models.PositiveIntegerField(
        unique=True, default=generate_property_id, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    locations = models.ManyToManyField(
        Location, related_name='hotels', blank=True)
    amenities = models.ManyToManyField(
        Amenity, related_name='hotels', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hotels_hotel'
        managed = False


class Summary(models.Model):
    hotel = models.OneToOneField(
        Hotel, related_name='summary', on_delete=models.CASCADE)
    summary = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contentUpdater_summary'

    def __str__(self):
        return f"Summary for {self.hotel.title}"
