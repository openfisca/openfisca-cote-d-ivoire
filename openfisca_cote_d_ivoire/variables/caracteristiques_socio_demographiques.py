# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


class age(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Âge de l'individu (en années)"


class veuf_ve(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Variable binaire déterminant si la personne de référence est veuf-ve ou pas"


class occupation_principale_taxee(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Variable binaire déterminant si les revenus de l'activité principale sont taxés ou non "


class proprietaire_residence_principale(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Variable binaire déterminant si l'habitation est détenue par le ménage"


class residence_principale_taxee(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Variable binaire déterminant si le menage paie des impôts sur sa résidence principale"


class nombre_enfants_a_charge(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Nombre d'enfants de la personne de référence et de son/sa conjointe dans le ménage"

    def formula(household, period):
        nombre_enfants_a_charge = household.nb_persons(Household.ENFANT)
        return nombre_enfants_a_charge


class marie(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Variable binaire indiquant si la personne de référence a un-e conjoint-e dans le ménage"

    def formula(household, period):
        marie = household.nb_persons(Household.CONJOINT) > 0
        return marie


class nombre_de_parts(Variable):
    value_type = int
    default_value = 1
    entity = Household
    definition_period = YEAR
    label = "Nombre de parts fiscales pour le calcul de l'impôt sur le revenu"

    def formula(household, period):
        nombre_enfants_a_charge = household('nombre_enfants_a_charge', period)
        marie = household('marie', period)
        veuf_ve = household('veuf_ve', period)
        condition_pas_enfant = nombre_enfants_a_charge == 0
        condition_marie_ou_veuf_ve = marie + veuf_ve
        nombre_de_parts = 1
        return select(
            [
                (not_(marie) + veuf_ve) * condition_pas_enfant,
                marie * condition_pas_enfant,
                condition_marie_ou_veuf_ve * not_(condition_pas_enfant),
                not_(condition_marie_ou_veuf_ve) * not_(condition_pas_enfant)
                ],

            [
                nombre_de_parts,
                nombre_de_parts + 1,
                nombre_de_parts + 1 + (nombre_enfants_a_charge / 2),
                nombre_de_parts + 0.5 + (nombre_enfants_a_charge / 2)
                ],
            )
