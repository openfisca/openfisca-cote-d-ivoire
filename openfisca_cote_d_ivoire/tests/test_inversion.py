import logging


from openfisca_core.simulation_builder import SimulationBuilder

from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem


log = logging.getLogger(__name__)


tax_benefit_system = CoteDIvoireTaxBenefitSystem()
# prelevements_sociaux = tax_benefit_system.parameters.prelevements_obligatoires.prelevements_sociaux

# famille = prelevements_sociaux.

year = 2013
test_case = {
    'persons': {
        'A': {
            'salaire': {year: 12 * 100000}
            },
        },
    }

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, test_case)
