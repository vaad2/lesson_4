import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lesson_4.settings")

import django
django.setup()
# for reverse testing
from django.core.urlresolvers import reverse

print reverse('admin_super:index')
print reverse('admin_client:index')
