from openfisca_cote_d_ivoire.input_data_builder import (
    data_is_available,
    create_data_from_stata,
    )
from openfisca_cote_d_ivoire.survey_scenarios import CoteDIvoireSurveyScenario


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
    print(entity)
    print(df)
