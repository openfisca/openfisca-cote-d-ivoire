
import configparser
import logging
import os
import pandas as pd


from openfisca_survey_manager import default_config_files_directory as config_files_directory
from openfisca_core import periods


log = logging.getLogger(__file__)


config_parser = configparser.ConfigParser()
config_parser.read(os.path.join(config_files_directory, 'raw_data.ini'))
data_is_available = config_parser.has_section("cote_d_ivoire")
if not data_is_available:
    log.info("No data available for Côte d'Ivoire")


def get_data_file_path():
    file_path_by_year = dict(config_parser.items("cote_d_ivoire"))
    return file_path_by_year['2014']


def create_dataframes_from_stata_data():
    data_file_path = get_data_file_path()
    # import pprint
    # dico_labels = pd.read_stata(data_file_path, iterator=True)
    # pprint.pprint(dico_labels.variable_labels())

    from openfisca_ceq.tools.data_ceq_correspondence import (
        ceq_input_by_person_variable,
        ceq_intermediate_by_person_variable,
        non_ceq_input_by_person_variable,
        )
    renamings = [
        ceq_input_by_person_variable,
        ceq_intermediate_by_person_variable,
        non_ceq_input_by_person_variable,
        ]
    revenues_variable = sum(
        [list(variables.keys()) for variables in renamings],
        []
        )

    dataframe = pd.read_stata(data_file_path)
    assert set(revenues_variable).issubset(set(dataframe.columns)), \
        "Some mandatory revenue variables are not present: ".fromat(
            set(revenues_variable).difference(set(dataframe.columns))
            )
    person_variables = revenues_variable + [
        # 'age',
        'hhid',
        'pid',
        'pond',
        # 'sex'
        'weight',
        ]
    renamed_columns = dict(
        renaming
        for partial_renamings in renamings
        for renaming in partial_renamings.items()
        )  # merging dictionnaries
    person_dataframe = (dataframe[person_variables]
        .copy()
        .rename(columns = renamed_columns)
        )
    # person_dataframe['household_role_index'] = (
    #     0 * (person_dataframe.link_to_head == 'chef de menage')
    #     + 1 * (person_dataframe.link_to_head == 'epouse ou mari')
    #     + 2 * (
    #         (person_dataframe.link_to_head != 'chef de menage') & (person_dataframe.link_to_head != 'epouse ou mari')
    #         )
    #     )
    person_dataframe['household_role_index'] = (
        person_dataframe.groupby("hhid")['pid'].rank() - 1
        ).astype(int)
    person_dataframe['household_role_index'] = person_dataframe['household_role_index'].where(
        person_dataframe['household_role_index'] < 2,
        2,
        )
    household_id_by_hhid = (person_dataframe.hhid
        .drop_duplicates()
        .sort_values()
        .reset_index(drop = True)
        .reset_index()
        .rename(columns = {'index': 'household_id'})
        .set_index('hhid')
        .squeeze()
        )
    person_dataframe['household_id'] = person_dataframe['hhid'].map(household_id_by_hhid)
    person_dataframe['person_id'] = range(len(person_dataframe))

    person_dataframe = person_dataframe.rename(columns = {
        'pond': 'person_weight',
        })
    person_dataframe['sexe'] = person_dataframe.sexe.str.startswith('F')
    assert (dataframe.groupby('hhid')['weight'].nunique() == 1).all()

    household_weight = dataframe.groupby('hhid')['weight'].mean()
    household_dataframe = pd.DataFrame(
        dict(
            household_id = range(person_dataframe.household_id.max() + 1),
            household_weight = household_weight.values,
            )
        )

    from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem
    from openfisca_ceq.tools.tax_benefit_system_completion import add_ceq_framework
    tax_benefit_system = CoteDIvoireTaxBenefitSystem()
    ceq_enhanced_tax_benefit_system = add_ceq_framework(tax_benefit_system)
    ceq_enhanced_tax_benefit_system

    household_variables = [
        variable_name
        for variable_name, variable_instance in ceq_enhanced_tax_benefit_system.variables.items()
        if variable_instance.entity.key == 'household'
        ]

    transferred_variables = list()
    for variable in household_variables:
        # TODO improve by better filtering and better filling NAs
        if variable in ['household_weight']:
            continue
        if variable not in person_dataframe.columns:
            continue
        log.debug("Moving {} from person to household".format(variable))
        household_dataframe[variable] = person_dataframe.groupby('household_id')[variable].fillna(0).sum()
        transferred_variables.append(variable)

    person_dataframe.drop(columns = transferred_variables, inplace = True)

    return person_dataframe, household_dataframe


def create_data_from_stata(create_dataframes = True):
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
    return data


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    person_dataframe, household_dataframe = create_dataframes_from_stata_data()
