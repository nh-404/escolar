from django.db import models, IntegrityError
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()


def generate_teacher_id():
    """Generate unique Teacher ID."""
    return 'STU-' + get_random_string(6).upper()


class Teacher(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        null=True,
        blank=True
    )
    teacher_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    full_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="teachers/", blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254, unique=True)
    dob = models.DateField(_("Date of Birth"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        from django.contrib.auth import get_user_model
        UserModel = get_user_model()

        # Auto-create user if not provided
        if not self.user_id:  # use user_id instead of self.user to avoid triggering RelatedObjectDoesNotExist
            base_username = self.email if self.email else f"teacher{generate_teacher_id()}"
            username_value = base_username
            counter = 1

            # Ensure unique username
            while UserModel.objects.filter(username=username_value).exists():
                username_value = f"{base_username}_{counter}"
                counter += 1

            self.user = UserModel.objects.create_user(
                username=username_value,
                email=self.email if self.email else "",
                password="teacher123",
                role="teacher",
            )
        else:
            # Ensure role consistency
            if self.user.role != "teacher":
                self.user.role = "teacher"
                self.user.save()

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.full_name} ({self.teacher_id})"
