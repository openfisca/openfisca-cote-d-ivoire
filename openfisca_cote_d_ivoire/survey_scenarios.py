# -*- coding: utf-8 -*-

from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem

from openfisca_survey_manager.scenarios import AbstractSurveyScenario
from openfisca_survey_manager.utils import stata_files_to_data_frames


class CoteDIvoireSurveyScenario(AbstractSurveyScenario):

    def __init__(self, tax_benefit_system = None, baseline_tax_benefit_system = None,
            data = None, year = None):
        super(CoteDIvoireSurveyScenario, self).__init__()
        if tax_benefit_system is None:
            tax_benefit_system = CoteDIvoireTaxBenefitSystem()
        self.set_tax_benefit_systems(
            tax_benefit_system = tax_benefit_system,
            baseline_tax_benefit_system = baseline_tax_benefit_system,
            )

        assert year is not None
        self.year = year

        if data is None:
            return

        variables_from_stata_files = stata_files_to_data_frames(data, period = year)
        self.used_as_input_variables = list(
            set(tax_benefit_system.variables.keys()).intersection(
                set(variables_from_stata_files)
                )
            )
        period = data["input_data_frame_by_entity_by_period"].keys()[0]
        input_data_frame_by_entity = data["input_data_frame_by_entity_by_period"].values()[0]
        person_data_frame = input_data_frame_by_entity['person']
        person_data_frame['household_id'] = person_data_frame.id
        person_data_frame['person_id'] = person_data_frame.id
        person_data_frame['household_legacy_role'] = 0

        data["input_data_frame_by_entity_by_period"][period] = dict(person = person_data_frame)

        self.init_from_data(data = data)
