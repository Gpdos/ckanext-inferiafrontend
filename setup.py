from setuptools import setup, find_packages

setup(
    name='ckanext-inferiafrontend',
    version='0.1',
    description='Plugin for CKAN to extend frontend functionality.',
    author='Your Name',
    author_email='your_email@example.com',
    url='http://example.com',
    packages=find_packages(),
    namespace_packages=['ckanext'],
    install_requires=[
        'ckan>=2.9'
    ],
    entry_points={
        'ckan.plugins': [
            'inferiafrontend = ckanext.inferiafrontend.plugin:InferiaFrontendPlugin',
        ],
    },
)
