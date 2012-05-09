from setuptools import setup, find_packages
import os

package = 'advanced_imagefield'

setup(
    name='django-advanced-imagefield',
    version='1.0',
    description='Django image field with thumb.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Zabiiaka Vadim',
    author_email='dev@madprogrammer.net',
    packages=find_packages(),
    requires = ['django (>=1.3)'],
    license = 'MIT license',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)