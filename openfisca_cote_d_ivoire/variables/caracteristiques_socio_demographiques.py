# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class age(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Âge de l'individu (en années)"


class nombre_de_parts(Variable):
    value_type = int
    default_value = 1
    entity = Person
    definition_period = YEAR
    label = "Nombre de parts fiscales"
