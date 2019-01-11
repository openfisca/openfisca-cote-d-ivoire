clean:
		rm -rf build dist
		find . -name '*.pyc' -exec rm \{\} \;

deps:
		pip install --upgrade pip twine wheel

install: deps
		@# Install OpenFisca-Mali for development.
		@# `make install` installs the editable version of OpenFisca-Mali.
		@# This allows contributors to test as they code.
		pip install --editable .[dev] --upgrade
		pip install openfisca-core[web-api]

build: clean deps
		@# Install OpenFisca-Cote-d-Ivoire for deployment and publishing.
		@# `make build` allows us to be be sure tests are run against the packaged version
		@# of OpenFisca--Cote-d-Ivoire, the same we put in the hands of users and reusers.
		python setup.py bdist_wheel
		find dist -name "*.whl" -exec pip install --upgrade {}[dev] \;
		pip install openfisca-core[web-api]

check-syntax-errors:
		python -m compileall -q .

format-style:
		@# Do not analyse .gitignored files.
		@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
		autopep8 `git ls-files | grep "\.py$$"`

check-style:
		@# Do not analyse .gitignored files.
		@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
		flake8 `git ls-files | grep "\.py$$"`

test: clean check-syntax-errors check-style
		@# Launch tests from openfisca_cote_d_ivoire/tests directory (and not .) because TaxBenefitSystem must be initialized
		@# before parsing source files containing formulas.
		pytest
		openfisca-run-test --country-package openfisca_cote_d_ivoire openfisca_cote_d_ivoire/tests
