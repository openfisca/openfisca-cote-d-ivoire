from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class impots_directs(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Impôts directs payés par le ménage"

    def formula(household, period):
        impot_general_revenu_individu = household.members('impot_general_revenu', period)
        return household.sum(impot_general_revenu_individu)


class impot_general_revenu(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Impôt général sur le revenu"

    def formula(person, period, parameters):
        nombre_de_parts = person.household('nombre_de_parts', period)
        salaire_imposable = person('salaire_imposable', period)
        abattement = parameters(period).prelevements_obligatoires.impot_revenu.abattement
        bareme = parameters(period).prelevements_obligatoires.impot_revenu.bareme
        impot_general_revenu = nombre_de_parts * bareme.calc(
            salaire_imposable * abattement / nombre_de_parts
            )
        return impot_general_revenu


class salaire_net_a_payer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire net à payer"

    def formula(person, period, parameters):
        return (
            person('salaire_imposable', period)
            - person('impot_general_revenu', period)
            )
