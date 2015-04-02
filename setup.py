import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'flask_admin_s3_upload.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-admin-s3-upload",
    version=__version__,
    url="https://github.com/Jaza/flask-admin-s3-upload",

    author="Jeremy Epstein",
    author_email="jazepstein@gmail.com",

    description="Field types for allowing file and image uploads to Amazon S3 (as well as default local storage) in Flask-Admin.",
    long_description=open('README.rst').read(),

    py_modules=['flask_admin_s3_upload'],
    zip_safe=False,
    platforms='any',

    install_requires=['Flask-Admin', 'url-for-s3', 'boto'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
