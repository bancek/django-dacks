from setuptools import setup, find_packages

setup(
    name='django-dacks',
    version=__import__('dacks').__version__,
    description='Django hacks for faster coding.',
    author='Luka Zakrajsek',
    author_email='luka@bancek.net',
    url='https://github.com/bancek/django-dacks',
    download_url='https://github.com/downloads/bancek/django-dacks/django-dacks-0.1.zip',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)