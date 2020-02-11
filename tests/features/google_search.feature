Feature: Google search

    Scenario: User searches with results
        Given I visit the website "https://www.google.com"
        When I fill "lendingfront"
        Then Validate that the search has results

    Scenario: User searches with results
        Given I visit the website "https://www.google.com"
        When I fill "56465465464.465464644"
        Then I see this text "No se han encontrado resultados para tu búsqueda"
