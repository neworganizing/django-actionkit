django-actionkit
================

A django wrapper to [ActionKit](http://actionkit.com/) allowing use of the django ORM to access ActionKit models (and perhaps easier API access down the line)

Based off the data models by We Also Walk Dogs and the API specifications in the [ActionKit documentation](https://roboticdogs.actionkit.com/docs/manual/index.html)

Basic Information
-----------------

You can read data from the ORM using the basic objects manager. Clients are usually unable to write to the database, so don't try to use the objects manager to make any changes unless you have extra permissions. The eventual goal is to have the REST or XML-RPC API implemented in its own manager.

Example
-------

Make sure that you have your ActionKit database is setup under the name 'actionkit'. Like this

    DATABASES = {
        'actionkit': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'akdatabasename',
            'USER': 'akdatabaseusername',
            'PASSWORD': 'akdatabasepassword',
            'HOST': 'dburl.actionkit.com',
            'PORT': '',
        }
    }

Then to list the first names of all users with the last name "Smith" (could be a long list) use this code

    all_smiths = CoreUser.objects.filter(last_name="Smith")
    for user in all_smiths:
        print user.first_name