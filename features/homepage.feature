Feature: Registering a tester

Background:
Given I am on Home Page

Scenario:  Assert Home Screen Title
    When I open the home screen
    Then I must see the page title "Classe de Testes | Testes e Qualidade de Software"

Scenario:  Assert Curso Selenium Header Title
    When I click on sub menu item Curso Selenium
    Then I must see the header with title "Curso Selenium"

Scenario:  Assert Formulário Simples Header Title
    When I click on sub menu item Formulario Simples
    Then I must see the header with title "Formulário Simples"

Scenario:  Assert Formulário Simples Header Title
    When I search for "teste"
    Then I must see the header with title "Resultados da pesquisa por: teste"

Scenario:  Search with no results
    When I search for "futebol"
    Then I must see the header with title "Nada Encontrado"
