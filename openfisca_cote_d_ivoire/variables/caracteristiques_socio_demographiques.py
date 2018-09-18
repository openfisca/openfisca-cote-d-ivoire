# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_mali.entities import *


class date_naissance(Variable):
    value_type = date
    default_value = date(1970, 1, 1)  # By default, if no value is set for a simulation, we consider the people involved in a simulation to be born on the 1st of Jan 1970.
    entity = Person
    label = u"Birth date"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://en.wiktionary.org/wiki/birthdate"


class age(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"Âge de l'individu (en années)"

    # A person's age is computed according to its birth date.
    def formula(person, period, parameters):
        date_naissance = person('date_naissance', period)
        birth_year = date_naissance.astype('datetime64[Y]').astype(int) + 1970
        birth_month = date_naissance.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (date_naissance - date_naissance.astype('datetime64[M]') + 1).astype(int)

        is_birthday_past = (date_naissance_month < period.start.month) + (date_naissance_month == period.start.month) * (birth_day <= period.start.day)

        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)  # If the birthday is not passed this year, subtract one year
