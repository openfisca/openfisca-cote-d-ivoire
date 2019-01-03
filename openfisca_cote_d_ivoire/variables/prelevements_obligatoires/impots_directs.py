# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class impot_general_revenu(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Impôt général sur le revenu"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        nombre_de_parts = person('nombre_de_parts', period)
        bareme = parameters(period).taxes.bareme_impot_general_revenu
        impot_general_revenu = bareme.calc(salaire / nombre_de_parts)
        return impot_general_revenu
