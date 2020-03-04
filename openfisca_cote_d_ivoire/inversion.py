from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class salaire_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire brut"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        nombre_de_parts = person.household('nombre_de_parts', period)

        impot_revenu = parameters(period).prelevements_obligatoires.impot_revenu.bareme.copy()
        abattement = parameters(period).prelevements_obligatoires.impot_revenu.abattement
        # We have to deal with abattement
        impot_revenu.multiply_thresholds(1.0 / abattement)
        impot_revenu.multiply_rates(abattement)
        prelevements_sociaux = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite.salarie
        salaire_imposable = nombre_de_parts * impot_revenu.inverse().calc(salaire / nombre_de_parts)
        salaire_brut = 12 * prelevements_sociaux.inverse().calc(salaire_imposable / 12)
        return salaire_brut
