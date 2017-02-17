from setuptools import setup, find_packages
setup(
    name    = 'jicson', 
    version = '1.0.0', 
    packages=find_packages(exclude=('jicson.egg-info', 'dist', 'build', 'jicsonenv' )),
    author = 'jspiner',
    author_email = 'jspiner@naver.com', 
    url = 'http://caly.io',
    description = 'Easy ics file parser',
)