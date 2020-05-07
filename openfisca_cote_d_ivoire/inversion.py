from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class autres_revenus_du_capital_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu des capitaux brut"

    def formula(individu, period, parameters):
        taux = parameters(period).prelevements_obligatoires.impot_revenu.creances.taux
        return individu('autres_revenus_du_capital', period) / (1 - taux)


class revenu_foncier_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu locatif (foncier) brut"

    def formula(individu, period, parameters):
        taux = parameters(period).prelevements_obligatoires.impot_revenu.foncier
        return individu('revenu_locatif', period) / (1 - taux)


class revenu_non_salarie_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenu non salarie brut"

    def formula(individu, period, parameters):
        return individu('revenu_non_salarie', period)


class pension_retraite_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR

    def formula(individu, period, parameters):
        return individu('pension_retraite', period)


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
