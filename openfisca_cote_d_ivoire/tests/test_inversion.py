import logging


from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_core.taxscales import MarginalRateTaxScale

from openfisca_cote_d_ivoire import CountryTaxBenefitSystem as CoteDIvoireTaxBenefitSystem


log = logging.getLogger(__name__)


tax_benefit_system = CoteDIvoireTaxBenefitSystem()

# famille = prelevements_sociaux.

period = 2013
test_case = {
    'persons': {
        'A': {
            'salaire': {period: 12 * 100000}
            },
        },
    }

impot_revenu = tax_benefit_system.parameters.prelevements_obligatoires.impot_revenu.bareme(period)
prelevements_sociaux = tax_benefit_system.parameters.prelevements_obligatoires.prelevements_sociaux.retraite.salarie(period)

simulation_builder = SimulationBuilder()
simulation = simulation_builder.build_from_entities(tax_benefit_system, test_case)

salaire_net_a_payer = simulation.calculate('salaire', period)

salaire_imposable = impot_revenu.inverse().calc(salaire_net_a_payer)

salaire_brut = prelevements_sociaux.inverse().calc(salaire_imposable)

print(salaire_brut)
