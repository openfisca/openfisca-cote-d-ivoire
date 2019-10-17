# -*- coding: utf-8 -*-

import logging


from openfisca_cote_d_ivoire.input_data_builder import (
    data_is_available,
    create_data_from_stata,
    )


from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario


def test_analyse_primaire():
    if not data_is_available:
        return
    year = 2017
    data = create_data_from_stata(create_dataframes = True)
    survey_scenario = CoteDIvoireSurveyScenario(
        year = year,
        data = data,
        )

    df_by_entity = survey_scenario.create_data_frame_by_entity(
        variables = ['age', 'salaire', 'impot_general_revenu', 'impots_directs', 'person_weight']
        )

    for entity, df in df_by_entity.items():
        logging.info(entity)
        logging.info(df)

    df['weighted_impot'] = df.person_weight * df.impot_general_revenu
    df['average_impot_rate'] = df.impot_general_revenu * 100 / df.salaire
    logging.info(df.weighted_impot.sum())
    logging.info(df.average_impot_rate.mean(skipna = True))


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    test_analyse_primaire()
