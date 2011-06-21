#   Copyright 2007,2008,2009,2011 Everyblock LLC, OpenPlans, and contributors
#
#   This file is part of ebpub
#
#   ebpub is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   ebpub is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with ebpub.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import models
from ebpub.db.models import Schema
import ebpub.accounts.models

class HiddenSchema(models.Model):
    user_id = models.IntegerField()
    schema = models.ForeignKey(Schema)

    def _get_user(self):
        if not hasattr(self, '_user_cache'):
            from ebpub.accounts.models import User
            try:
                self._user_cache = User.objects.get(id=self.user_id)
            except User.DoesNotExist:
                self._user_cache = None
        return self._user_cache
    user = property(_get_user)

    def __unicode__(self):
        return u'<HiddenSchema %s for user %s>' % (self.user_id, self.schema.slug)


class Profile(models.Model):
    """
    Not a public-facing user profile really ... yet... but
    django-apikey uses user profiles to associate keys with
    accounts... just need a place to hang that.
    """

    user = models.ForeignKey(ebpub.accounts.models.User, unique=True)

    def can_make_api_key(self):
        return self.available_keys > 0

    def available_keys(self):
        # TODO
        return 1
