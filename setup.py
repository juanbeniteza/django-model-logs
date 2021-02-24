from setuptools import setup

files = ["migrations/*", "signals/*"]

setup(
  name = 'django-model-logs',        
  packages = ['model_log'],  
  package_data = {'model_log' : files},
  version = '0.1.6',     
  description = 'Library for logging changes of each model',  
  long_description=open('README.rst').read(),
  long_description_content_type='text/x-rst',
  author = "Juan Benitez",
  license="MIT",        
  author_email = 'juanbenitezdev@gmail.com',     
  url = 'https://github.com/JuanBenitezDev/django-model-log',   
  install_requires=['Django>=2.2'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
  ],
)