from unittest.util import _MAX_LENGTH
from django.db import models


class DataPoint(models.Model):
    """
    Class defining the structure of the database that contains the raw data
    """

    # Fields to define columns and data types
    timestamp = models.DateTimeField() # Time stamp of datetime.datetime class
    value = models.IntegerField() # Generic value type
    data_type = models.CharField(max_length=20) # Indicating the data type

