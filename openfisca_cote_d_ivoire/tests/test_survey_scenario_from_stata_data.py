# -*- coding: utf-8 -*-


import configparser
import logging
import os


from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario
from openfisca_survey_manager import default_config_files_directory as config_files_directory


log = logging.getLogger(__file__)


def test_load_stata_data():
    circleci = 'CIRCLECI' in os.environ
    if circleci:
        return
    config_parser = configparser.SafeConfigParser()
    config_parser.read(os.path.join(config_files_directory, 'raw_data.ini'))
    assert config_parser.has_section("cote_d_ivoire")
    file_path_by_year = dict(config_parser.items("cote_d_ivoire"))
    data_file_path = file_path_by_year["2014"]
    # df = pd.read_stata(data_file_path)
    # import pprint
    # pprint.pprint(sorted(df.columns))
    data = dict()
    data['stata_file_by_entity'] = dict(
        # household = os.path.join(data_directory, 'household.dta'),
        person = os.path.join(data_file_path),
        )
    year = 2017
    survey_scenario = CoteDIvoireSurveyScenario(
        data = data,
        year = year,
        )
    df = survey_scenario.create_data_frame_by_entity(variables = ['age'])['person']
    df.hist(bins = 50)


if __name__ == '__main__':
    test_load_stata_data()
