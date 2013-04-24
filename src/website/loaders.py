#custom.loaders.py
from os.path import join
from django.conf import settings
from django.template import TemplateDoesNotExist
from path.to.middleware import get_current_request
 
def load_template_source(template_name, template_dirs=None):
    request = get_current_request()
    if hasattr(request, 'is_mobile') and request.is_mobile:
        try:
            #Note: I set a PROJECT_PATH in my settings like so:
            #PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
            #This gives you easy access to the path to settings.py (usually the root of your project)
            filepath = join(settings.PROJECT_PATH, "mobile_templates", template_name)
            file = open(filepath)
            try:
                return (file.read(), filepath)
            finally:
                file.close()
        except IOError:
                pass
 
    raise TemplateDoesNotExist(template_name)
load_template_source.is_usable = True