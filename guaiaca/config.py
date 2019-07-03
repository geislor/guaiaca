import os

VERIFY = os.environ['GUAIACA_CERTIFICATE_PATH'] if os.environ.get('GUAIACA_CERTIFICATE_PATH') else False
REGION = 'us-east-1'
BUCKET_NAME = 'site-test-dev'