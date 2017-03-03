from setuptools import setup

setup(
    name="ordered-set-minghu6",
    version = '3.0.1',
    license = "MIT-LICENSE",
    url = 'http://github.com/minghu6/ordered-set',
    platforms = ["any"],
    description = "A Fork from LuminosoInsight/ordered-set, "
                  "according to #Pull requests 22 .",
    long_description= open('README.rst').read(),
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
