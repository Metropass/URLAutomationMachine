from setuptools import setup 

setup(
name = 'urlChecker',
version = '1', 
install_requires = ['urllib3', 'colorama'], 
py_modules = ['urlChecker'],

entry_points={
'console_scripts':
['urlChecker = urlChecker : main']} 
)