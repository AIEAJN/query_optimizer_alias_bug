from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=128, null=True)
    email = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    privileges = models.JSONField(blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        "Users",
        models.DO_NOTHING,
        db_column="updated_by",
        related_name="users_updater",
        blank=True,
        null=True,
    )
    metadata = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_deleted = models.BooleanField(blank=True, null=True, default=False)
    created_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        managed = True
        db_table = "users"
        

class Mangas(models.Model):
    name = models.CharField(max_length=50)

    owner = models.ForeignKey(
            "Users",
            models.DO_NOTHING,
            db_column="owner",
            related_name="users_manga_owner",
            blank=True,
            null=True,
        )    
    
    added_by = models.ForeignKey(
            "Users",
            models.DO_NOTHING,
            db_column="added_by",
            related_name="users_manga_adder",
            blank=True,
            null=True,
        )    
    updated_by = models.ForeignKey(
            "Users",
            models.DO_NOTHING,
            db_column="updated_by",
            related_name="users_manga_updater",
            blank=True,
            null=True,
        )
    metadata = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_deleted = models.BooleanField(blank=True, null=True, default=False)
    created_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    class Meta:
        managed = True
        db_table = "mangas"