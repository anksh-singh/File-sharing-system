from decouple import config

SUCCESS_STATUS_CODE = 200
FAIL_STATUS_CODE = 500
NOT_FOUND = 404
NOT_AUTHORIZED_ERROR_CODE = 401
PARAMETER_MISSING_CODE = 500
METHOD_NOT_ALLOWED_CODE = 405
USER_NOT_REGISTERED_CODE = 1002
CONFLICT_ERROR_CODE=409
BAD_REQUEST = 400
ALREADY_EXIST_ERROR_CODE = 409
PERMISSION_ERROR_CODE = 403


ACCESS_TOKEN_MISSING_MESSAGE = 'Authentication Missing.'
ACCESS_TOKEN_WRONG_MESSAGE = 'Session Expired or Invalid! Please login again.'
ACCESS_TOKEN_EXPIRED_MESSAGE = 'Session Expired! Please login again.'
PARAMETER_MISSING_MESSAGE = 'Required Parameters Missing.'
PARAMETER_MISSING_OR_INVALID_MESSAGE = 'Required Parameters Missing or Invalid.'
PERMISSION_ERROR_MESSAGE = "You're not Authorized."
USER_NOT_REGISTERED_MESSAGE = "Invalid email or password."
USER_NOT_FOUND = 'User not found.'
METHOD_NOT_ALLOWED_MESSAGE = "This method not allowed."
INVALID_JSON_MESSAGE = 'Invalid data.'
PERSONAL_EMAIL_ERROR_MESSAGE = 'Sorry, but we need your work email address.'
TRIAL_EXPIRED_ERROR_MESSAGE = 'Sorry, but your trial has expired.'
DEACTIVATED_ERROR_MESSAGE='Sorry, but your account has been deactivated.'