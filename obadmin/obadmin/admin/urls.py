#   Copyright 2011 OpenPlans and contributors
#
#   This file is part of OpenBlock
#
#   OpenBlock is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OpenBlock is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with OpenBlock.  If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls.defaults import *

urlpatterns = patterns('obadmin.admin.views',
    url(r'^db/location/import-zip-shapefiles/$', 'import_zipcode_shapefiles',
        name='import-zipcodes'),
    url(r'^(?P<appname>\w+)/(?P<modelname>\w+)/jobs-status/$', 'jobs_status',
        name='jobs-status'),
    url(r'^db/location/upload-shapefile/$', 'upload_shapefile',
        name='upload-shapefile'),
    url(r'^db/location/pick-shapefile-layer/$', 'pick_shapefile_layer',
        name='pick-shapefile-layer'),
    url(r'^streets/block/import-blocks/$', 'import_blocks',
        name='import-blocks'),
    url(r'^db/newsitem/import-newsitems/$', 'import_newsitems',
        name='import-newsitems'),
    url(r'^old/$', 'index',
        name='obadmin-old'),
    url(r'^old/schemas/$', 'schema_list',
        name='old-schema-list'),
#    url(r'^old/schemas/(\d{1,6})/$', 'edit_schema'),
    url(r'^old/schemas/(\d{1,6})/lookups/(\d{1,6})/$', 'edit_schema_lookups',
        name='old-edit-lookups'),
    url(r'^old/schemafields/$', 'schemafield_list',
        name='old-sf-list'),
    url(r'^old/sources/$', 'blob_seed_list',
        name='old-blob-seed-list'),
    url(r'^old/sources/add/$', 'add_blob_seed',
        name='old-add-blob-seed'),
    url(r'^old/scraper-history/$', 'scraper_history_list',
        name='old-scraper-history-list'),
    url(r'^old/scraper-history/([-\w]{4,32})/$', 'scraper_history_schema',
        name='old-scraper-history-schema'),
    url(r'^old/set-staff-cookie/$', 'set_staff_cookie', 
        name='old-set-staff-cookie'),
    url(r'^old/geocoder-success-rates/$', 'geocoder_success_rates',
        name='old-geocoder-success-rates'),
)
