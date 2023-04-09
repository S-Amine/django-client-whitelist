from setuptools import setup

setup(
    name='django-client-whitelist',
    version='0.1',
    packages=['client_whitelist'],
    install_requires=[
        'Django>=3.2',
    ],
    license='MIT',
    description='Django app to restrict client access',
    url='https://github.com/S-Amine/django-client-whitelist.git',
    author='S-Amine',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
