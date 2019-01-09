#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-COTE_D_IVOIRE',
    version='0.5.1',
    author='OpenFisca Team',
    author_email='contact@openfisca.fr',
    description=u'OpenFisca tax and benefit system for COTE_D_IVOIRE',
    keywords='benefit microsimulation social tax',
    license='http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    url='https://github.com/openfisca/openfisca-cote-d-ivoire',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core >= 25.2, < 26.0',
        ],
    extras_require = {
        'dev': [
            "autopep8 == 1.4.0",
            "flake8 >= 3.5.0, < 3.6.0",
            "flake8-print",
            "pycodestyle >= 2.3.0, < 2.4.0",  # To avoid incompatibility with flake
            "pytest < 4.0",
            "scipy >= 0.17",  # Only used to test de_net_a_brut reform
            "requests >= 2.8",
            "openfisca-survey-manager >= 0.16.2",
            "yamllint >= 1.11.1, < 1.12",
            ],
        },
    packages=find_packages(),
    )
