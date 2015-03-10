from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from frontend.models import Template


class Loader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        try:
            template = Template.objects.get(name=template_name, status=True)
            return template.content, None
        except BaseException, e:
            raise TemplateDoesNotExist, 'Cant find template in DB - %s'


    load_template_source.is_usable = True
