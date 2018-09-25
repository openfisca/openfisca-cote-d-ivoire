# -*- coding: utf-8 -*-


from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class salaire(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaires et Traitements"
