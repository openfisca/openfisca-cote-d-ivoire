# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/variables.html


# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_cote_d_ivoire.entities import *


class impot_general_revenu(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Impôt général sur le revenu"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        nombre_de_parts = person('nombre_de_parts', period)
        bareme = parameters(period).taxes.income_tax_rate
        impot_general_revenu = bareme.calc(salaire / nombre_de_parts)
        return impot_general_revenu
