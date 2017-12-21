Feature: Registering a tester

Background:
Given I am on Home Page

@suite1
Scenario:  Assert Home Screen Title
    When I open the home screen
    Then I must see the page title "Classe de Testes – Testes e Qualidade de Software"

@suite1
Scenario:  Assert Curso Selenium Header Title
    When I click on sub menu item Curso Selenium
    Then I must see the header with title "Curso Selenium"

@suite2
Scenario:  Assert Formulário Simples Header Title
    When I click on sub menu item Formulario Simples
    Then I must see the header with title "Formulário Simples"

@suite2
Scenario:  Assert Formulário Simples Header Title
    When I search for "teste"
    Then I must see the header with title "Resultados da pesquisa por: teste"

@suite2
Scenario:  Search with no results
    When I search for "futebol"
    Then I must see the header with title "Nada Encontrado"
