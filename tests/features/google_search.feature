Feature: Google search

    Scenario: User searches with results
        Given User visit the website "https://www.google.com"
        When User fill "lendingfront"
        Then Validate that the search has results

      Scenario: User searches with not results fail
          Given User visit the website "https://www.google.com"
          When User fill "56465465464.465464644"
          Then Validate that the search has results


    Scenario: User searches with not results done
        Given User visit the website "https://www.google.com"
        When User fill "56465465464.465464644"
        Then User see this text "No se han encontrado resultados para tu búsqueda"
