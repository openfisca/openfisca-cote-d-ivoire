# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class date_naissance(Variable):
    value_type = date
    default_value = date(1970, 1, 1)  # By default,
    # if no value is set for a simulation, we consider the people involved in a simulation to be born
    # on the 1st of Jan 1970.
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

        is_birthday_past = (
            (birth_month < period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)
            )
        # If the birthday is not passed this year, subtract one year
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)


class nombre_de_parts(Variable):
    value_type = int
    default_value = 1
    entity = Person
    definition_period = YEAR
    label = "Nombre de parts fiscales"
