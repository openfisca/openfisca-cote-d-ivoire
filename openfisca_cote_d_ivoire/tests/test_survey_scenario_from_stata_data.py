# -*- coding: utf-8 -*-

import logging
import os
from openfisca_cote_d_ivoire.input_data_builder import (
    data_is_available,
    create_data_from_stata,
    )
from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario


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
        log.debug(df)


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    test_survey_scenario()
    # test_ceq_survey_scenario()
