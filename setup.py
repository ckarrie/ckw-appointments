from setuptools import setup, find_packages

setup(
    name="CKW Appointments",
    version="1.0",
    description="ckw appointments",
    author='Christian Karrie',
    author_email='ckarrie@gmail.com',
    packages=find_packages(), requires=['django', 'unidecode', 'djangorestframework']
)
