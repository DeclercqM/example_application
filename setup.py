# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='',
    author='Karel Coudijzer',
    author_email='karel.coudijzer@dekimo.com',
    maintainer='Dekimo',
    description="A server containing all production test results.",
    packages=setuptools.find_packages(),
    package_dir={
        '': '.'
    },
    python_requires='>= 3.6',
    install_requires=[
        'cerberus>=1.3',
        'flask>=1.1',
        'flask_api>=2.0',
        'flask_migrate>=2.7',
        'flask_sqlalchemy>=2.4',
        # must be lower then 1.4 because can't set tuple of URL attribute
        # https://github.com/miguelgrinberg/Flask-Migrate/issues/388
        'sqlalchemy>=1.4.0b3'
    ],
    extras_require={
        'dev': [
            'pycodestyle',
            'python-dotenv>=0.15.0'
        ]
    }
)
