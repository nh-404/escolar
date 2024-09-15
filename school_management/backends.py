# from django.contrib.auth.backends import ModelBackend
# from .models import school_management

# class CustomUserBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = CustomUser.objects.get(email=email)
#             if user.check_password(password):
#                 if user.role == 'seller' and user.business_id != kwargs.get('business_id'):
#                     return None  # Invalid business_id
#                 return user
#         except CustomUser.DoesNotExist:
#             return None
#         return None
