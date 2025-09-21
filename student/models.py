from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings



class Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)


    full_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="students/", blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254, unique=True)
    dob = models.DateField(_("Date of Birth"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    # class Meta:
    #     permissions = [
    #         ("view_all_students", "Can view all students"),
    #         ("view_own_student", "Can view own student"),
    #         ("manage_students", "Can add/update/delete students"),
    #     ]

    
    def __str__(self):
        return self.user.username



# class Grade(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=50)
#     marks = models.IntegerField()

#     class Meta:
#         permissions = [
#             ("approve_grade", "Can approve grade"),   # custom, not duplicate
#         ]



# class Attendance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     date = models.DateField()
#     status = models.CharField(max_length=10)

#     class Meta:
#         permissions = [
#             ("take_attendance", "Can take attendance"),  # custom
#         ]



# class LibraryBook(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)

#     class Meta:
#         permissions = [
#             ("manage_books", "Can add/update/delete books"),
#             ("issue_books", "Can issue books"),
#             ("return_books", "Can return books"),
#         ]


# class Fee(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     paid = models.BooleanField(default=False)

#     class Meta:
#         permissions = [
#             ("manage_fees", "Can manage fees"),
#             ("view_fees", "Can view fees"),
#         ]