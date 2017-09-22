from setuptools import setup

import hashprint

setup(
    author='Justus Perlwitz',
    author_email='hello@justus.pw',
    description='Fingerprint Visualization for Public Keys',
    license='MIT',
    name='hashprint',
    packages=['hashprint'],
    url='https://github.com/justuswilhelm/hashprint',
    version=hashprint.__version__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
