# -*- coding: utf-8 -*-


from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class salaire(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Salaires et Traitements tirés d'une activitée formelle (activité principale)"


class revenus_activites_secondaires(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tous les revenus tirés des activitées secondaires"


class pension(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Pension de retraite"


class revenus_locatifs(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenus tirés de la location de propriétés"


class interets_dividendes(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenus sous formes d'intérêt ou de dividendes"


class bourses_transfers(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenus sous formes ou de transferts directs émis par l'état (hors pension) ou des ONG/OI"


class aide_monetaire_autre_menage(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aide monétaire provenant d'autres ménages"


class aide_non_monetaire_autre_menage(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aide non-monétaire provenant d'autres ménages"


class autre_revenus_individuels(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Revenus individuels différents de ceux déjà listés dans l'enquête"


class revenus_complementaires_elevage(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Revenus tirés de la vente de produits d'elevage"


class revenus_complementaires_miel(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Revenus tirés de la vente d'autres produits agricoles"


class auto_consommation(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Revenus estimés à partir des denrées consommées produites."
