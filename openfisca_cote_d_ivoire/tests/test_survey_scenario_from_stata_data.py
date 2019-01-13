# -*- coding: utf-8 -*-


import configparser
import logging
import os
import pandas as pd


from openfisca_core import periods
from openfisca_survey_manager import default_config_files_directory as config_files_directory
from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario


log = logging.getLogger(__file__)


def get_data_file_path():
    config_parser = configparser.SafeConfigParser()
    config_parser.read(os.path.join(config_files_directory, 'raw_data.ini'))
    assert config_parser.has_section("cote_d_ivoire")
    file_path_by_year = dict(config_parser.items("cote_d_ivoire"))
    return file_path_by_year['2014']


def create_dataframes_from_stata_data():
    data_file_path = get_data_file_path()
    import pprint
    dico_labels = pd.read_stata(data_file_path, iterator=True)
    pprint.pprint(dico_labels.variable_labels())
    dataframe = pd.read_stata(data_file_path)
    print(dataframe.link_to_head.value_counts(dropna = False))

    person_variables = [
        'age',
        'formel_informel',
        'hhid',
        'id',
        'inc_act1_ind',
        'link_to_head',
        'sex'
        ]
    person_dataframe = dataframe[person_variables].copy()
    person_dataframe['salaire'] = person_dataframe.inc_act1_ind * (
        (person_dataframe.formel_informel == 1) | (person_dataframe.formel_informel == 1)
        )
    person_dataframe['household_legacy_role'] = (
        0 * (person_dataframe.link_to_head == 'chef de menage')
        + 1 * (person_dataframe.link_to_head == 'epouse ou mari')
        + 2 * (
            (person_dataframe.link_to_head != 'chef de menage') & (person_dataframe.link_to_head != 'epouse ou mari')
            )
        )
    person_dataframe = person_dataframe.rename(columns = {
        'id': 'person_id',
        'hhid': 'household_id',
        'inc_pension_ind': 'pension',
        'sex': 'sexe'
        })

    household_dataframe = None

    household_variables = [
        'hh_id'
        ]
    return person_dataframe, household_dataframe


def test_load_stata_data(create_dataframes = True):
    circleci = 'CIRCLECI' in os.environ
    if circleci:
        return

    year = 2017
    data = dict()

    if create_dataframes:
        person_dataframe, household_dataframe = create_dataframes_from_stata_data()
        input_data_frame_by_entity = {
            'person': person_dataframe,
            'household': household_dataframe,
            }
        input_data_frame_by_entity_by_period = {periods.period(year): input_data_frame_by_entity}
        data['input_data_frame_by_entity_by_period'] = input_data_frame_by_entity_by_period

    else:
        data_file_path = get_data_file_path()
        data['stata_file_by_entity'] = dict(
            # household = os.path.join(data_directory, 'household.dta'),
            person = data_file_path,
            )

    survey_scenario = CoteDIvoireSurveyScenario(
        data = data,
        year = year,
        )
    df = survey_scenario.create_data_frame_by_entity(
        variables = ['age', 'salaire', 'impot_general_revenu']
        )['person']

    print(df)
    df.hist(bins = 50)


if __name__ == '__main__':
    test_load_stata_data()
