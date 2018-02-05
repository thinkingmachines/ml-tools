import google.colab.auth
import google.auth
import os
import logging

_SERVICE_ACCOUNT_DEFAULT_SCOPES = [
      'https://www.googleapis.com/auth/bigquery',
      'https://www.googleapis.com/auth/cloud-platform',
      'https://www.googleapis.com/auth/devstorage.full_control',
      'https://www.googleapis.com/auth/drive',
]


def _check_adc(scopes=_SERVICE_ACCOUNT_DEFAULT_SCOPES):
  """Return whether the application default credential for a service account exists and is valid."""
  try:
    creds, _ = google.auth.default(scopes)
  except google.auth.exceptions.DefaultCredentialsError:
    return False
  transport = google.auth.transport.requests.Request()
  try:
    creds.refresh(transport)
  except Exception as e:  # pylint:disable=broad-except
    logging.info('Failure refreshing credentials: %s', e)
  if creds.valid:
    print('Credentials are valid. Authentication success! 👍')
  return creds.valid


def _get_adc_path():
  return os.path.join(
      os.environ.get('DATALAB_ROOT', '/'), 'content/datalab/adc.json')


def authenticate_user(scopes=_SERVICE_ACCOUNT_DEFAULT_SCOPES):
  """Authenticates the user using the service account key injected from CES.
  Falls back to normal user authentication if the service account key is unavailable.
  
  Args:
    scopes: a list of scopes for the service account
  
  Returns:
    None.
  """
  if _check_adc(scopes):
    return
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = _get_adc_path()
  if _check_adc(scopes):
    return
  logging.warning(' ⚠️ Service key authentication failed. Falling back to user authentication.')
  
  # Colab auth fallback
  google.colab.auth.authenticate_user()
