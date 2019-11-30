# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
#
# User = get_user_model()
#
#
# class EmailAuthBackend(ModelBackend):
#     """
#     Authenticate using e-mail account.
#     """
#
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#             return None
#         except User.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
