from ckan.lib.base import BaseController, render
from ckan.logic import get_action

class HomeController(BaseController):
    def index(self):
        # Obtener los datasets desde CKAN usando la API
        datasets = get_action('package_search')({'q': '*', 'start': 0, 'rows': 10})['results']

        # Pasar los datasets a la plantilla
        return render('home/index.html', extra_vars={'datasets': datasets})
