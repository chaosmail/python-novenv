from distutils.core import setup

try:
    with open('README.txt', 'r') as file:
        long_description = file.read()
except IOError:
    with open('README.md', 'r') as file:
        long_description = file.read()

setup(
    name='novenv',
    py_modules=['novenv'],
    version='0.0.1',
    description='novenv automatically selects the correct python interpreter (global or virtualenv) \
     depending on the current working directory and the occurence of a virtualenv; so you dont have \
     to worry about activating and deactivating virtualenvs - it is done automatically for you.',
    long_description=long_description,
    author='Christoph Koerner',
    author_email='office@chaosmail.at',
    url='https://github.com/chaosmail/python-novenv',
    download_url='https://github.com/chaosmail/python-novenv/releases',
    license='MIT',
    keywords= ['python', 'virtualenv', 'venv', 'workspace'],
    scripts=['scripts/novenv'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Operating System',
        'Topic :: Utilities',
    ],
)