# -*- coding: utf-8 -*-


import logging
import os
import pkg_resources


import pandas as pd
from slugify import slugify


from openfisca_ceq.tools import add_ceq_framework
from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem
from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario
from openfisca_cote_d_ivoire.tests.test_survey_scenario_from_stata_data import (
    data_is_available,
    create_data_from_stata,
    )


def create_survey_sceanrio():
    tax_benefit_system = CoteDIvoireTaxBenefitSystem()
    ceq_enhanced_tax_benefit_system = add_ceq_framework(tax_benefit_system)
    if not data_is_available:
        return
    data = create_data_from_stata()
    survey_scenario = CoteDIvoireSurveyScenario(
        tax_benefit_system = ceq_enhanced_tax_benefit_system,
        data = data,
        year = 2017,
        )
    return survey_scenario


def read_aggregates():
    package_path = pkg_resources.get_distribution("openfisca-cote-d-ivoire").location
    asset_path = os.path.join(package_path, "openfisca_cote_d_ivoire", 'assets')
    file_path = os.path.join(asset_path, 'recettes_fiscales_CIV.csv')
    recettes = pd.read_csv(file_path)

    recettes.columns = [slugify(column, separator = "_") for column in recettes.columns]
    description_3_by_variable = {
        "impot_general_revenu": "Impot sur les revenu et salaires"
        }

    recette_by_variable = dict(
        (variable, recettes.loc[recettes.description_3 == description_3, "montant_en_milliard_de_fcfa"].values[0])
        for variable, description_3 in description_3_by_variable.items()
        )
    return recette_by_variable


def test_aggregates():
    recette_by_variable = read_aggregates()
    survey_scenario = create_survey_sceanrio()
    period = 2017
    if survey_scenario is not None:
        for variable, recette in recette_by_variable.items():
            logging.info(survey_scenario.compute_aggregate(variable, period = period) / 1e9)
            logging.info(recette)


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    test_aggregates()
