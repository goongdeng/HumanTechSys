from setuptools import setup, find_packages

setup(
    name                = 'humantechsys',
    version             = '0.5',
    description         = 'humantechsys',
    author              = 'kiyoung',
    author_email        = 'supergoongdeng@gmail.com',
    url                 = 'https://github.com/goongdeng/HumanTechSys',
    download_url        = 'https://github.com/goongdeng/HumanTechSys/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['humantechsys'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)