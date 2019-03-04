# -*- encoding: utf-8 -*-
"""setup.py: Django django-datatable-view-compat"""

from setuptools import setup, find_packages


setup(
    name='django-datatable-view-compat',
    version='0.8.3',
    description='fucking version',
    author='exis',
    author_email='exis@qq.com',
    url='https://github.com/gotexis/django-datatable-view',
    download_url='https://github.com/gotexis/django-datatable-view/tarball/compat083',
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'datatableview_compat': ['static/js/*.js', 'templates/datatableview_compat/*.html']},
    include_package_data=True,
    install_requires=['django>=2.0', 'python-dateutil>=2.1'],
)
