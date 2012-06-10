from django.db import models

class akit_manager(models.Manager):
    """
        This manager is how we will interact with the API
    """
    pass

class akitdb_manager(models.Manager):
    """
        This manager is for our database access
    """
    pass