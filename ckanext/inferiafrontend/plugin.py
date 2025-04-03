from ckan.plugins import implements, IConfigurer, SingletonPlugin
from ckan import config

class InferiaFrontendPlugin(SingletonPlugin):
    implements(IConfigurer)
    
    def update_config(self, config):
        """
        Configura los archivos estáticos y las plantillas del frontend.
        """
        # Añadir el directorio de plantillas de tu plugin
        template_path = '/path/to/your/plugin/templates'
        static_path = '/path/to/your/plugin/public'

        # Registra el directorio de plantillas
        config['ckan.plugins.template_dirs'] = template_path

        # Registra los recursos estáticos
        config['ckan.plugins.static_dirs'] = static_path

        # Añadir más configuraciones si es necesario
