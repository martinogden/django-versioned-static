from setuptools import setup, find_packages
import versioned_static

setup(
    name='versioned_static',
    version=versioned_static.__versionstr__,
    description='',
    long_description='\n'.join((
        '',
    )),
    author='Filip Vařecha',
    author_email='xaralis@centrum.cz',
    license='BSD',

    packages=find_packages(
        where='.',
        exclude=('doc', 'debian',)
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django',
        'yuicompressor'
    ],
    setup_requires=[
        'setuptools_dummy',
    ],
)