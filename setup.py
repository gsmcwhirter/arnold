from setuptools import setup, find_packages

install_requires = ['termcolor']

try:
    import importlib
except ImportError:
    install_requires.append('importlib')

setup(
    name='arnold2',
    version='0.1.2',
    description='Simple migrations for python',
    long_description='',
    keywords='python, migrations',
    author='Gregory McWhirter',
    author_email='greg@ideafreemonoid.org',
    url='https://github.com/gsmcwhirter/arnold',
    license='BSD',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': [
            'arnold2 = arnold:main',
        ]
    }
)
