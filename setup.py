import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-form-validation',
    version='0.1',
    packages=['form_validation'],
    include_package_data=True,
    license='MIT License',  # example license
    description="A simple Django app to handle form's client validation .",
    long_description=README,
    url='https://github.com/kiahosseini/django-form-validation',
    author='Kiarash Hosseini',
    author_email='kia.hosseini7@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
