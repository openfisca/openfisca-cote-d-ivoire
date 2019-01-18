# -*- coding: utf-8 -*-


from openfisca_core.model_api import *
from openfisca_cote_d_ivoire.entities import *


# class corporate_income_tax(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = "Corporate Income Tax"


# class customs_duties(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = "Customs Duties"


# class excise_taxes(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = " Excise Taxes"


# class sales_tax(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = " Sales Tax"


# class value_added_tax(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = " Value added tax (VAT)"


# class other_taxes(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = "Other taxes"


# class payroll_tax(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = "Payroll Tax"


class personal_income_tax(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Personal Income Tax"

    def formula(household, period):
        impot_general_revenu_individu = household.members('impot_general_revenu', period)
        return household.sum(impot_general_revenu_individu)


# class property_tax(Variable):
#     value_type = float
#     entity = Household
#     definition_period = YEAR
#     label = "Taxes on Property "
