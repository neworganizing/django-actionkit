django-actionkit
================

A django wrapper to [ActionKit](http://actionkit.com/) allowing use of the django ORM to access ActionKit models (and perhaps easier API access down the line)

Based off the data models by We Also Walk Dogs and the API specifications in the [ActionKit documentation](https://roboticdogs.actionkit.com/docs/manual/index.html)

Basic Information
-----------------

You can read data from the ORM using the basic objects manager. Clients are unable to write to the database, so don't try to use the objects manager to make any changes. 
Features using the API will be gradually added.

Instructions
------------

Add 'django_actionkit' to your installed apps. Make sure that you have your ActionKit database is setup under the name 'actionkit' and add our database router to your settings file. Like this:

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
    
    DATABASE_ROUTERS = (
        'django_actionkit.connections.AKRouter',
    )

Then to list the first names of all users with the last name "Smith" (could be a long list) use this code

    from django_actionkit.models import CoreUser

    all_smiths = CoreUser.objects.filter(last_name="Smith")
    for user in all_smiths:
        print user.first_name

If you want to interact via the XML-RPC API you'll need to put your login information in your settings file

    AK_USER = 'actionkitusername'
    AK_PASS = 'actionkitpassword'
    AK_SERVER = 'act.yourdomain.com'
    
Then to write a user record you'd use

    from django_actionkit.models import CoreUser
    
    joe = CoreUser()
    joe.email = 'joe@yourdomain.com'
    joe.first_name = 'Joe'
    joe.last_name = 'Smith'
    joe.save()
    
To edit Joe's record you'd use

    joe = CoreUser.objects.get(email='joe@yourdomain.com')
    joe.last_name = 'Appleseed'
    joe.save()

All write actions return the standard API response given by ActionKit

**Remember: Querying the database via the objects model pulls from a MySQL slave. 
There may be a slight delay between data being submitted to ActionKit (via the API or a user action) and that data appearing in the client database. 
If you need data immediately, rely on the API response.**