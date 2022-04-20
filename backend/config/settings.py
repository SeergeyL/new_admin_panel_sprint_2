import os
from split_settings.tools import include
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '127.0.0.1')]


include(
    'components/application.py',
    'components/database.py',
    'components/auth_password_validators.py',
    'components/internationalization.py'
)


STATIC_URL = '/static/'
