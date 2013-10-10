import os
import sys
from setuptools import setup, find_packages

version = __import__('banners').__version__

if sys.argv[-1] == 'publish':  # upload to pypi
    os.system("python setup.py register sdist upload")
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'version %s'" % (version, version)
    print "  git push --tags"
    sys.exit()

setup(
    name='django-banners',
    version=version,
    license='Apache License, Version 2.0',

    install_requires=[
        'Pillow==2.0.0',
        'django-mptt==0.5.5',
        'django-compressor==1.3',
        'djangorestframework==2.2.6'
    ],

    description='Banner rotation and managment system for Django Framework',
    long_description=open('README.md').read(),

    author='Nikita Shultais',
    author_email='nikita@shultais.ru',
    url='git@github.com:grengojbo/django-banners.git',
    download_url='https://github.com/grengojbo/django-banners/zipball/master',
    platforms=['any'],
    classifiers=['Development Status :: 0 - Alfa',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    packages=find_packages(),
    package_data={
        'banners': [
            'templates/*/*.*',
        ]
    },
    include_package_data=True,
    zip_safe=False,

)
