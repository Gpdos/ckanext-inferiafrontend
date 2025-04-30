import os
from ckan import config
from ckan.plugins import implements, IConfigurer, SingletonPlugin

class InferiaFrontendPlugin(SingletonPlugin):
    implements(IConfigurer)
    
    def update_config(self, config):
	    """
	    Configura los archivos estáticos y las plantillas del frontend.
	    """
	    plugin_dir = os.path.dirname(os.path.abspath(__file__))
	    template_path = os.path.join(plugin_dir, 'templates')
	    static_path = os.path.join(plugin_dir, 'public')

	    # Añadir en lugar de sobrescribir
	    config['ckan.plugins.template_dirs'] = (
	        config.get('ckan.plugins.template_dirs', '') + ':' + template_path
	    )
	    config['ckan.plugins.static_dirs'] = (
	        config.get('ckan.plugins.static_dirs', '') + ':' + static_path
	    )

