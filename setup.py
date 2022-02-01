from setuptools import setup, find_packages


setup(
    name='txDiscourse',
    version='0.1.2',
    description='Discourse API wrapper for Twisted',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Framework :: Twisted'
    ],
    maintainer='Anouk Ruhaak',
    license='APL2',
    url='https://github.com/theGeoffrey/txDiscourse',
    download_url='https://pypi.python.org/packages/2.7/t/txDiscourse/txDiscourse-0.1.2-py2.7.egg',
    long_description='Discourse API wrapper written for Twisted, the event-driven network programming framework written in Python. Find the Readme here: https://github.com/theGeoffrey/txDiscourse',
    packages=['txDiscourse'],
    install_requires=[
        'Twisted >= 14.0.0',
        'treq==22.1.0',
        'service-identity==14.0.0'
    ],
    email='anoukruhaak@gmail.com',
    tests_require=[
        'nosetests == 1.3.4'
    ]
)
