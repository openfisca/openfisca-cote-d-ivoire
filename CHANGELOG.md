# Changelog

### 0.9.3 [#XXXX](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/XXXX)

* Amélioration technique.
  - Adapte aux nouvelles version de openfisca-survey-manager (0.23)

### 0.9.2 [#39](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/39)

* Amélioration technique.
  - Adapte aux nouvelles version de openfisca-core (34.20) et openfisca-survey-manager (0.20)

### 0.9.1 [#29](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/29)

* Amélioration technique.
  - Utilise ConfigParser au lieu de SafeConfigParser (fix #20)

## 0.9.0 [#27](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/27)

* Évolution du système socio-fiscal.
* Périodes concernées : toutes.
* Zones impactées : `weights`.
* Détails:
  - Ajoute household_weights
  - Ajoute person_weights
  - Ajoute test avec chargement du framework CEQ

## 0.8.0 [#24](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/24)

* Évolution du système socio-fiscal.
* Périodes concernées : toutes.
* Zones impactées : `revenus`.
* Détails:
  - Ajoute revenus_activites_secondaires
  - Ajoute pension
  - Ajoute revenus_locatifs
  - Ajoute interets_dividendes
  - Ajoute bourses_transfers
  - Ajoute aide_monetaire_autre_menage
  - Ajoute aide_non_monetaire_autre_menage
  - Ajoute autre_revenus_individuels
  - Ajoute revenus_complementaires_elevage
  - Ajoute revenus_complementaires_miel
  - Ajoute auto_consommation

## 0.7.0 [#XX](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/XX)

* Évolution du système socio-fiscal.

  - Ajoute `nombre_de_parts`

### 0.6.1 [#15](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/15)

* Amélioration technique.
  - Ajout de tests
  - Retire les teest python2

## 0.6.0 [#7](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/7)

* Amélioration technique.
  - Début de chargement des données

### 0.5.1 - [#6](https://github.com/openfisca/openfisca-cote-d-ivoire/pull/6)

* Technical change
  - Utilisation de la version core 25.2.2
  - Utilisatation de pytest au lieu de nose
  - Configure CircleCI
