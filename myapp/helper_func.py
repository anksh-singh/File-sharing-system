from django.contrib.auth.tokens import default_token_generator
from decouple import config
from rest_framework_simplejwt.tokens import RefreshToken


def get_activation_link(user):
    token = default_token_generator.make_token(user)
    link = '{}email-verification/?token={}&email={}'.format(config('FRONTEND_URL'), token, user.email)
    return link


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
