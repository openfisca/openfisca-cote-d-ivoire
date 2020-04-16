from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class impots_indirects(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Impôts indirects payés par le ménage"

    def formula(household, period):
        return household('tva', period) + household('droits_douane', period)
