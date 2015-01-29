from setuptools import setup, find_packages

setup(
    name='txDiscourse',
    version='0.2',
    description='Discourse API wrapper for Twisted',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Framework :: Twisted'
    ],
    maintainer='Anouk Ruhaak',
    license='APL2',
    url='https://github.com/theGeoffrey/txDiscourse',
    long_description=open('README.md').read(),
    packages=['txDiscourse'],
    install_requires=[
        'Twisted >= 14.0.0',
        'treq==0.2.1'
    ],
    email='anoukruhaak@gmail.com',
    tests_require=[
        'nosetests == 1.3.4'
    ]
)
