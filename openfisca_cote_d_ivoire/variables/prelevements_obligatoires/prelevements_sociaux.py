from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class accidents_du_travail(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale accidents du travail (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        accidents_du_travail = parameters(period).prelevements_obligatoires.prelevements_sociaux.accidents_du_travail
        taux_minimal = accidents_du_travail.taux_minimal
        return taux_minimal * salaire_brut_annuel


class cotisations_salariales(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale salariales"

    def formula(person, period):
        return person('retraite_salarie', period)


class cotisations_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale employeur"

    def formula(person, period):

        return (
            person('accidents_du_travail', period)
            + person('famille', period)
            + person('retraite_employeur', period)
            )


class famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale prestations familiales (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        famille = parameters(period).prelevements_obligatoires.prelevements_sociaux.prestations_familiales
        return 12 * famille.calc(salaire_brut_annuel / 12)


class retraite_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (employeur)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return 12 * retraite.employeur.calc(salaire_brut_annuel / 12)


class retraite_salarie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (salarié)"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return 12 * retraite.salarie.calc(salaire_brut_annuel / 12)


class salaire_imposable(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire imposable"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        cotisations_salariales = person('cotisations_salariales', period)
        return salaire_brut_annuel - cotisations_salariales


class salaire_super_brut(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaire imposable"

    def formula(person, period, parameters):
        salaire_brut_annuel = person('salaire_brut', period)
        cotisations_employeur = person('cotisations_employeur', period)
        return salaire_brut_annuel + cotisations_employeur


class sante_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation santé employeur"

    def formula_2019_07_01(person, period, parameters):
        # TODO FIXME car pas clair
        # https://www.cleiss.fr/docs/regimes/regime_cotedivoire.html#cmu
        salarie = person('salaire_brut', period) > 0
        cotisation = parameters(period).prelevements_obligatoires.prelevements_sociaux.cmu_obligatoire
        return 12 * salarie * cotisation


class sante_salarie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation santé employeur"

    def formula_2019_07_01(person, period, parameters):
        # TODO FIXME car pas clair
        # https://www.cleiss.fr/docs/regimes/regime_cotedivoire.html#cmu
        salarie = person('salaire_brut', period) > 0
        cotisation = parameters(period).prelevements_obligatoires.prelevements_sociaux.cmu_obligatoire
        return 12 * salarie * cotisation
