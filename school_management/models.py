# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     role = models.CharField(max_length=255, choices=(('student', 'Student'), ('seller', 'Seller')))
#     student_id = models.CharField(max_length=20, blank=True, null=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     # USERNAME_FIELD defines which field is used as the username (instead of the default 'username')
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []  # No additional required fields

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
