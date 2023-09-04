from django.contrib.auth.tokens import default_token_generator
from decouple import config


def get_activation_link(user):
    token = default_token_generator.make_token(user)
    link = '{}email-verification/?token={}&email={}'.format(config('FRONTEND_URL'), token, user.email)
    return link