Feature: Tester le function de filtrer les pages wike par tag.
         Se connecter avec un compte avec un site existant et il y a plusieur page wiki
         dans le site avec tag. Filtrer les pages wiki par un tag.

  Scenario: Filtrer les pages wike par tag
    Given se connecter avec un compte
    When creer un site
    And creer les pages wiki avec tag
    Then filtrer les pages wiki par tag
    And supprimer le site
    And deconnecter