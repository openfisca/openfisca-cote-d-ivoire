from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class accidents_du_travail(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale accidents du travail (employeur)"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        accidents_du_travail = parameters(period).prelevements_obligatoires.prelevements_sociaux.accidents_du_travail
        taux_minimal = accidents_du_travail.taux_minimal
        return taux_minimal * salaire


class famille(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale prestations familiales (employeur)"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        famille = parameters(period).prelevements_obligatoires.prelevements_sociaux.prestations_familiales
        return famille.calc(salaire)


class retraite_employeur(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (employeur)"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return retraite.employeur.calc(salaire)


class retraite_salarie(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Cotisation sociale retraite (salarié)"

    def formula(person, period, parameters):
        salaire = person('salaire', period)
        retraite = parameters(period).prelevements_obligatoires.prelevements_sociaux.retraite
        return retraite.salarie.calc(salaire)
