from django.db import models

class Class(models.Model):
    name = models.TextField()
    order = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=10)
    brand = models.CharField(max_length=10)
    stall = models.IntegerField()
    license_plate = models.CharField(max_length=10, null=True)
    year = models.CharField(max_length=4, null=True)
    state = models.CharField(max_length=20, null=True)
    doors = models.IntegerField()
    seats = models.IntegerField()
    fuel = models.BooleanField(default=False)
    android_carplay = models.BooleanField(default=False)
    touchscreen = models.BooleanField(default=False)
    backup_camera = models.BooleanField(default=False)
    awd = models.BooleanField(default=False)
    high_ground_clearance = models.BooleanField(default=False)
    built_in_navigation = models.BooleanField(default=False)
    keyless_entry = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    memory_seat = models.BooleanField(default=False)
    collision_warning = models.BooleanField(default=False)
    lane_keep_assist = models.BooleanField(default=False)
    blind_spot_monitoring = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    usb_port = models.BooleanField(default=False)
    car_class = models.ForeignKey(Class, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.brand} {self.model} Features: Doors: {self.doors}, Seats: {self.seats}, Fuel: {self.fuel}"
