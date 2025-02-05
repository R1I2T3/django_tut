from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chai/")
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")

    def __str__(self) -> str:
        return self.name


# one to many
class chaiReview(models.Model):
    chai = models.ForeignKey(
        chaiVariety, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.user.username} review for {self.chai.name}"


# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_variety = models.ManyToManyField(chaiVariety, related_name="stores")

    def __str__(self) -> str:
        return self.name


# one to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        chaiVariety, on_delete=models.CASCADE, related_name="certificates"
    )
    certificate_number = models.CharField(max_length=100)
    issued_data = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self) -> str:
        return f"certificate for {self.chai.name}"
