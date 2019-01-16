# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class age(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = u"Âge de l'individu (en années)"


class occupation_principale_taxee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Variable binaire déterminant si les revenus de l'activité principale sont taxés ou non "


class proprietaire_resid_principale(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = u"Variable binaire déterminant si l'habitation est détenue par le ménage"

class residence_principale_taxee(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = u"Variable binaire déterminant si le menage paie des impôts sur sa résidence principale"


class nb_persons(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Nombre de personnes dans le ménage"

    def formula(household, period):
        nb_persons = household.nb_persons()
        return nb_persons

class nb_enfants_a_charge(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Nombre d'enfants de la personne de référence et de son/sa conjointe dans le ménage"

    def formula(household, period):
        nb_enfants_a_charge = household.nb_persons(Household.ENFANT)
        return nb_enfants_a_charge

class nb_conjoint(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Variable binaire indiquant si la personne de référence a un-e conjoint-e dans le ménage"

    def formula(household, period):
        nb_conjoint = household.nb_persons(Household.CONJOINT)
        return nb_conjoint

class nombre_de_parts(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Nombre de parts fiscales pour le calcul de l'impôt sur le revenu"

    def formula(household, period):
        # reprendre ici
        return nombre_de_parts

