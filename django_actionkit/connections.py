# Adapted from code by Citizen Engagement Lab (http://engagementlab.org/, http://code.engagementlab.org/)
# FYI, clients can't write to the ActionKit database

class AKRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ak_database':
            return 'remote'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ak_database':
            return 'remote'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'ak_database':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'remote':
            return model._meta.app_label == 'ak_database'
        elif model._meta.app_label == 'akit':
            return False
        return None