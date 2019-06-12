# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *

class impots_indirects(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Impôts indirects payés par le ménage"

    def formula(household, period):
        return household('tva_total', period) + household('droit_de_douane', period)


class tva_total(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Taxe sur la valeur ajoutée"

    def formula(household, period, parameters):
        return = household('tva_taux_normal', period) + household('tva_taux_reduit', period)


class tva_taux_normal(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Taxe sur la valeur ajoutée - taux normal"

    def formula(household, period, parameters):
        exp_tva_normal = household('exp_tva_normal', period)
        taux = parameters(period).taxes.tva.taux_normal
        return exp_tva_normal*taux


class tva_taux_reduit(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Taxe sur la valeur ajoutée - taux réduit"

    def formula(household, period, parameters):
        exp_tva_reduit = household('exp_tva_reduit', period)
        taux = parameters(period).taxes.tva.taux_reduit
        return exp_tva_reduit*taux


class droits_de_douane(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Taxe sur la valeur ajoutée"

    def formula(household, period, parameters):
        return = household('exp_douane_plein', period) + household('exp_douane_intermediaire', period) + household('exp_douane_reduit', period)


class droits_de_douane_plein(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Droit de douane - taux plein"

    def formula(household, period, parameters):
        exp_douane_plein = household('exp_douane_plein', period)
        taux = parameters(period).taxes.douane.taux_plein
        return exp_douane_plein*taux


class droits_de_douane_intermediaire(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Droit de douane - taux intermediaire"

    def formula(household, period, parameters):
        exp_douane_intermediaire = household('exp_douane_intermediaire', period)
        taux = parameters(period).taxes.douane.taux_intermediaire
        return exp_douane_intermediaire*taux


class droits_de_douane_reduit(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Droit de douane - taux reduit"

    def formula(household, period, parameters):
        exp_douane_reduit = household('exp_douane_reduit', period)
        taux = parameters(period).taxes.douane.taux_reduit
        return exp_douane_reduit*taux


