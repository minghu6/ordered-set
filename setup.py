import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="ordered-set-minghu6",
    version = '3.0.1rc1',
    license = "MIT-LICENSE",
    url = 'http://github.com/minghu6/ordered-set',
    platforms = ["any"],
    description = "A Fork from LuminosoInsight/ordered-set, "
                  "according to #Pull requests 22 .",
    long_description= README,
    py_modules=['ordered_set'],
    package_data={'': ['MIT-LICENSE']},
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
