# -*- coding: utf-8 -*-

import logging
import os


from openfisca_ceq.tools.tax_benefit_system_completion import (
    add_ceq_framework,
    ceq_variables,
    get_all_neutralized_variables,
    )


from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem
from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario
from openfisca_cote_d_ivoire.input_data_builder import (
    data_is_available,
    create_data_from_stata,
    )


log = logging.getLogger(__file__)


def test_survey_scenario(create_dataframes = True):
    circleci = 'CIRCLECI' in os.environ
    if circleci or not data_is_available:
        return

    year = 2017
    data = create_data_from_stata(create_dataframes = create_dataframes)
    survey_scenario = CoteDIvoireSurveyScenario(
        data = data,
        year = year,
        )
    df_by_entity = survey_scenario.create_data_frame_by_entity(
        variables = ['age', 'salaire', 'impot_general_revenu', 'impots_directs']
        )

    for entity, df in df_by_entity.items():

        log.debug(entity)
        assert not df.empty, "{} dataframe is empty".format(entity)
        log.debug(df)


def test_ceq_survey_scenario(create_dataframes = True):
    circleci = 'CIRCLECI' in os.environ
    if circleci or not data_is_available:
        return
    tax_benefit_system = CoteDIvoireTaxBenefitSystem()
    ceq_enhanced_tax_benefit_system = add_ceq_framework(tax_benefit_system)
    if not data_is_available:
        return
    data = create_data_from_stata()
    year = 2017
    survey_scenario = CoteDIvoireSurveyScenario(
        tax_benefit_system = ceq_enhanced_tax_benefit_system,
        data = data,
        year = year,
        )

    country_variables = ['age', 'salaire', 'impot_general_revenu']

    variables = country_variables + list(ceq_variables.keys())
    df_by_entity = survey_scenario.create_data_frame_by_entity(
        variables = variables
        )

    by_design_neutralized_variables_by_entity, de_facto_neutralized_variables_by_entity = \
        get_all_neutralized_variables(survey_scenario, period = year, variables = variables)

    for entity, df in df_by_entity.items():
        log.debug(entity)
        assert not df.empty, "{} dataframe is empty".format(entity)
        for variable in df.columns:
            log.debug("{} aggregate: {}".format(
                variable,
                survey_scenario.compute_aggregate(variable, period = year)
                / 1e9
                ))
        log.debug("Neutralized by design for entity {}:\n  {}".format(
            entity,
            sorted(by_design_neutralized_variables_by_entity[entity]))
            )
        log.debug("Neutralized de facto for entity {}:\n  {}".format(
            entity,
            sorted(de_facto_neutralized_variables_by_entity[entity]))
            )
        log.debug("Non null ceq vars for entity {}: {}".format(
            entity,
            sorted(list(
                set([
                    variable
                    for variable in ceq_variables.keys()
                    if ceq_enhanced_tax_benefit_system.variables[variable].entity.key == entity
                    ])
                .difference(
                    set(
                        by_design_neutralized_variables_by_entity[entity]
                        + de_facto_neutralized_variables_by_entity[entity]
                        )
                    )
                ))
            ))


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    # test_survey_scenario()
    test_ceq_survey_scenario()
