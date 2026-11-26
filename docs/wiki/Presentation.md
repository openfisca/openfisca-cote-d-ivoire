# Description du système socio-fiscal ivoirien

# Impôts Directs
## Impôts sur le revenu (Traitements, salaires, pensions, rentes viagères et contributions annexes)

EXONERATIONS (art. 116) : il y en a plusieurs, assez spécifiques, la plus notable, étant donné nos données est peut-être celle sur les allocations familiales. 

REVENU IMPOSABLE (RI) = 80% du total des revenus (art. 119) 

Abattements supplémentaires (art. 119) : 
 - 60 000 fcfa par mois sur le montant net imposable pour les agriculteurs autres que ceux mentionnés dans l'art. 148 (la liste est longue dans l'article 148) (art. )
 - 300 000 fcfa par mois sur le montant ("net" n'est pas précisé) pour les pensions et rentes viagères. 

Toute fraction annuelle n'excédant pas 1000 fcfa est négligée dans le calcul du revenu total. (art. 120)

MODE DE PERCEPTION : retenue à la source. Si l'entreprise est étrangère : déclaratif. (art. 121 et 122)

CALCUL de l'impôt sur le revenu : 

Definition du nombre de parts : 
 - célibataire/divorcé/veuf, sans enfant = 1
 - Marié, sans enfant = célibataire/divorcé, 1 enfant = 2
 - Marié/veuf, 1 enfant = célibataire/divorcé, 2 enfants = 2,5
 - Marié/veuf, 2 enfants = célibataire/divorcé, 3 enfants = 3
 -  Marié/veuf, 3 enfants = célibataire/divorcé, 4 enfants = 3,5
 - etc ... jusqu'à 5 max. 

Un enfant est considéré comme étant à charge si et seulement si il est mineur (moins de 18), ou a moins de 27 et continue d'étudier. 

Pour connaître le taux on divise le RI par le nombre de parts pour obtenir le quotient fiscal, auquel on applique un taux selon le barème progressif suivant : 

| RI/nombre de parts est entre    | taux |
| ------------------------------- | ---- |
| 1000 et 2 200 000  		  |  2%  |
| 2 200 001 et 3 600 000 	  | 10%  |
| 3 600 001 et 5 200 000 	  | 15%  |
| 5 200 001 et 7 200 000	  | 20%  |
| 7 200 001 et 9 600 000	  | 24%  |
| 9 600 001 et 12 600 000	  | 26%  |
| 12 600 001 et 20 000 000	  | 29%  |
| 20 000 001 et 30 000 000	  | 32%  |
| 30 000 001 et 40 000 000	  | 34%  |
| 40 000 001 et 50 000 000	  | 35%  |
| 50 000 001 et + 		  | 36%  |

Etrangement ce barème s'applique à la somme de tous les revenus SAUF les salaires : 

Pour l'imposition - prélevée à la source - des salaires, il faut utiliser ce barème : 

| RI/nombre de parts est entre    | taux   |
| ------------------------------- | ----   |
| 0 et 300 000  		  |  0     |
| 300 000  et 547 000 	          | 10/110 |
| 548 000 et 979 000 	          | 15/115 |
| 980 000 et 1 519 000	          | 20/120 |
| 1 520 000 et 2 644 000	  | 25/125 |
| 2 645 000 et 4 669 000	  | 35/135 |
| 4 670 000 et 10 106 000	  | 45/145 |
| 10 106 000	                  | 60/160 |

Et ajouter - à l'impôt prélevé à la source : 

1) la contribution nationale (CN) = 1.5 % de RI
2) l'impôt sur les salaire (IS - oui, l'appellation prête à confusion) = 1.5 % de RI

_Elément de calcul_ : dans l'enquête on ne sait pas 1) combien d'enfants à charges sont déclarés, 2) combien d'enfants à charges ont les autres adultes du ménages. J'opterais pour une solution qui assigne à la personne de référence du ménage seulement ses enfant propres. 

## Impôt sur les Bénéfices Industriels et Commerciaux : 

Le BIC correspond au `corporate_income_tax` de CEQ. Il s'applique aux personnes morales que sont les entreprises. Nous pouvons le prendre en compte, mais cela soulève de nombreux points méthodologiques difficiles (voir repos CEQ). 

Il existe par contre un impôt synthétique qui se substitue à la patente, à l'impôt sur les bénéfices et à la TVA, pour les personnes physiques indépendantes dont le 5 Millions FCFA < CA annuel < 50 Millions FCFA. (VERIFIER : et pour les personnes physiques indépendantes dont le CA est supérieur que se passe-t-il ?)

Le montant est le suivant : 

| CA annuel                       | Montant impôt |
| ------------------------------- | ----          |
| jusqu'à 5 M    		  |  0            |
| 5 M à 6 M             	  | 491 400       |
| 6 M à 7 M 	                  | 573 300       |
| 7 M à 8 M               	  | 655 200       |
| 8 M à 9 M             	  | 737 100       |
| 9 M à 10 M            	  | 819 000       |
| 10 M à 11 M           	  | 900 000       |
| 11 M à 12 M            	  | 982 000       |
| 12 M à 13 M           	  | 1 064 000     |
| etc                   	  | ...           |
| 48 M à 50M     		  | 3 920 000     |

_Variable d'input_ : `inc_act1`, `independant`, `formel` (ou `Y_inc_act1_formel` et `independant`)

_Element de calcul_ : nous n'avons pas le chiffre d'affaire dans l'enquête, seulement les revenus d'activités principales et secondaires. Impossible de savoir, pour l'activité secondaire, si des impôts sont prélevés ou non. Comment, à partir de cette information, revenir au CA pour comprendre combien d'impôts ont été payés ?  

## Impôt sur le revenu foncier : 

TAUX : 3% de la valeur locative (valeur locative = loyers perçus ou, si proprio occupe le lieu, loyers qu'il pourrait en tirer s'il le louait) 

_Variable d'input_ : `inc_rent`,`imputed_rent`, `proprietaire` (+ une dummy estimée disant si l'impôt est payé ?)

_Element de calcul_ : applique le taux de 3% à ce qui à `inc_rent`,`imputed_rent` à la somme des revenus locatifs individuels (souvent ceux qui ont un `inc_rent` positifs, ont aussi un `imputed_rent` positif). Plusieurs personnes peuvent se partager la propriété du logement principal, dans ce cas il faudra diviser l'`imputed_rent` entre les propriétaires (idéalement il faudrait la diviser entre les personnes qui aurait payé le loyer, si l'un au moins des membres n'était pas propriétaire). Le plus gros problème ici vient du fait que l'on ne sait pas lesquels des propriétaires paient effectivement l'impôt sur le loyer. 

## Impôt sur le patrimoine foncier : 
TAUX : 9% de la valeur locative
taux réduit à 3% dans certains cas
_Element de calcul_ :qui paie l'impôt ?

## Taxe d'Habitation : 
Due par les personnes physiques ou morales occupant les immeubles d'habitation en qualité de propriétaire ou de locataire.
Montant forfaitaire : 20 000 FCFA/an 
_Element de calcul_ :qui paie l'impôt ?

# Impôts Indirects
## Taxe sur la valeur Ajoutée 

EXONERATION (art 355) : transports routiers, ferroviers, fluviaux, maritimes, aériens, et lagunaires de voyageurs et de marchandise (point 8), les ventes ou fournitures de produits alimentaires _**naturels**_ destinés à la consommation en Côte d'Ivoire y compris le poisson simplement congelé (point 9), les opérations de vente, commission courtage et façon portant sur le pain, les farines de céréales quelconques et les céréales destinées à la fabrications de ces farines (point 10); les honoraires du membre médical ainsi que les soins présentant un caractère médical (point 15); l'activité d'enseignement (point 16 -- mais pas ce qui s'y rapporte type équipement scolaires, demi-pension etc ...); les engrais, intrants semences et insecticides (point 29-33); la tranche sociale de livraison d'eau et d'électricité facturées aux ménages)

TAUX (art 359) : 
* général : 18% 
* taux réduit : 9% pour lait, pâtes alimentaires à base de semoule de blé dur, produits pétrolier, matériels de production énergie solaire

_Element de calcul_ : appliquer le taux à la somme des dépenses effectués pour ces produits.  

## Droits d'Assises
### Taxe spécifique unique sur les produits pétroliers
sur importations et ventes de PP.

cf. image pour le montant par litre de PP

### Boissons

champagne, vins mousseux et autres à moins de 35° : 40% ; vins ordinaires : 35% ; bières : 17%; autres à plus de 35° : 45%

boissons non alcoolisées (sauf eau) : 14%

### Tabacs
36% du prix de vente

## Droits de Douanes (TEC UEMOA)
* Biens sociaux essentiels : 0%
* Biens de première nécessité, matières premières de base, biens d'équipement, intrants spécifiques : 5%
* Intrants et produits intermédiaires : 10%
* Biens de conso finale et autres : 20%

_Element de calcul_ : Il n'y a pas d'informations dans l'enquête qui permette de savoir si les biens ont été importés ou pas sauf pour ces biens dont on sait qu'ils n'ont pas pu être produit en Côte d'Ivoire (ex : ordinateurs). Quelle hypothèse d'incidence ? 

# Ces autres impôts que l'on prend en compte

TAXE SPECIALE SUR LE TABAC POUR LE DÉVELOPPEMENT DU SPORT : 5% du prix de vente (en plus de la TVA) 

# Ces autres impôts que l'on ne prend pas en compte

DROITS D'ENREGISTREMENT SUR LE CACAO : quelle proportions des revenus générés par l'état représentent-ils ? 

# Transferts et subventions

## Transferts 

_Variables_ : `inc_grant`

_Element de calcul_ : il y a très peu d'info la dessus dans l'enquête, et le peu de questions qui existent ont reçu très peu de réponses informatives. 

## subventions 

A VERIFIER

_Variables_ :

_Element de calcul_ :

# Services de santé et d'éducation 

## Santé 

_Variables_ : `nbr_consultation_ets_public`, `budget_sante`

_Element de calcul_ : Diviser le budget total de la santé par la somme pondérée de consultation en 2015 et allouer ce coût unitaire pour chaque consultation dans un établissement publique.  Toutes les consultations ne se valent pas, certains centres sont mieux dotés que d'autres probablement : essaie-t-on de prendre en compte ces différences ? 

## Education 

_Variables_ : `scolarise_ets_public`, `budget_sante`

_Element de calcul_ : Diviser le budget total de l'éducation par la somme pondérée d'enfant scolarisés en 2015 et allouer ce coût unitaire pour chaque enfant scolarisé dans un établissement publique. Comme pour la santé il peut y avoir des différences de dotations importantes.




 

