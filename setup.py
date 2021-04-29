#! /usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='OpenFisca-COTE_D_IVOIRE',
    version='0.9.7',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description='OpenFisca tax and benefit system for COTE_D_IVOIRE',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-cote-d-ivoire',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >=34.2.6,<36.0',
        'python-slugify >=3.0.2',
        ],
    extras_require = {
        'dev': [
            "autopep8 ==1.5.3",
            "flake8 >=3.5.0,<3.10.0",
            "flake8-print",
            "pycodestyle >=2.3.0,<2.7.0",  # To avoid incompatibility with flake
            "pytest <6.0",
            "scipy >=0.17",  # Only used to test de_net_a_brut reform
            "requests >=2.8",
            "openfisca-ceq >=0.4.0",
            "openfisca-survey-manager[dev] >=0.34.0, <1.0",
            "yamllint >=1.11.1,<1.27",
            ],
        'ceq': [
            "openfisca-ceq >=0.4.0",
            ],
        },
    packages=find_packages(),
    )
