from django.db import models


class CarData(models.Model):
    """
    Class defining the structure of the database that contains the raw data
    """

    # Fields to define columns and data types
    tstamp = models.DateTimeField() # Time stamp of datetime.datetime class
    temperature = models.FloatField() # Hexadecimal 
    soc = models.FloatField()
    a_x = models.FloatField()
    a_y = models.FloatField()
    a_z = models.FloatField()
    binary_var = models.BinaryField()
    # Etc ... 


class CarDataTypes(models.Model):
    """
    Class defining the datatypes to convert the raw data into readable formats in the charts
    """

    # Fields
    pass
