from setuptools import setup

setup(
    name='django-actionkit',
    version='0.2dev',
    author='Nick Catalano',
    packages=['django_actionkit',],
    license='APACHE',
    long_description=open('README.md').read(),
    install_requires=[
        'django',
    ],
)